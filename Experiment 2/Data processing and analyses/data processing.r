########################################################################
# Data processing for learning via CC study experiment 2
########################################################################
# Author: Ian Hussey (ian.hussey@ugent.be)

########################################################################
# Dependencies
########################################################################
library(plyr) #must import before dplyr
library(dplyr)
library(tidyr)
library(readr)
library(data.table)

########################################################################
# Data acquisition and cleaning
########################################################################

# Set the working directory in which to look for data files, then read them in.
setwd("/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer - the IAT as an analogical learning task/Experiment 2/Data/Raw data/")
files <- list.files(pattern = "\\.csv$")
data_df <- tbl_df(rbind.fill(lapply(files, fread, header=TRUE)))

# Make some variable names more transparent, plus rectify the the accuracy variable
data_df <- 
  data_df %>%
  rename(likert_Pre_item = likertPre.thisTrialN,
         likert_Post_item = likertPost.thisTrialN,
         likert_Valence_item = likertValence.thisTrialN, # likert check of valenced items
         rating = rating.response,
         SCIAT1 = SCIAT1blocks.thisRepN, # RTs relevant to the SCIAT 1
         IAT = IATblocks.thisRepN, # RTs relevant to the IAT
         SCIAT2 = SCIAT2blocks.thisRepN, # RTs relevant to the SCIAT 2
         IAT_blocks = IATblocks.thisN, # current block
         SCIAT1_blocks = SCIAT1blocks.thisN, # current block 
         SCIAT2_blocks = SCIAT2blocks.thisN, # current block 
         IAT_trial = IATtrials.thisN, # trial order of presentation within each block
         rt = requiredResponse.rt, # first correct response rt
         accuracy = feedbackResponse.corr, # accuracy of the first response (currently reversed: 0 = correct)
         IATtrial = IATtrials.thisN, # trial by order of presentation within each block
         SCIAT1trial = SCIAT1trials.thisN, # trial by order of presentation within each block
         SCIAT2trial = SCIAT2trials.thisN, # trial by order of presentation within each block
         understands_chinese = recognition.response) %>% # Single item understanding of chinese characters, 0 or 1 
  mutate(accuracy = abs(accuracy - 1), # recitfies the direction of accuracy so that 0 = error and 1 = correct.
         IAT_blocks = IAT_blocks + 1, # recifies block to be 1 to 7 rather than 0-6
         SCIAT1_blocks = SCIAT1_blocks + 1, # recifies block to be 1 to 7 rather than 0-6
         SCIAT2_blocks = SCIAT2_blocks + 1, # recifies block to be 1 to 7 rather than 0-6
         SCIAT_IAT_block_order_congruency = ifelse(participant <= 48, 0, 1), #do the IAT and SCIAT block order match. *** nb this data is not explicitly included in the data file, but is how the sample was run.
         likert_Pre_item = likert_Pre_item + 1, # recitify 0-4 to 1-5,
         likert_Post_item = likert_Post_item + 1, # recitify 0-4 to 1-5
         likert_Valence_item = likert_Valence_item + 1, # recitify 0-9 to 1-10
         gender = ifelse(gender == "M", "m", # correct M to m
                         ifelse (gender == "FALSE", "f", gender))) # correct F (which R reads in as FALSE) to f

########################################################################
# Extract demographics data
demographics_data <-
  data_df %>%
  select(participant,
         gender,
         age,
         understands_chinese) %>%
  distinct(participant, .keep_all = TRUE)


########################################################################
# Likert data

# chinese ratings
Likert_chinese_data <-
  data_df %>%
  filter(!is.na(likert_Pre_item | likert_Post_item)) %>% 
  select(participant,
         rating,
         likert_Pre_item,
         likert_Post_item) %>%
  gather(likertTimepoint, 
         likertOrderOfPresentation, 
         c(likert_Pre_item, likert_Post_item), 
         na.rm = TRUE) %>%
  group_by(participant) %>%
  summarize(ratings_pre = round(mean(rating[likertTimepoint == "likert_Pre_item"]), 2),
            ratings_post = round(mean(rating[likertTimepoint == "likert_Post_item"]), 2))

