###################################################################
# Combination analysis of learning via CC experiments 1 and 2 
# NB Only rating scales are common to both studies
###################################################################
# Author: Ian Hussey (ian.hussey@ugent.be)

# NB R treats the two conditions alphabetically, so that all effects
# sizes are retured as negative despite being in line with the hypotheses. 
# All are inverted when reported in the manuscript to make the reported 
# results congruent with the wording of the hypothesis.

###################################################################
## Dependencies
library(tidyverse)
library(effsize)
library(pwr)
library(psych)
library(BayesFactor)

###################################################################
## Data acquisition and processing

setwd("/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Analogical learning via IAT - OSF files/Combination analysis/")

# experiment 1
exp1_df <- 
  read.csv("/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Analogical learning via IAT - OSF files/Experiment 1/Analyses/dataset.csv") %>%  # acquire data
  select(participant,
         condition,
         ratings_pre,
         ratings_post,
         ratings_change_scores) %>%  # select only necessary columns
  mutate(experiment = 1,
         unique_identifier = paste(experiment, participant, sep = "_"),
         ratings_pre_Z_scores = as.numeric(scale(ratings_pre,  # convert ratings to z scores
                                                    center = TRUE,  # i.e., deduct rows from mean
                                                    scale = TRUE)),
         ratings_post_Z_scores = as.numeric(scale(ratings_post,  # convert ratings to z scores
                                                    center = TRUE,  # i.e., deduct rows from mean
                                                    scale = TRUE)),
         ratings_change_Z_scores = as.numeric(scale(ratings_change_scores,  # convert ratings to z scores
                                                    center = TRUE,  # i.e., deduct rows from mean
                                                    scale = TRUE)))  # i.e., devide by SD

# experiment 2
exp2_df <- 
  read.csv("/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Analogical learning via IAT - OSF files/Experiment 2/Analyses/dataset.csv") %>%  # acquire data
  select(participant,
         condition,
         ratings_pre,
         ratings_post,
         ratings_change_scores) %>%  # select only necessary columns
  mutate(experiment = 2,
         unique_identifier = paste(experiment, participant, sep = "_"),
         ratings_pre_Z_scores = as.numeric(scale(ratings_pre,  # convert ratings to z scores
                                                 center = TRUE,  # i.e., deduct rows from mean
                                                 scale = TRUE)),
         ratings_post_Z_scores = as.numeric(scale(ratings_post,  # convert ratings to z scores
                                                  center = TRUE,  # i.e., deduct rows from mean
                                                  scale = TRUE)),
         ratings_change_Z_scores = as.numeric(scale(ratings_change_scores,  # convert ratings to z scores
                                                    center = TRUE,  # i.e., deduct rows from mean
                                                    scale = TRUE)))  # i.e., devide by SD


###################################################################
## combine frames

combined_df <- 
  full_join(exp1_df, exp2_df) %>%
  select(unique_identifier, 
         condition, 
         ratings_pre_Z_scores,
         ratings_post_Z_scores,
         ratings_change_Z_scores)


###################################################################
## Neyman-Pearson frequentist tests

## hypothesis test - differences in ratings changes between conditions
# t test
ratings_independent_t_test <- 
  t.test(ratings_change_Z_scores ~ condition, 
         data = combined_df, 
         alternative = "less")  
# effect size
ratings_d <- 
  cohen.d(ratings_change_Z_scores ~ condition, 
          data = combined_df)



# robustness test: ANCOVA with pre as covariate
model1 <- lm(ratings_post_Z_scores ~ ratings_pre_Z_scores + condition, 
             data = combined_df)  # if anova() had been used below there would be ordering effects: must specify model as DV ~ covariate + IV
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
n_df <- combined_df %>% dplyr::summarize(n_variable = n())
n_integer <- n_df$n_variable
# 2. 90% CIs
ancova_eta2_90pc_ci <- ci.pvaf(F.value = ancova_F, 
                               df.1 = ancova_df_1, 
                               df.2 = ancova_df_2, 
                               N = n_integer, 
                               conf.level=.90)



###################################################################
## Bayes factors 

# medium width prior
bf_medium <- ttestBF(formula = ratings_change_Z_scores ~ condition,
                     data = combined_df,
                     rscale = "medium",
                     paired = FALSE,
                     nullInterval = c(-Inf, 0))  # one sided

# wide prior
bf_wide <- ttestBF(formula = ratings_change_Z_scores ~ condition,
                   data = combined_df,
                   rscale = "wide",
                   paired = FALSE,
                   nullInterval = c(-Inf, 0))  # one sided


###################################################################
## write data to disk
sink("Combination analysis.txt")
cat("###################     all participants from both studies\n")
describe(combined_df)
cat("\n")
cat("\n")
cat("###################     flowers condition only\n")
filter(combined_df, condition == "flowers") %>% select(ratings_change_Z_scores) %>% describe()
cat("\n")
cat("\n")
cat("###################     insects condition only\n")
filter(combined_df, condition == "insects") %>% select(ratings_change_Z_scores) %>% describe()
cat("\n")
cat("\n")
cat("###################     frequentist test - change in ratings of chinese characters between conditions\n")
ratings_independent_t_test
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
cat("###################     bayes factors - change in ratings of chinese characters between conditions\n")
bf_medium
cat("\n")
bf_wide
sink()




