###################################################################
# Analyse data from learning via CC experiment 1
###################################################################
# Author: Ian Hussey (ian.hussey@ugent.be)

# NB R treats the two conditions alphabetically, so that all effects
# sizes are retured as negative despite being in line with the hypotheses. 
# All are inverted when reported in the manuscript to make the reported 
# results congruent with the wording of the hypothesis.

###################################################################
# Clean the workspace
rm(list=ls())

###################################################################
## Dependencies
library(tidyverse)
library(psych)
library(effsize)
library(pwr)
library(car)  # for Anova()
library(lsr)  # for eta sq
library(MBESS)  # for ci.pvaf(), 95% CI on eta2
library(BayesFactor)


###################################################################
## Data acquisition
setwd("/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Analogical learning via IAT - OSF files/Experiment 1/Analyses/")

data_df <- read.csv("/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Analogical learning via IAT - OSF files/Experiment 1/Analyses/dataset.csv")  # acquire data


###################################################################
## descriptives

gender_counts <- data_df %>% count(gender)

descriptives_all_participants <- 
  data_df %>% 
  select(age,
         IAT_accuracy,
         IAT_mean_RT) %>%
  psych::describe(fast = TRUE,  # subset of descriptive stats
                  ranges = FALSE,
                  trim = 0)

descriptives_by_condition <- 
  data_df %>% 
  select(gender,
         age,
         ratings_pre,
         ratings_post,
         ratings_change_scores,
         D1) %>%
  psych::describeBy(data_df$condition,
                    fast = TRUE,  # subset of descriptive stats
                    ranges = FALSE,
                    trim = 0)

###################################################################
## Distribution plots - buyers vs non buyers for each scale
plot(density(data_df$ratings_change_scores[data_df$condition == "insects"]))
lines(density(data_df$ratings_change_scores[data_df$condition == "flowers"]))


###################################################################
## Neyman-Pearson frequentist tests

## hypothesis test - differences in ratings changes between conditions
# t test
ratings_independent_t_test <- 
  t.test(ratings_change_scores ~ condition, 
         data = data_df, alternative = "less")  
# effect size
ratings_d <- 
  cohen.d(ratings_change_scores ~ condition, 
          data = data_df)

# robustness test: ANCOVA with pre as covariate
model1 <- lm(ratings_post ~ ratings_pre + condition, 
             data = data_df)  # if anova() had been used below there would be ordering effects: must specify model as DV ~ covariate + IV
ratings_ANCOVA <- etaSquared(model1, 
                             type = 3, 
                             anova = TRUE)  # output full anova results, not just eta2

# 90% CI on ANCOVA's eta2 
# (nb 90% not 95%, see Wuensch, 2009; Steiger. 2004)
# from http://daniellakens.blogspot.be/2014/06/calculating-confidence-intervals-for.html
# generically: ci.pvaf(F.value=XX, df.1=XX, df.2=XX, N=XX, conf.level=.90)
# 1. extract individual stats
ancova_F        <-  round(ratings_ANCOVA[2,"F"], 2)         # where 2 specifies the main effect row
ancova_df_1     <-  round(ratings_ANCOVA[2,"df"], 2)        # where 2 specifies the main effect row
ancova_df_2     <-  round(ratings_ANCOVA[3,"df"], 2)        # where 3 specifies the residuals row
ancova_p        <-  round(ratings_ANCOVA[2,"p"], 5)         # where 2 specifies the main effect row
ancova_eta2     <-  round(ratings_ANCOVA[2,"eta.sq"], 2)    # where 2 specifies the main effect row
n_df <- data_df %>% dplyr::summarize(n_variable = n())
n_integer <- n_df$n_variable
# 2. 90% CIs
ancova_eta2_90pc_ci <- ci.pvaf(F.value = ancova_F, 
                               df.1 = ancova_df_1, 
                               df.2 = ancova_df_2, 
                               N = n_integer, 
                               conf.level=.90)

# alternative strategy: Bayes factors
ratings_bf_medium <- ttestBF(formula = ratings_change_scores ~ condition, 
                             rscale = "medium",  # i.e., r = .707
                             nullInterval = c(-Inf,0), # directional hypothesis
                             data = data_df)

ratings_bf_wide <- ttestBF(formula = ratings_change_scores ~ condition, 
                           rscale = "wide",  # i.e., r = 1.0
                           nullInterval = c(-Inf,0), # directional hypothesis
                           data = data_df)

## assumption test - differences in ratings of valenced stimuli
# t test
valenced_stimuli_ratings_independent_t_test <- 
  t.test(valenced_stimuli_ratings ~ condition, 
         data = data_df, alternative = "greater")

# effect size
valenced_stimuli_ratings_d <- 
  cohen.d(valenced_stimuli_ratings ~ condition, 
          data = data_df)

## assumption test - differences in (training) IAT effects betwen conditions
# t test
D1_independent_t_test <- 
  t.test(D1 ~ condition, 
         data = data_df, 
         alternative = "less")
# effect size
D1_d <- 
  cohen.d(D1 ~ condition, 
          data = data_df)


## write output to disk
sink("analyses.txt")
cat("###################     descriptives \n")
gender_counts
cat("\n")
descriptives_all_participants
cat("\n")
descriptives_by_condition
cat("\n")
cat("\n")
cat("###################     hypothesis test - change in ratings of chinese characters between conditions \n")
ratings_independent_t_test
cat("\n")
ratings_d
cat("\n")
cat("\n")
cat("###################     robustness test: alternative strategy ANCOVA post ~ pre + condition \n")
cat("\n")
ratings_ANCOVA
cat("\n")
cat("90% CI for eta2")
ancova_eta2_90pc_ci
cat("\n")
cat("\n")
cat("###################     alternative strategy: Bayes factors \n")
ratings_bf_medium
cat("\n")
ratings_bf_wide
cat("\n")
cat("\n")
cat("###################     assumptions test - difference in ratings of valenced images between conditions \n")
valenced_stimuli_ratings_independent_t_test
cat("\n")
valenced_stimuli_ratings_d
cat("\n")
cat("\n")
cat("###################     assumptions test - difference in training IAT D1 between conditions \n")
D1_independent_t_test
D1_d
sink()