# flowers/insects ratings
Likert_flowerInsects_data <-
  data_df %>%
  filter(!is.na(likert_Valence_item)) %>% 
  select(participant,
         rating,
         subscale,
         likert_Valence_item) %>%
  group_by(participant) %>%
  summarize(flowers_ratings = round(mean(rating[subscale == 2]), 2),
            insects_ratings = round(mean(rating[subscale == 3]), 2))


########################################################################
# IAT D1 scores
IAT_D1_df <-
  data_df %>%
  filter(IAT == 0) %>% # select only rows that corrispond to the IAT data
  group_by(participant) %>%
  filter(rt <= 10000) %>%
  summarize(IAT_mean_RT = round(mean(rt[IAT_blocks == 3 | IAT_blocks == 4 | IAT_blocks == 6 | IAT_blocks == 7])*1000, 0), 
            RT_block3_m = mean(rt[IAT_blocks == 3]),  # blocks 3 and 6
            RT_block6_m = mean(rt[IAT_blocks == 6]),
            RT_block3and6_SD = sd(rt[IAT_blocks == 3 | IAT_blocks == 6]),
            RT_block4_m = mean(rt[IAT_blocks == 4]),  # blocks 4 and 7
            RT_block7_m = mean(rt[IAT_blocks == 7]),
            RT_block4and7_SD = sd(rt[IAT_blocks == 4 | IAT_blocks == 7])) %>%
  mutate(differenceA = RT_block6_m - RT_block3_m,
         IAT_D1a = differenceA / RT_block3and6_SD,
         differenceB = RT_block7_m - RT_block4_m,
         IAT_D1b = differenceB / RT_block4and7_SD,
         IAT_D1 = round((IAT_D1a + IAT_D1b)/2, 2)) %>%
  select(participant, 
         IAT_mean_RT,
         IAT_D1)


########################################################################
# SCIAT 1 data
SCIAT1_D1_df <-
  data_df %>%
  filter(SCIAT1 == 0) %>% # select only rows that corrispond to the SCIAT1 data
  group_by(participant) %>%
  filter(rt <= 10000) %>%
  summarize(SCIAT1_mean_RT = round(mean(rt[SCIAT1_blocks == 2 | SCIAT1_blocks == 3])*1000, 0), 
            RT_block2_m = mean(rt[SCIAT1_blocks == 2]), 
            RT_block3_m = mean(rt[SCIAT1_blocks == 3]),
            RT_block2and3_SD = sd(rt[SCIAT1_blocks == 2 | SCIAT1_blocks == 3])) %>%
  mutate(difference = RT_block3_m - RT_block2_m,
         SCIAT1_D1 = round(difference / RT_block2and3_SD, 2)) %>%
  select(participant, 
         SCIAT1_mean_RT,
         SCIAT1_D1)


########################################################################
# SCIAT 2 data
SCIAT2_D1_df <-
  data_df %>%
  filter(SCIAT2 == 0) %>% # select only rows that corrispond to the SCIAT2 data
  group_by(participant) %>%
  filter(rt <= 10000) %>%
  summarize(SCIAT2_mean_RT = round(mean(rt[SCIAT2_blocks == 2 | SCIAT2_blocks == 3])*1000, 0), 
            RT_block2_m = mean(rt[SCIAT2_blocks == 2]), 
            RT_block3_m = mean(rt[SCIAT2_blocks == 3]),
            RT_block2and3_SD = sd(rt[SCIAT2_blocks == 2 | SCIAT2_blocks == 3])) %>%
  mutate(difference = RT_block3_m - RT_block2_m,
         SCIAT2_D1 = round(difference / RT_block2and3_SD, 2)) %>%  
  select(participant, 
         SCIAT2_mean_RT,
         SCIAT2_D1)


########################################################################
# conditions data

