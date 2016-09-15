# The IAT as an analogical learning task

## License
Copyright (c) Ian Hussey 2015 (ian.hussey@ugent.be)

Released under the GPLv3+ open source license. 

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## Version
1.0

Data collection and analysis complete - no issues found.

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

## Requirements
- [PsychoPy - v1.82](https://github.com/psychopy/psychopy/releases/tag/r1.82.02)
	- A free and open source program for delivering psychology experiments written in Python. See [here for documentation](http://www.psychopy.org/documentation.html).
	- PsychoPy runs locally on Windows, Mac, and Linux. It's not possible to run PsychoPy scripts online.
	- You might be able to use more recent versions, but will probably need to run the `.py` files rather than the `.psyexp` file.
	
- [R - v3.3.1](https://www.r-project.org/) or later
	- The included data processing script is written in R and [RStudio](https://www.rstudio.com/). Various depencies are listed at the top of each R script.
