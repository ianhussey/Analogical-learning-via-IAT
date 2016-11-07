###################################################################
# Plot data from learning via IAT contrast category exps 1 and 2
###################################################################
# Author: Ian Hussey (ian.hussey@ugent.be)

###################################################################
# Clean the workspace
rm(list=ls())

###################################################################
## Dependencies
library(tidyverse)
library(yarrr)

###################################################################
## Data acquisition
setwd("/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Analogical learning via IAT - OSF files/Manuscript")

exp1_df <- 
  read.csv("/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Analogical learning via IAT - OSF files/Experiment 1/Analyses/dataset.csv") %>%
  mutate(`Experiment 1` = ifelse(condition == "flowers", "Flowers", "Insects"))

exp2_df <- 
  read.csv("/Users/Ian/Dropbox/Work/Manuscripts/Hussey & De Houwer, Learning via IAT CC/Analogical learning via IAT - OSF files/Experiment 2/Analyses/dataset.csv") %>%
  mutate(`Experiment 2` = ifelse(condition == "flowers", "Flowers", "Insects"))


###################################################################
## Plotting

# create a 1x3 grid of plots
par(mfrow=c(1,3))

RDI_plot_exp1_ratings <- 
  pirateplot(formula = ratings_change_scores ~ `Experiment 1`,
             data = exp1_df,
             ylab = "Ratings",
             theme.o = 1,
             pal = "526273",
             bean.o = 1,
             point.o = .4,
             bar.o = 0,
             line.o = 1,
             inf.o = .5,
             inf = "ci",
             jitter.val = 0.05)  # confidence intervals

RDI_plot_exp2_ratings <- 
  pirateplot(formula = ratings_change_scores ~ `Experiment 2`,
             data = exp2_df,
             ylab = "Ratings",
             theme.o = 1,
             pal = "526273",
             bean.o = 1,
             point.o = .4,
             bar.o = 0,
             line.o = 1,
             inf.o = .5,
             inf = "ci",
             jitter.val = 0.05)  # confidence intervals

RDI_plot_exp2_SCIATs <- 
  pirateplot(formula = SCIAT_D1_change_scores ~ `Experiment 2`,
             data = exp2_df,
             ylab = substitute(paste("SC-IAT ", italic("D"), "1")),
             theme.o = 1,
             pal = "526273",
             bean.o = 1,
             point.o = .4,
             bar.o = 0,
             line.o = 1,
             inf.o = .5,
             inf = "ci",
             jitter.val = 0.05)  # confidence intervals