# IAT condition & contrast category condition
IAT_condition_df <-
  data_df %>%
  filter(IAT == 0) %>% # select only rows that corrispond to the IAT data
  group_by(participant) %>%
  distinct(condition) %>%
  rename(IAT_condition = condition) %>%
  select(participant, 
         IAT_condition) %>%
  mutate(valence_of_IAT_contrast_category = ifelse(IAT_condition == 1 | IAT_condition == 2,
                                                   "flowers", 
                                                   ifelse(IAT_condition == 3 | IAT_condition == 4,
                                                          "insects")),
         block_order = ifelse(IAT_condition == 1 | IAT_condition == 4, 
                              "consistent_first", 
                              ifelse(
                                IAT_condition == 2 | IAT_condition == 3, 
                                "inconsistent_first", 
                                "error")))
                                                   

# SC-IAT condition
SCIAT_condition_df <-
  data_df %>%
  filter(SCIAT1 == 0) %>% # select only rows that corrispond to the SCIAT data
  group_by(participant) %>%
  distinct(condition) %>%
  rename(SCIAT_condition = condition) %>%
  select(participant, 
         SCIAT_condition)


########################################################################
# Accuracy summaries

IAT_accuracy_data <- 
  data_df %>%
  filter(IAT == 0) %>% 
  group_by(participant) %>%
  summarize(IAT_accuracy = round(sum(accuracy[IAT_blocks == 3 |
                                                IAT_blocks == 4 | 
                                                IAT_blocks == 6 | 
                                                IAT_blocks == 7]) / 120 *100, 2)) # 120 critical trials in the IAT

SCIAT1_accuracy_data <- 
  data_df %>%
  filter(SCIAT1 == 0) %>% 
  group_by(participant) %>%
  summarize(SCIAT1_accuracy = round(sum(accuracy[SCIAT1_blocks == 2 | 
                                                   SCIAT1_blocks == 3]) / 140 *100, 2)) # 140 critical trials in this SCIAT

SCIAT2_accuracy_data <- 
  data_df %>%
  filter(SCIAT2 == 0) %>% 
  group_by(participant) %>%
  summarize(SCIAT2_accuracy = round(sum(accuracy[SCIAT2_blocks == 2 |
                                                   SCIAT2_blocks == 3]) / 140 *100, 2)) # 140 critical trials in this SCIAT


########################################################################
# Join data frames

all_tasks_df <- 
  join_all(list(demographics_data,
                Likert_chinese_data, 
                Likert_flowerInsects_data,
                IAT_condition_df,
                SCIAT_condition_df,
                IAT_D1_df,
                SCIAT1_D1_df,
                SCIAT2_D1_df,
                IAT_accuracy_data,
                SCIAT1_accuracy_data,
                SCIAT2_accuracy_data),
           by = "participant",
           type = "full")


########################################################################
# Final manipulations

## D1 score inversions
# invert any task that begins with a chinese-negative block so that all D1 scores refer to chinese-positive effects
output_df <- 
  all_tasks_df %>%
  mutate(IAT_D1 = ifelse(IAT_condition == 1 | IAT_condition == 3, IAT_D1 *-1, IAT_D1),
         SCIAT1_D1 = ifelse(SCIAT_condition == 2, SCIAT1_D1 *-1, SCIAT1_D1),
         SCIAT2_D1 = ifelse(SCIAT_condition == 2, SCIAT2_D1 *-1, SCIAT2_D1))

## Difference scores
output_df <-
  output_df %>%
  mutate(ratings_change_scores = ratings_post - ratings_pre,
         SCIAT_D1_change_scores= SCIAT2_D1 - SCIAT1_D1)

## drop unnecessary variables & tidy names
output_df <- 
  output_df %>%
  select(participant,
         valence_of_IAT_contrast_category,  # condition
         block_order,
         ratings_pre,
         ratings_post,
         ratings_change_scores,
         SCIAT1_D1,
         SCIAT2_D1,
         SCIAT_D1_change_scores,
         gender,
         age,
         understands_chinese,
         flowers_ratings,
         insects_ratings,
         IAT_mean_RT,
         IAT_D1,
         SCIAT1_mean_RT,
         SCIAT2_mean_RT,
         IAT_accuracy,
         SCIAT1_accuracy,
         SCIAT2_accuracy) %>%
  rename(condition = valence_of_IAT_contrast_category)

########################################################################
# Write to file
output_df %>% write.csv(file = "/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer - the IAT as an analogical learning task/Experiment 2/Data/processed data.csv", row.names=FALSE)
