########################################################################
# Process data for learning via CC experiment 1
########################################################################
# Author: Ian Hussey (ian.hussey@ugent.be)

########################################################################
# Clean the workspace
rm(list=ls())

########################################################################
# Dependencies

# function to check if libraries are not already installed, and if not it installs them
auto_install_dependencies <- function(pkg){
  new.pkg <- pkg[!(pkg %in% installed.packages()[, "Package"])]
  if (length(new.pkg)) 
    install.packages(new.pkg, dependencies = TRUE)
}
packages <- c("plyr", "tidyverse", "data.table")
auto_install_dependencies(packages)

library(plyr) # must import before dplyr
library(tidyverse)
library(data.table)

########################################################################
# Data acquisition and cleaning

# Set the working directory in which to look for data files
setwd("~/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Experiment 1/Master data")

# Create a list of these files
files <- list.files(pattern = "\\.csv$")
# Read these files into a single dplyr-style data frame. You can remove the tbl_df() to get a standard data frame if you prefer.
data_df <- tbl_df(rbind.fill(lapply(files, fread, header=TRUE)))

# Make some variable names more transparent, plus rectify the the accuracy variable
data_df <- 
  data_df %>%
  rename(likertPre = likertPre.thisN, 
         likertPost = likertPost.thisN,
         blocks = blocks.thisN, # current block within a given task
         trial = trials.thisN, # trial order of presentation within each block
         rating = rating.response,
         rt = requiredResponse.rt, # first correct response rt
         #accuracy = feedbackResponse.corr # This is what would normally be used. However, some mistake in psychopy means
                                           # that all are recorded as wrong. The workaround is to use the presence of a feedbackResponse RT as an incorrect response.
         emmittedWrongAnswer = feedbackResponse.rt) %>% # accuracy of the first response (currently reversed: 0 = correct)
  mutate(accuracy = ifelse(is.na(emmittedWrongAnswer), 1, 0), 
         blocks = blocks + 1,   # recifites block to be 1 to 7 rather than 0-6 
         gender = ifelse(gender == "M", "m", # correct M to m
                         ifelse (gender == "FALSE", "f", gender)))

########################################################################
# Likert data
likert_data <-
  data_df %>%
  filter(!is.na(rating)) %>% 
  select(participant,
         rating,
         subscale,
         likertPre,
         likertPost) %>%
  gather(likertTimepoint, 
         likertOrderOfPresentation, 
         c(likertPre, likertPost), 
         na.rm = TRUE) %>%
  group_by(participant) %>%
  summarize(ratings_pre = mean(rating[subscale == 2 & likertTimepoint == "likertPre"]),
            ratings_post = mean(rating[subscale == 2 & likertTimepoint == "likertPost"]),
            valenced_stimuli_ratings = mean(rating[subscale == 1 & likertTimepoint == "likertPre"]),
            ratings_change_scores = ratings_post - ratings_pre)
    

########################################################################
# IAT data
D1_data <-
  data_df %>%
  filter(!is.na(rt)) %>% 
  group_by(participant) %>%
  filter(rt <= 10000) %>%
  ## D1 scores
  summarize(IAT_mean_RT = round(mean(rt[blocks == 3 | blocks == 4 | blocks == 6 | blocks == 7])*1000, 0), # mean RT in the critical blocks
            RT_block3_m = mean(rt[blocks == 3]), # D1 score blocks 3 and 6
            RT_block6_m = mean(rt[blocks == 6]),
            difference1 = RT_block6_m - RT_block3_m,
            RT_block3and6_SD = sd(rt[blocks == 3 | blocks == 6]),
            D1a = difference1 / RT_block3and6_SD,
            RT_block4_m = mean(rt[blocks == 4]), # D1 score blocks 4 and 7
            RT_block7_m = mean(rt[blocks == 7]),
            difference2 = RT_block7_m - RT_block4_m,
            RT_block4and7_SD = sd(rt[blocks == 4 | blocks == 7]),
            D1b = difference2 / RT_block4and7_SD) %>%
  mutate(D1 = round(((D1a + D1b)/2), 2)) %>% # Calculate D1
  
  # Condition variable is set within the task by the modulo of the participant code within the task, but I forgot to write it out to the data file.
  mutate(experimental_condition = (participant - 1)%%4 + 1, # sets condition to between 1 and 4
         condition = ifelse(experimental_condition == 1 | experimental_condition == 2, 
                                "flowers", 
                                ifelse(
                                  experimental_condition == 3 | experimental_condition == 4, 
                                  "insects", 
                                  "error")),
         block_order = ifelse(experimental_condition == 1 | experimental_condition == 4, 
                              "consistent_first", 
                              ifelse(
                                experimental_condition == 2 | experimental_condition == 3, 
                                "inconsistent_first", 
                                "error"))) %>%
    
  # D1 score rectifications
  # The logic of these rectifications is taken from the condition assignment within the psychopy code:
  # 1 First block = flowers-positive/chinese-negative      -> *-1 to make positive scores = chinese-positive 
  # 2 First block = flowers-negative/chinese-positive      -> positive scores = chinese-positive 
  # 3 First block = insects-positive/chinese-negative      -> *-1 to make positive scores = chinese-positive 
  # 4 First block = insects-negative/chinese-positive      -> positive scores = chinese-positive 
  # > Therefore positive D1 scores = chinese-positive for all conditions
  mutate(D1 = ifelse(experimental_condition == 1 | experimental_condition == 3, 
                     D1 *-1, 
                     ifelse(
                       experimental_condition == 2 | experimental_condition == 4, 
                       D1, 
                       "error"))) %>%
  select(participant,
         D1,
         condition,
         IAT_mean_RT) 


########################################################################
# Accuracy summary
# This relies on the work around to extract accuracies, mentioned above.
accuracy_data <- 
  data_df %>%
  filter(!is.na(rt)) %>% 
  group_by(participant) %>%
  summarize(IAT_accuracy = round(sum(accuracy[blocks == 3 | blocks == 4 | blocks == 6 | blocks == 7]) / 120 * 100, 2))  # 120 critical trials


########################################################################
# Extract demographics data
demographics_data <-
  data_df %>%
  select(participant,
         gender,
         age) %>%
  distinct(participant, .keep_all = TRUE)


########################################################################
# Join data frames
df_output <- 
  join_all(list(demographics_data,
                accuracy_data,
                D1_data,
                likert_data), 
           by = "participant", 
           type = "full")


########################################################################
# Write to file
df_output %>% write.csv(file = "/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Experiment 1/Analysis/dataset.csv", row.names=FALSE)

