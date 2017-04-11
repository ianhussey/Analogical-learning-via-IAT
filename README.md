# The IAT as an analogical learning task

## License
Copyright (c) Ian Hussey 2015 (ian.hussey@ugent.be), released under the GPLv3+ open source license. 

## Description & purpose
Measures, processing scripts, and analysis scripts for two experiments on the IAT as an analogical learning task. Project on Open Science Framework with the design, data, and analysis can be found [here](https://osf.io/t89fu).

- Measures written in PsychoPy (v1.82)
- Processing scripts and analyses scripts written in R (v3.3)

IAT code origianlly from my repository [here](https://github.com/ianhussey/ImplicitAssociationTest).

SC-IAT code origianlly from my repository [here](https://github.com/ianhussey/SingleCategoryImplicitAssociationTest).

### Experiment 1
- Ratings scales, IAT (employed as training task), ratings scales. 
- Automatic counterbalancing of condition and IAT block order based on participant code

### Experiment 2
- Recognition test, SC-IAT, Ratings scales, IAT (employed as training task), Ratings scales, SC-IAT, ratings scales. 
- Automatic counterbalancing of condition, IAT block order and SC-IAT block order based on participant code. The congruency between SC-IAT and IAT block order is set manually via exchanging out the excel stimuli files. See the incongruent condition folder for details. This was changed exactly half way through data collection when the possible confound was spotted. 

## Code usage

Run in order:

1. `Data screening.r`
   1. Compares the number of trials on each task to the modal number for the sample and creates two lists of participants, those with complete vs incomplete data. Participants can be paid/rejected on prolific.ac appropriately.
2. `Data processing`
   1. Processes data into analysable format.
3. `Analysis.rmd`
   1. Applies exclusion criteria. If sample doesn't meet stopping rule, increase N on prolific.ac and iteratively rerun these scripts on the new, complete data. When sample has been reached, interpret analyses.
4. `Remove prolific codes.r`
   1. Once final sample has been completed, remove participants' prolific codes from data using this script. Ensure that the original demographics.csv file is either overwritten or deleted. This anonymised data can then be put online.

## Requirements

- [PsychoPy - v1.82](https://github.com/psychopy/psychopy/releases/tag/r1.82.02)
  - A free and open source program for delivering psychology experiments written in Python. See [here for documentation](http://www.psychopy.org/documentation.html).
  - PsychoPy runs locally on Windows, Mac, and Linux. It's not possible to run PsychoPy scripts online.
  - You might be able to use more recent versions, but will probably need to run the `.py` files rather than the `.psyexp` file.

- [R - v3.3.1](https://www.r-project.org/) or later
  - The included data processing script is written in R and [RStudio](https://www.rstudio.com/). Various depencies are listed at the top of each R script.
