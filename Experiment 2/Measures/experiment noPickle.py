#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Tue Feb 23 16:31:23 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'SCIAT IAT and likerts'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s' %(expInfo['participant'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "recognitionScales"
recognitionScalesClock = core.Clock()
recognition = visual.RatingScale(win=win, name='recognition', marker='circle', size=1.0, pos=[0.0, -0.4], low=0, high=1, labels=['Nee', ' Ja'], scale='')
instructionBox_2 = visual.TextStim(win=win, ori=0, name='instructionBox_2',
    text='Kent u de betekenis van een of meer van deze Chinese symbolen?',    font='Arial',
    pos=[0, 0.75], height=0.1, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
allChineseCharactersImage = visual.ImageStim(win=win, name='allChineseCharactersImage',
    image='allChineseCharacters.png', mask=None,
    ori=0, pos=[0, 0], size=[1.3, .4],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
target1box_inst = visual.TextStim(win=win, ori=0, name='target1box_inst',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0)
target2box_inst = visual.TextStim(win=win, ori=0, name='target2box_inst',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-3.0)
attribute1box_inst = visual.TextStim(win=win, ori=0, name='attribute1box_inst',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0)
attribute2box_inst = visual.TextStim(win=win, ori=0, name='attribute2box_inst',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-5.0)
orLeftBox_inst = visual.TextStim(win=win, ori=0, name='orLeftBox_inst',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
orRightBox_inst = visual.TextStim(win=win, ori=0, name='orRightBox_inst',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimulusImage = visual.ImageStim(win=win, name='stimulusImage',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=.4,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
stimulusBox = visual.TextStim(win=win, ori=0, name='stimulusBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0)
msg1=""

# dertermine the condition based on the modulo of the participant code 
# i.e., if the remained of the participant code divided by 4 = 1, run condition 1, etc.
participant = int(expInfo['participant'])
if (participant % 4) == 1: 
    SCIATtaskFile = "blocks_SCIAT_Afirst.xlsx"
    IATtaskFile = "blocks_IAT_flowers_Afirst.xlsx"
elif (participant % 4) == 2:
    SCIATtaskFile = "blocks_SCIAT_Bfirst.xlsx"
    IATtaskFile = "blocks_IAT_flowers_Bfirst.xlsx"
elif (participant % 4) == 3:
    SCIATtaskFile = "blocks_SCIAT_Afirst.xlsx"
    IATtaskFile = "blocks_IAT_insects_Afirst.xlsx"
elif (participant % 4) == 0:
    SCIATtaskFile = "blocks_SCIAT_Bfirst.xlsx"
    IATtaskFile = "blocks_IAT_insects_Bfirst.xlsx"
else:
    print "****condition file error****"
accuracyFeedback = visual.TextStim(win=win, ori=0, name='accuracyFeedback',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-5.0)
target1box = visual.TextStim(win=win, ori=0, name='target1box',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
target2box = visual.TextStim(win=win, ori=0, name='target2box',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-7.0)
attribute1box = visual.TextStim(win=win, ori=0, name='attribute1box',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-8.0)
attribute2box = visual.TextStim(win=win, ori=0, name='attribute2box',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-9.0)
orLeftBox = visual.TextStim(win=win, ori=0, name='orLeftBox',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-10.0)
orRightBox = visual.TextStim(win=win, ori=0, name='orRightBox',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-11.0)

# Initialize components for Routine "likertScales"
likertScalesClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker='circle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=['helemaal niet aangenaam', ' heel aangenaam'], scale='')
instructionBox = visual.TextStim(win=win, ori=0, name='instructionBox',
    text='default text',    font='Arial',
    pos=[0, 0.75], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=.4,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
target1box_inst = visual.TextStim(win=win, ori=0, name='target1box_inst',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0)
target2box_inst = visual.TextStim(win=win, ori=0, name='target2box_inst',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-3.0)
attribute1box_inst = visual.TextStim(win=win, ori=0, name='attribute1box_inst',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0)
attribute2box_inst = visual.TextStim(win=win, ori=0, name='attribute2box_inst',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-5.0)
orLeftBox_inst = visual.TextStim(win=win, ori=0, name='orLeftBox_inst',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
orRightBox_inst = visual.TextStim(win=win, ori=0, name='orRightBox_inst',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimulusImage = visual.ImageStim(win=win, name='stimulusImage',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=.4,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
stimulusBox = visual.TextStim(win=win, ori=0, name='stimulusBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0)
msg1=""

# dertermine the condition based on the modulo of the participant code 
# i.e., if the remained of the participant code divided by 4 = 1, run condition 1, etc.
participant = int(expInfo['participant'])
if (participant % 4) == 1: 
    SCIATtaskFile = "blocks_SCIAT_Afirst.xlsx"
    IATtaskFile = "blocks_IAT_flowers_Afirst.xlsx"
elif (participant % 4) == 2:
    SCIATtaskFile = "blocks_SCIAT_Bfirst.xlsx"
    IATtaskFile = "blocks_IAT_flowers_Bfirst.xlsx"
elif (participant % 4) == 3:
    SCIATtaskFile = "blocks_SCIAT_Afirst.xlsx"
    IATtaskFile = "blocks_IAT_insects_Afirst.xlsx"
elif (participant % 4) == 0:
    SCIATtaskFile = "blocks_SCIAT_Bfirst.xlsx"
    IATtaskFile = "blocks_IAT_insects_Bfirst.xlsx"
else:
    print "****condition file error****"
accuracyFeedback = visual.TextStim(win=win, ori=0, name='accuracyFeedback',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-5.0)
target1box = visual.TextStim(win=win, ori=0, name='target1box',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
target2box = visual.TextStim(win=win, ori=0, name='target2box',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-7.0)
attribute1box = visual.TextStim(win=win, ori=0, name='attribute1box',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-8.0)
attribute2box = visual.TextStim(win=win, ori=0, name='attribute2box',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-9.0)
orLeftBox = visual.TextStim(win=win, ori=0, name='orLeftBox',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-10.0)
orRightBox = visual.TextStim(win=win, ori=0, name='orRightBox',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-11.0)

# Initialize components for Routine "likertScales"
likertScalesClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker='circle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=['helemaal niet aangenaam', ' heel aangenaam'], scale='')
instructionBox = visual.TextStim(win=win, ori=0, name='instructionBox',
    text='default text',    font='Arial',
    pos=[0, 0.75], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=.4,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
target1box_inst = visual.TextStim(win=win, ori=0, name='target1box_inst',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0)
target2box_inst = visual.TextStim(win=win, ori=0, name='target2box_inst',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-3.0)
attribute1box_inst = visual.TextStim(win=win, ori=0, name='attribute1box_inst',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0)
attribute2box_inst = visual.TextStim(win=win, ori=0, name='attribute2box_inst',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-5.0)
orLeftBox_inst = visual.TextStim(win=win, ori=0, name='orLeftBox_inst',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
orRightBox_inst = visual.TextStim(win=win, ori=0, name='orRightBox_inst',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimulusImage = visual.ImageStim(win=win, name='stimulusImage',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=.4,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
stimulusBox = visual.TextStim(win=win, ori=0, name='stimulusBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0)
msg1=""

# dertermine the condition based on the modulo of the participant code 
# i.e., if the remained of the participant code divided by 4 = 1, run condition 1, etc.
participant = int(expInfo['participant'])
if (participant % 4) == 1: 
    SCIATtaskFile = "blocks_SCIAT_Afirst.xlsx"
    IATtaskFile = "blocks_IAT_flowers_Afirst.xlsx"
elif (participant % 4) == 2:
    SCIATtaskFile = "blocks_SCIAT_Bfirst.xlsx"
    IATtaskFile = "blocks_IAT_flowers_Bfirst.xlsx"
elif (participant % 4) == 3:
    SCIATtaskFile = "blocks_SCIAT_Afirst.xlsx"
    IATtaskFile = "blocks_IAT_insects_Afirst.xlsx"
elif (participant % 4) == 0:
    SCIATtaskFile = "blocks_SCIAT_Bfirst.xlsx"
    IATtaskFile = "blocks_IAT_insects_Bfirst.xlsx"
else:
    print "****condition file error****"
accuracyFeedback = visual.TextStim(win=win, ori=0, name='accuracyFeedback',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-5.0)
target1box = visual.TextStim(win=win, ori=0, name='target1box',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
target2box = visual.TextStim(win=win, ori=0, name='target2box',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-7.0)
attribute1box = visual.TextStim(win=win, ori=0, name='attribute1box',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-8.0)
attribute2box = visual.TextStim(win=win, ori=0, name='attribute2box',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-9.0)
orLeftBox = visual.TextStim(win=win, ori=0, name='orLeftBox',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-10.0)
orRightBox = visual.TextStim(win=win, ori=0, name='orRightBox',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-11.0)

# Initialize components for Routine "likertScales"
likertScalesClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker='circle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=['helemaal niet aangenaam', ' heel aangenaam'], scale='')
instructionBox = visual.TextStim(win=win, ori=0, name='instructionBox',
    text='default text',    font='Arial',
    pos=[0, 0.75], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=.4,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'End of experiment',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "recognitionScales"-------
t = 0
recognitionScalesClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
recognition.reset()
# keep track of which components have finished
recognitionScalesComponents = []
recognitionScalesComponents.append(recognition)
recognitionScalesComponents.append(instructionBox_2)
recognitionScalesComponents.append(allChineseCharactersImage)
for thisComponent in recognitionScalesComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "recognitionScales"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = recognitionScalesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *recognition* updates
    if t >= 0.5 and recognition.status == NOT_STARTED:
        # keep track of start time/frame for later
        recognition.tStart = t  # underestimates by a little under one frame
        recognition.frameNStart = frameN  # exact frame index
        recognition.setAutoDraw(True)
    continueRoutine &= recognition.noResponse  # a response ends the trial
    
    # *instructionBox_2* updates
    if t >= 0.5 and instructionBox_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionBox_2.tStart = t  # underestimates by a little under one frame
        instructionBox_2.frameNStart = frameN  # exact frame index
        instructionBox_2.setAutoDraw(True)
    
    # *allChineseCharactersImage* updates
    if t >= 0.5 and allChineseCharactersImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        allChineseCharactersImage.tStart = t  # underestimates by a little under one frame
        allChineseCharactersImage.frameNStart = frameN  # exact frame index
        allChineseCharactersImage.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in recognitionScalesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "recognitionScales"-------
for thisComponent in recognitionScalesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('recognition.response', recognition.getRating())
thisExp.nextEntry()
# the Routine "recognitionScales" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SCIAT1blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(SCIATtaskFile),
    seed=None, name='SCIAT1blocks')
thisExp.addLoop(SCIAT1blocks)  # add the loop to the experiment
thisSCIAT1block = SCIAT1blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisSCIAT1block.rgb)
if thisSCIAT1block != None:
    for paramName in thisSCIAT1block.keys():
        exec(paramName + '= thisSCIAT1block.' + paramName)

for thisSCIAT1block in SCIAT1blocks:
    currentLoop = SCIAT1blocks
    # abbreviate parameter names if possible (e.g. rgb = thisSCIAT1block.rgb)
    if thisSCIAT1block != None:
        for paramName in thisSCIAT1block.keys():
            exec(paramName + '= thisSCIAT1block.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setColor(colourA, colorSpace='rgb')
    instructionsBox.setText(instruction)
    responseContinue = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue.status = NOT_STARTED
    target1box_inst.setColor(colourA, colorSpace='rgb')
    target1box_inst.setText(target1)
    target2box_inst.setColor(colourA, colorSpace='rgb')
    target2box_inst.setText(target2)
    attribute1box_inst.setColor(colourB, colorSpace='rgb')
    attribute1box_inst.setText(attribute1)
    attribute2box_inst.setColor(colourB, colorSpace='rgb')
    attribute2box_inst.setText(attribute2)
    orLeftBox_inst.setColor(colourA, colorSpace='rgb')
    orLeftBox_inst.setText(orStimulusLeft)
    orRightBox_inst.setColor(colourA, colorSpace='rgb')
    orRightBox_inst.setText(orStimulusRight)
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(responseContinue)
    instructionsComponents.append(target1box_inst)
    instructionsComponents.append(target2box_inst)
    instructionsComponents.append(attribute1box_inst)
    instructionsComponents.append(attribute2box_inst)
    instructionsComponents.append(orLeftBox_inst)
    instructionsComponents.append(orRightBox_inst)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 1 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *responseContinue* updates
        if t >= 1.5 and responseContinue.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue.tStart = t  # underestimates by a little under one frame
            responseContinue.frameNStart = frameN  # exact frame index
            responseContinue.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if responseContinue.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *target1box_inst* updates
        if t >= 1 and target1box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box_inst.tStart = t  # underestimates by a little under one frame
            target1box_inst.frameNStart = frameN  # exact frame index
            target1box_inst.setAutoDraw(True)
        
        # *target2box_inst* updates
        if t >= 1 and target2box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box_inst.tStart = t  # underestimates by a little under one frame
            target2box_inst.frameNStart = frameN  # exact frame index
            target2box_inst.setAutoDraw(True)
        
        # *attribute1box_inst* updates
        if t >= 1 and attribute1box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box_inst.tStart = t  # underestimates by a little under one frame
            attribute1box_inst.frameNStart = frameN  # exact frame index
            attribute1box_inst.setAutoDraw(True)
        
        # *attribute2box_inst* updates
        if t >= 1 and attribute2box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box_inst.tStart = t  # underestimates by a little under one frame
            attribute2box_inst.frameNStart = frameN  # exact frame index
            attribute2box_inst.setAutoDraw(True)
        
        # *orLeftBox_inst* updates
        if t >= 1 and orLeftBox_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox_inst.tStart = t  # underestimates by a little under one frame
            orLeftBox_inst.frameNStart = frameN  # exact frame index
            orLeftBox_inst.setAutoDraw(True)
        
        # *orRightBox_inst* updates
        if t >= 1 and orRightBox_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox_inst.tStart = t  # underestimates by a little under one frame
            orRightBox_inst.frameNStart = frameN  # exact frame index
            orRightBox_inst.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    SCIAT1trials = data.TrialHandler(nReps=nBlockRepeats, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(block),
        seed=None, name='SCIAT1trials')
    thisExp.addLoop(SCIAT1trials)  # add the loop to the experiment
    thisSCIAT1trial = SCIAT1trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisSCIAT1trial.rgb)
    if thisSCIAT1trial != None:
        for paramName in thisSCIAT1trial.keys():
            exec(paramName + '= thisSCIAT1trial.' + paramName)
    
    for thisSCIAT1trial in SCIAT1trials:
        currentLoop = SCIAT1trials
        # abbreviate parameter names if possible (e.g. rgb = thisSCIAT1trial.rgb)
        if thisSCIAT1trial != None:
            for paramName in thisSCIAT1trial.keys():
                exec(paramName + '= thisSCIAT1trial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        stimulusImage.setImage(imageStimulus)
        stimulusBox.setColor(stimulusColour, colorSpace='rgb')
        stimulusBox.setText(stimulus)
        requiredResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        requiredResponse.status = NOT_STARTED
        feedbackResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        feedbackResponse.status = NOT_STARTED
        
        target1box.setColor(colourA, colorSpace='rgb')
        target1box.setText(target1)
        target2box.setColor(colourA, colorSpace='rgb')
        target2box.setText(target2)
        attribute1box.setColor(colourB, colorSpace='rgb')
        attribute1box.setText(attribute1
)
        attribute2box.setColor(colourB, colorSpace='rgb')
        attribute2box.setText(attribute2)
        orLeftBox.setColor(colourA, colorSpace='rgb')
        orLeftBox.setText(orStimulusLeft)
        orRightBox.setColor(colourA, colorSpace='rgb')
        orRightBox.setText(orStimulusRight)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(stimulusImage)
        trialComponents.append(stimulusBox)
        trialComponents.append(requiredResponse)
        trialComponents.append(feedbackResponse)
        trialComponents.append(accuracyFeedback)
        trialComponents.append(target1box)
        trialComponents.append(target2box)
        trialComponents.append(attribute1box)
        trialComponents.append(attribute2box)
        trialComponents.append(orLeftBox)
        trialComponents.append(orRightBox)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulusImage* updates
            if t >= 0.3 and stimulusImage.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusImage.tStart = t  # underestimates by a little under one frame
                stimulusImage.frameNStart = frameN  # exact frame index
                stimulusImage.setAutoDraw(True)
            
            # *stimulusBox* updates
            if t >= 0.3 and stimulusBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusBox.tStart = t  # underestimates by a little under one frame
                stimulusBox.frameNStart = frameN  # exact frame index
                stimulusBox.setAutoDraw(True)
            
            # *requiredResponse* updates
            if t >= 0.3 and requiredResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                requiredResponse.tStart = t  # underestimates by a little under one frame
                requiredResponse.frameNStart = frameN  # exact frame index
                requiredResponse.status = STARTED
                # AllowedKeys looks like a variable named `requiredAllowed`
                if not 'requiredAllowed' in locals():
                    logging.error('AllowedKeys variable `requiredAllowed` is not defined.')
                    core.quit()
                if not type(requiredAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(requiredAllowed, basestring):
                        logging.error('AllowedKeys variable `requiredAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in requiredAllowed: requiredAllowed = (requiredAllowed,)
                    else:  requiredAllowed = eval(requiredAllowed)
                # keyboard checking is just starting
                requiredResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if requiredResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(requiredAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if requiredResponse.keys == []:  # then this was the first keypress
                        requiredResponse.keys = theseKeys[0]  # just the first key pressed
                        requiredResponse.rt = requiredResponse.clock.getTime()
                        # was this 'correct'?
                        if (requiredResponse.keys == str(requiredKey)) or (requiredResponse.keys == requiredKey):
                            requiredResponse.corr = 1
                        else:
                            requiredResponse.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *feedbackResponse* updates
            if t >= 0.3 and feedbackResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackResponse.tStart = t  # underestimates by a little under one frame
                feedbackResponse.frameNStart = frameN  # exact frame index
                feedbackResponse.status = STARTED
                # AllowedKeys looks like a variable named `feedbackAllowed`
                if not 'feedbackAllowed' in locals():
                    logging.error('AllowedKeys variable `feedbackAllowed` is not defined.')
                    core.quit()
                if not type(feedbackAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(feedbackAllowed, basestring):
                        logging.error('AllowedKeys variable `feedbackAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in feedbackAllowed: feedbackAllowed = (feedbackAllowed,)
                    else:  feedbackAllowed = eval(feedbackAllowed)
                # keyboard checking is just starting
                feedbackResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if feedbackResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(feedbackAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if feedbackResponse.keys == []:  # then this was the first keypress
                        feedbackResponse.keys = theseKeys[0]  # just the first key pressed
                        feedbackResponse.rt = feedbackResponse.clock.getTime()
                        # was this 'correct'?
                        if (feedbackResponse.keys == str(feedbackKey)) or (feedbackResponse.keys == feedbackKey):
                            feedbackResponse.corr = 1
                        else:
                            feedbackResponse.corr = 0
            if len(feedbackResponse.keys)<1:
                msg1=""
            else:
                msg1="X"
            
            # *accuracyFeedback* updates
            if t >= 0.3 and accuracyFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyFeedback.tStart = t  # underestimates by a little under one frame
                accuracyFeedback.frameNStart = frameN  # exact frame index
                accuracyFeedback.setAutoDraw(True)
            if accuracyFeedback.status == STARTED:  # only update if being drawn
                accuracyFeedback.setText(msg1, log=False)
            
            # *target1box* updates
            if t >= 0.0 and target1box.status == NOT_STARTED:
                # keep track of start time/frame for later
                target1box.tStart = t  # underestimates by a little under one frame
                target1box.frameNStart = frameN  # exact frame index
                target1box.setAutoDraw(True)
            
            # *target2box* updates
            if t >= 0.0 and target2box.status == NOT_STARTED:
                # keep track of start time/frame for later
                target2box.tStart = t  # underestimates by a little under one frame
                target2box.frameNStart = frameN  # exact frame index
                target2box.setAutoDraw(True)
            
            # *attribute1box* updates
            if t >= 0.0 and attribute1box.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute1box.tStart = t  # underestimates by a little under one frame
                attribute1box.frameNStart = frameN  # exact frame index
                attribute1box.setAutoDraw(True)
            
            # *attribute2box* updates
            if t >= 0.0 and attribute2box.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute2box.tStart = t  # underestimates by a little under one frame
                attribute2box.frameNStart = frameN  # exact frame index
                attribute2box.setAutoDraw(True)
            
            # *orLeftBox* updates
            if t >= 0.0 and orLeftBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                orLeftBox.tStart = t  # underestimates by a little under one frame
                orLeftBox.frameNStart = frameN  # exact frame index
                orLeftBox.setAutoDraw(True)
            
            # *orRightBox* updates
            if t >= 0.0 and orRightBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                orRightBox.tStart = t  # underestimates by a little under one frame
                orRightBox.frameNStart = frameN  # exact frame index
                orRightBox.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if requiredResponse.keys in ['', [], None]:  # No response was made
           requiredResponse.keys=None
           # was no response the correct answer?!
           if str(requiredKey).lower() == 'none': requiredResponse.corr = 1  # correct non-response
           else: requiredResponse.corr = 0  # failed to respond (incorrectly)
        # store data for SCIAT1trials (TrialHandler)
        SCIAT1trials.addData('requiredResponse.keys',requiredResponse.keys)
        SCIAT1trials.addData('requiredResponse.corr', requiredResponse.corr)
        if requiredResponse.keys != None:  # we had a response
            SCIAT1trials.addData('requiredResponse.rt', requiredResponse.rt)
        # check responses
        if feedbackResponse.keys in ['', [], None]:  # No response was made
           feedbackResponse.keys=None
           # was no response the correct answer?!
           if str(feedbackKey).lower() == 'none': feedbackResponse.corr = 1  # correct non-response
           else: feedbackResponse.corr = 0  # failed to respond (incorrectly)
        # store data for SCIAT1trials (TrialHandler)
        SCIAT1trials.addData('feedbackResponse.keys',feedbackResponse.keys)
        SCIAT1trials.addData('feedbackResponse.corr', feedbackResponse.corr)
        if feedbackResponse.keys != None:  # we had a response
            SCIAT1trials.addData('feedbackResponse.rt', feedbackResponse.rt)
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nBlockRepeats repeats of 'SCIAT1trials'
    
# completed 1 repeats of 'SCIAT1blocks'


# set up handler to look after randomisation of conditions etc
likertPre = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('trials_likerts_chinese.xlsx'),
    seed=None, name='likertPre')
thisExp.addLoop(likertPre)  # add the loop to the experiment
thisLikertPre = likertPre.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLikertPre.rgb)
if thisLikertPre != None:
    for paramName in thisLikertPre.keys():
        exec(paramName + '= thisLikertPre.' + paramName)

for thisLikertPre in likertPre:
    currentLoop = likertPre
    # abbreviate parameter names if possible (e.g. rgb = thisLikertPre.rgb)
    if thisLikertPre != None:
        for paramName in thisLikertPre.keys():
            exec(paramName + '= thisLikertPre.' + paramName)
    
    #------Prepare to start Routine "likertScales"-------
    t = 0
    likertScalesClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    rating.reset()
    instructionBox.setText(instruction)
    image.setImage(exemplar)
    # keep track of which components have finished
    likertScalesComponents = []
    likertScalesComponents.append(rating)
    likertScalesComponents.append(instructionBox)
    likertScalesComponents.append(image)
    for thisComponent in likertScalesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "likertScales"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = likertScalesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating* updates
        if t >= 0.5 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t  # underestimates by a little under one frame
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # *instructionBox* updates
        if t >= 0 and instructionBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionBox.tStart = t  # underestimates by a little under one frame
            instructionBox.frameNStart = frameN  # exact frame index
            instructionBox.setAutoDraw(True)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in likertScalesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "likertScales"-------
    for thisComponent in likertScalesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for likertPre (TrialHandler)
    likertPre.addData('rating.response', rating.getRating())
    # the Routine "likertScales" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'likertPre'


# set up handler to look after randomisation of conditions etc
IATblocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(IATtaskFile),
    seed=None, name='IATblocks')
thisExp.addLoop(IATblocks)  # add the loop to the experiment
thisIATblock = IATblocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIATblock.rgb)
if thisIATblock != None:
    for paramName in thisIATblock.keys():
        exec(paramName + '= thisIATblock.' + paramName)

for thisIATblock in IATblocks:
    currentLoop = IATblocks
    # abbreviate parameter names if possible (e.g. rgb = thisIATblock.rgb)
    if thisIATblock != None:
        for paramName in thisIATblock.keys():
            exec(paramName + '= thisIATblock.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setColor(colourA, colorSpace='rgb')
    instructionsBox.setText(instruction)
    responseContinue = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue.status = NOT_STARTED
    target1box_inst.setColor(colourA, colorSpace='rgb')
    target1box_inst.setText(target1)
    target2box_inst.setColor(colourA, colorSpace='rgb')
    target2box_inst.setText(target2)
    attribute1box_inst.setColor(colourB, colorSpace='rgb')
    attribute1box_inst.setText(attribute1)
    attribute2box_inst.setColor(colourB, colorSpace='rgb')
    attribute2box_inst.setText(attribute2)
    orLeftBox_inst.setColor(colourA, colorSpace='rgb')
    orLeftBox_inst.setText(orStimulusLeft)
    orRightBox_inst.setColor(colourA, colorSpace='rgb')
    orRightBox_inst.setText(orStimulusRight)
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(responseContinue)
    instructionsComponents.append(target1box_inst)
    instructionsComponents.append(target2box_inst)
    instructionsComponents.append(attribute1box_inst)
    instructionsComponents.append(attribute2box_inst)
    instructionsComponents.append(orLeftBox_inst)
    instructionsComponents.append(orRightBox_inst)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 1 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *responseContinue* updates
        if t >= 1.5 and responseContinue.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue.tStart = t  # underestimates by a little under one frame
            responseContinue.frameNStart = frameN  # exact frame index
            responseContinue.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if responseContinue.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *target1box_inst* updates
        if t >= 1 and target1box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box_inst.tStart = t  # underestimates by a little under one frame
            target1box_inst.frameNStart = frameN  # exact frame index
            target1box_inst.setAutoDraw(True)
        
        # *target2box_inst* updates
        if t >= 1 and target2box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box_inst.tStart = t  # underestimates by a little under one frame
            target2box_inst.frameNStart = frameN  # exact frame index
            target2box_inst.setAutoDraw(True)
        
        # *attribute1box_inst* updates
        if t >= 1 and attribute1box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box_inst.tStart = t  # underestimates by a little under one frame
            attribute1box_inst.frameNStart = frameN  # exact frame index
            attribute1box_inst.setAutoDraw(True)
        
        # *attribute2box_inst* updates
        if t >= 1 and attribute2box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box_inst.tStart = t  # underestimates by a little under one frame
            attribute2box_inst.frameNStart = frameN  # exact frame index
            attribute2box_inst.setAutoDraw(True)
        
        # *orLeftBox_inst* updates
        if t >= 1 and orLeftBox_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox_inst.tStart = t  # underestimates by a little under one frame
            orLeftBox_inst.frameNStart = frameN  # exact frame index
            orLeftBox_inst.setAutoDraw(True)
        
        # *orRightBox_inst* updates
        if t >= 1 and orRightBox_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox_inst.tStart = t  # underestimates by a little under one frame
            orRightBox_inst.frameNStart = frameN  # exact frame index
            orRightBox_inst.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    IATtrials = data.TrialHandler(nReps=nBlockRepeats, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(block),
        seed=None, name='IATtrials')
    thisExp.addLoop(IATtrials)  # add the loop to the experiment
    thisIATtrial = IATtrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisIATtrial.rgb)
    if thisIATtrial != None:
        for paramName in thisIATtrial.keys():
            exec(paramName + '= thisIATtrial.' + paramName)
    
    for thisIATtrial in IATtrials:
        currentLoop = IATtrials
        # abbreviate parameter names if possible (e.g. rgb = thisIATtrial.rgb)
        if thisIATtrial != None:
            for paramName in thisIATtrial.keys():
                exec(paramName + '= thisIATtrial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        stimulusImage.setImage(imageStimulus)
        stimulusBox.setColor(stimulusColour, colorSpace='rgb')
        stimulusBox.setText(stimulus)
        requiredResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        requiredResponse.status = NOT_STARTED
        feedbackResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        feedbackResponse.status = NOT_STARTED
        
        target1box.setColor(colourA, colorSpace='rgb')
        target1box.setText(target1)
        target2box.setColor(colourA, colorSpace='rgb')
        target2box.setText(target2)
        attribute1box.setColor(colourB, colorSpace='rgb')
        attribute1box.setText(attribute1
)
        attribute2box.setColor(colourB, colorSpace='rgb')
        attribute2box.setText(attribute2)
        orLeftBox.setColor(colourA, colorSpace='rgb')
        orLeftBox.setText(orStimulusLeft)
        orRightBox.setColor(colourA, colorSpace='rgb')
        orRightBox.setText(orStimulusRight)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(stimulusImage)
        trialComponents.append(stimulusBox)
        trialComponents.append(requiredResponse)
        trialComponents.append(feedbackResponse)
        trialComponents.append(accuracyFeedback)
        trialComponents.append(target1box)
        trialComponents.append(target2box)
        trialComponents.append(attribute1box)
        trialComponents.append(attribute2box)
        trialComponents.append(orLeftBox)
        trialComponents.append(orRightBox)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulusImage* updates
            if t >= 0.3 and stimulusImage.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusImage.tStart = t  # underestimates by a little under one frame
                stimulusImage.frameNStart = frameN  # exact frame index
                stimulusImage.setAutoDraw(True)
            
            # *stimulusBox* updates
            if t >= 0.3 and stimulusBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusBox.tStart = t  # underestimates by a little under one frame
                stimulusBox.frameNStart = frameN  # exact frame index
                stimulusBox.setAutoDraw(True)
            
            # *requiredResponse* updates
            if t >= 0.3 and requiredResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                requiredResponse.tStart = t  # underestimates by a little under one frame
                requiredResponse.frameNStart = frameN  # exact frame index
                requiredResponse.status = STARTED
                # AllowedKeys looks like a variable named `requiredAllowed`
                if not 'requiredAllowed' in locals():
                    logging.error('AllowedKeys variable `requiredAllowed` is not defined.')
                    core.quit()
                if not type(requiredAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(requiredAllowed, basestring):
                        logging.error('AllowedKeys variable `requiredAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in requiredAllowed: requiredAllowed = (requiredAllowed,)
                    else:  requiredAllowed = eval(requiredAllowed)
                # keyboard checking is just starting
                requiredResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if requiredResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(requiredAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if requiredResponse.keys == []:  # then this was the first keypress
                        requiredResponse.keys = theseKeys[0]  # just the first key pressed
                        requiredResponse.rt = requiredResponse.clock.getTime()
                        # was this 'correct'?
                        if (requiredResponse.keys == str(requiredKey)) or (requiredResponse.keys == requiredKey):
                            requiredResponse.corr = 1
                        else:
                            requiredResponse.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *feedbackResponse* updates
            if t >= 0.3 and feedbackResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackResponse.tStart = t  # underestimates by a little under one frame
                feedbackResponse.frameNStart = frameN  # exact frame index
                feedbackResponse.status = STARTED
                # AllowedKeys looks like a variable named `feedbackAllowed`
                if not 'feedbackAllowed' in locals():
                    logging.error('AllowedKeys variable `feedbackAllowed` is not defined.')
                    core.quit()
                if not type(feedbackAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(feedbackAllowed, basestring):
                        logging.error('AllowedKeys variable `feedbackAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in feedbackAllowed: feedbackAllowed = (feedbackAllowed,)
                    else:  feedbackAllowed = eval(feedbackAllowed)
                # keyboard checking is just starting
                feedbackResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if feedbackResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(feedbackAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if feedbackResponse.keys == []:  # then this was the first keypress
                        feedbackResponse.keys = theseKeys[0]  # just the first key pressed
                        feedbackResponse.rt = feedbackResponse.clock.getTime()
                        # was this 'correct'?
                        if (feedbackResponse.keys == str(feedbackKey)) or (feedbackResponse.keys == feedbackKey):
                            feedbackResponse.corr = 1
                        else:
                            feedbackResponse.corr = 0
            if len(feedbackResponse.keys)<1:
                msg1=""
            else:
                msg1="X"
            
            # *accuracyFeedback* updates
            if t >= 0.3 and accuracyFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyFeedback.tStart = t  # underestimates by a little under one frame
                accuracyFeedback.frameNStart = frameN  # exact frame index
                accuracyFeedback.setAutoDraw(True)
            if accuracyFeedback.status == STARTED:  # only update if being drawn
                accuracyFeedback.setText(msg1, log=False)
            
            # *target1box* updates
            if t >= 0.0 and target1box.status == NOT_STARTED:
                # keep track of start time/frame for later
                target1box.tStart = t  # underestimates by a little under one frame
                target1box.frameNStart = frameN  # exact frame index
                target1box.setAutoDraw(True)
            
            # *target2box* updates
            if t >= 0.0 and target2box.status == NOT_STARTED:
                # keep track of start time/frame for later
                target2box.tStart = t  # underestimates by a little under one frame
                target2box.frameNStart = frameN  # exact frame index
                target2box.setAutoDraw(True)
            
            # *attribute1box* updates
            if t >= 0.0 and attribute1box.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute1box.tStart = t  # underestimates by a little under one frame
                attribute1box.frameNStart = frameN  # exact frame index
                attribute1box.setAutoDraw(True)
            
            # *attribute2box* updates
            if t >= 0.0 and attribute2box.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute2box.tStart = t  # underestimates by a little under one frame
                attribute2box.frameNStart = frameN  # exact frame index
                attribute2box.setAutoDraw(True)
            
            # *orLeftBox* updates
            if t >= 0.0 and orLeftBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                orLeftBox.tStart = t  # underestimates by a little under one frame
                orLeftBox.frameNStart = frameN  # exact frame index
                orLeftBox.setAutoDraw(True)
            
            # *orRightBox* updates
            if t >= 0.0 and orRightBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                orRightBox.tStart = t  # underestimates by a little under one frame
                orRightBox.frameNStart = frameN  # exact frame index
                orRightBox.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if requiredResponse.keys in ['', [], None]:  # No response was made
           requiredResponse.keys=None
           # was no response the correct answer?!
           if str(requiredKey).lower() == 'none': requiredResponse.corr = 1  # correct non-response
           else: requiredResponse.corr = 0  # failed to respond (incorrectly)
        # store data for IATtrials (TrialHandler)
        IATtrials.addData('requiredResponse.keys',requiredResponse.keys)
        IATtrials.addData('requiredResponse.corr', requiredResponse.corr)
        if requiredResponse.keys != None:  # we had a response
            IATtrials.addData('requiredResponse.rt', requiredResponse.rt)
        # check responses
        if feedbackResponse.keys in ['', [], None]:  # No response was made
           feedbackResponse.keys=None
           # was no response the correct answer?!
           if str(feedbackKey).lower() == 'none': feedbackResponse.corr = 1  # correct non-response
           else: feedbackResponse.corr = 0  # failed to respond (incorrectly)
        # store data for IATtrials (TrialHandler)
        IATtrials.addData('feedbackResponse.keys',feedbackResponse.keys)
        IATtrials.addData('feedbackResponse.corr', feedbackResponse.corr)
        if feedbackResponse.keys != None:  # we had a response
            IATtrials.addData('feedbackResponse.rt', feedbackResponse.rt)
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nBlockRepeats repeats of 'IATtrials'
    
# completed 1 repeats of 'IATblocks'


# set up handler to look after randomisation of conditions etc
likertPost = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('trials_likerts_chinese.xlsx'),
    seed=None, name='likertPost')
thisExp.addLoop(likertPost)  # add the loop to the experiment
thisLikertPost = likertPost.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLikertPost.rgb)
if thisLikertPost != None:
    for paramName in thisLikertPost.keys():
        exec(paramName + '= thisLikertPost.' + paramName)

for thisLikertPost in likertPost:
    currentLoop = likertPost
    # abbreviate parameter names if possible (e.g. rgb = thisLikertPost.rgb)
    if thisLikertPost != None:
        for paramName in thisLikertPost.keys():
            exec(paramName + '= thisLikertPost.' + paramName)
    
    #------Prepare to start Routine "likertScales"-------
    t = 0
    likertScalesClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    rating.reset()
    instructionBox.setText(instruction)
    image.setImage(exemplar)
    # keep track of which components have finished
    likertScalesComponents = []
    likertScalesComponents.append(rating)
    likertScalesComponents.append(instructionBox)
    likertScalesComponents.append(image)
    for thisComponent in likertScalesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "likertScales"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = likertScalesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating* updates
        if t >= 0.5 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t  # underestimates by a little under one frame
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # *instructionBox* updates
        if t >= 0 and instructionBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionBox.tStart = t  # underestimates by a little under one frame
            instructionBox.frameNStart = frameN  # exact frame index
            instructionBox.setAutoDraw(True)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in likertScalesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "likertScales"-------
    for thisComponent in likertScalesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for likertPost (TrialHandler)
    likertPost.addData('rating.response', rating.getRating())
    # the Routine "likertScales" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'likertPost'


# set up handler to look after randomisation of conditions etc
SCIAT2blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(SCIATtaskFile),
    seed=None, name='SCIAT2blocks')
thisExp.addLoop(SCIAT2blocks)  # add the loop to the experiment
thisSCIAT2block = SCIAT2blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisSCIAT2block.rgb)
if thisSCIAT2block != None:
    for paramName in thisSCIAT2block.keys():
        exec(paramName + '= thisSCIAT2block.' + paramName)

for thisSCIAT2block in SCIAT2blocks:
    currentLoop = SCIAT2blocks
    # abbreviate parameter names if possible (e.g. rgb = thisSCIAT2block.rgb)
    if thisSCIAT2block != None:
        for paramName in thisSCIAT2block.keys():
            exec(paramName + '= thisSCIAT2block.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setColor(colourA, colorSpace='rgb')
    instructionsBox.setText(instruction)
    responseContinue = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue.status = NOT_STARTED
    target1box_inst.setColor(colourA, colorSpace='rgb')
    target1box_inst.setText(target1)
    target2box_inst.setColor(colourA, colorSpace='rgb')
    target2box_inst.setText(target2)
    attribute1box_inst.setColor(colourB, colorSpace='rgb')
    attribute1box_inst.setText(attribute1)
    attribute2box_inst.setColor(colourB, colorSpace='rgb')
    attribute2box_inst.setText(attribute2)
    orLeftBox_inst.setColor(colourA, colorSpace='rgb')
    orLeftBox_inst.setText(orStimulusLeft)
    orRightBox_inst.setColor(colourA, colorSpace='rgb')
    orRightBox_inst.setText(orStimulusRight)
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(responseContinue)
    instructionsComponents.append(target1box_inst)
    instructionsComponents.append(target2box_inst)
    instructionsComponents.append(attribute1box_inst)
    instructionsComponents.append(attribute2box_inst)
    instructionsComponents.append(orLeftBox_inst)
    instructionsComponents.append(orRightBox_inst)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 1 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *responseContinue* updates
        if t >= 1.5 and responseContinue.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue.tStart = t  # underestimates by a little under one frame
            responseContinue.frameNStart = frameN  # exact frame index
            responseContinue.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if responseContinue.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *target1box_inst* updates
        if t >= 1 and target1box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box_inst.tStart = t  # underestimates by a little under one frame
            target1box_inst.frameNStart = frameN  # exact frame index
            target1box_inst.setAutoDraw(True)
        
        # *target2box_inst* updates
        if t >= 1 and target2box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box_inst.tStart = t  # underestimates by a little under one frame
            target2box_inst.frameNStart = frameN  # exact frame index
            target2box_inst.setAutoDraw(True)
        
        # *attribute1box_inst* updates
        if t >= 1 and attribute1box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box_inst.tStart = t  # underestimates by a little under one frame
            attribute1box_inst.frameNStart = frameN  # exact frame index
            attribute1box_inst.setAutoDraw(True)
        
        # *attribute2box_inst* updates
        if t >= 1 and attribute2box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box_inst.tStart = t  # underestimates by a little under one frame
            attribute2box_inst.frameNStart = frameN  # exact frame index
            attribute2box_inst.setAutoDraw(True)
        
        # *orLeftBox_inst* updates
        if t >= 1 and orLeftBox_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox_inst.tStart = t  # underestimates by a little under one frame
            orLeftBox_inst.frameNStart = frameN  # exact frame index
            orLeftBox_inst.setAutoDraw(True)
        
        # *orRightBox_inst* updates
        if t >= 1 and orRightBox_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox_inst.tStart = t  # underestimates by a little under one frame
            orRightBox_inst.frameNStart = frameN  # exact frame index
            orRightBox_inst.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    SCIAT2trials = data.TrialHandler(nReps=nBlockRepeats, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(block),
        seed=None, name='SCIAT2trials')
    thisExp.addLoop(SCIAT2trials)  # add the loop to the experiment
    thisSCIAT2trial = SCIAT2trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisSCIAT2trial.rgb)
    if thisSCIAT2trial != None:
        for paramName in thisSCIAT2trial.keys():
            exec(paramName + '= thisSCIAT2trial.' + paramName)
    
    for thisSCIAT2trial in SCIAT2trials:
        currentLoop = SCIAT2trials
        # abbreviate parameter names if possible (e.g. rgb = thisSCIAT2trial.rgb)
        if thisSCIAT2trial != None:
            for paramName in thisSCIAT2trial.keys():
                exec(paramName + '= thisSCIAT2trial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        stimulusImage.setImage(imageStimulus)
        stimulusBox.setColor(stimulusColour, colorSpace='rgb')
        stimulusBox.setText(stimulus)
        requiredResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        requiredResponse.status = NOT_STARTED
        feedbackResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        feedbackResponse.status = NOT_STARTED
        
        target1box.setColor(colourA, colorSpace='rgb')
        target1box.setText(target1)
        target2box.setColor(colourA, colorSpace='rgb')
        target2box.setText(target2)
        attribute1box.setColor(colourB, colorSpace='rgb')
        attribute1box.setText(attribute1
)
        attribute2box.setColor(colourB, colorSpace='rgb')
        attribute2box.setText(attribute2)
        orLeftBox.setColor(colourA, colorSpace='rgb')
        orLeftBox.setText(orStimulusLeft)
        orRightBox.setColor(colourA, colorSpace='rgb')
        orRightBox.setText(orStimulusRight)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(stimulusImage)
        trialComponents.append(stimulusBox)
        trialComponents.append(requiredResponse)
        trialComponents.append(feedbackResponse)
        trialComponents.append(accuracyFeedback)
        trialComponents.append(target1box)
        trialComponents.append(target2box)
        trialComponents.append(attribute1box)
        trialComponents.append(attribute2box)
        trialComponents.append(orLeftBox)
        trialComponents.append(orRightBox)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulusImage* updates
            if t >= 0.3 and stimulusImage.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusImage.tStart = t  # underestimates by a little under one frame
                stimulusImage.frameNStart = frameN  # exact frame index
                stimulusImage.setAutoDraw(True)
            
            # *stimulusBox* updates
            if t >= 0.3 and stimulusBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusBox.tStart = t  # underestimates by a little under one frame
                stimulusBox.frameNStart = frameN  # exact frame index
                stimulusBox.setAutoDraw(True)
            
            # *requiredResponse* updates
            if t >= 0.3 and requiredResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                requiredResponse.tStart = t  # underestimates by a little under one frame
                requiredResponse.frameNStart = frameN  # exact frame index
                requiredResponse.status = STARTED
                # AllowedKeys looks like a variable named `requiredAllowed`
                if not 'requiredAllowed' in locals():
                    logging.error('AllowedKeys variable `requiredAllowed` is not defined.')
                    core.quit()
                if not type(requiredAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(requiredAllowed, basestring):
                        logging.error('AllowedKeys variable `requiredAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in requiredAllowed: requiredAllowed = (requiredAllowed,)
                    else:  requiredAllowed = eval(requiredAllowed)
                # keyboard checking is just starting
                requiredResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if requiredResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(requiredAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if requiredResponse.keys == []:  # then this was the first keypress
                        requiredResponse.keys = theseKeys[0]  # just the first key pressed
                        requiredResponse.rt = requiredResponse.clock.getTime()
                        # was this 'correct'?
                        if (requiredResponse.keys == str(requiredKey)) or (requiredResponse.keys == requiredKey):
                            requiredResponse.corr = 1
                        else:
                            requiredResponse.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *feedbackResponse* updates
            if t >= 0.3 and feedbackResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackResponse.tStart = t  # underestimates by a little under one frame
                feedbackResponse.frameNStart = frameN  # exact frame index
                feedbackResponse.status = STARTED
                # AllowedKeys looks like a variable named `feedbackAllowed`
                if not 'feedbackAllowed' in locals():
                    logging.error('AllowedKeys variable `feedbackAllowed` is not defined.')
                    core.quit()
                if not type(feedbackAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(feedbackAllowed, basestring):
                        logging.error('AllowedKeys variable `feedbackAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in feedbackAllowed: feedbackAllowed = (feedbackAllowed,)
                    else:  feedbackAllowed = eval(feedbackAllowed)
                # keyboard checking is just starting
                feedbackResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if feedbackResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(feedbackAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if feedbackResponse.keys == []:  # then this was the first keypress
                        feedbackResponse.keys = theseKeys[0]  # just the first key pressed
                        feedbackResponse.rt = feedbackResponse.clock.getTime()
                        # was this 'correct'?
                        if (feedbackResponse.keys == str(feedbackKey)) or (feedbackResponse.keys == feedbackKey):
                            feedbackResponse.corr = 1
                        else:
                            feedbackResponse.corr = 0
            if len(feedbackResponse.keys)<1:
                msg1=""
            else:
                msg1="X"
            
            # *accuracyFeedback* updates
            if t >= 0.3 and accuracyFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyFeedback.tStart = t  # underestimates by a little under one frame
                accuracyFeedback.frameNStart = frameN  # exact frame index
                accuracyFeedback.setAutoDraw(True)
            if accuracyFeedback.status == STARTED:  # only update if being drawn
                accuracyFeedback.setText(msg1, log=False)
            
            # *target1box* updates
            if t >= 0.0 and target1box.status == NOT_STARTED:
                # keep track of start time/frame for later
                target1box.tStart = t  # underestimates by a little under one frame
                target1box.frameNStart = frameN  # exact frame index
                target1box.setAutoDraw(True)
            
            # *target2box* updates
            if t >= 0.0 and target2box.status == NOT_STARTED:
                # keep track of start time/frame for later
                target2box.tStart = t  # underestimates by a little under one frame
                target2box.frameNStart = frameN  # exact frame index
                target2box.setAutoDraw(True)
            
            # *attribute1box* updates
            if t >= 0.0 and attribute1box.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute1box.tStart = t  # underestimates by a little under one frame
                attribute1box.frameNStart = frameN  # exact frame index
                attribute1box.setAutoDraw(True)
            
            # *attribute2box* updates
            if t >= 0.0 and attribute2box.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute2box.tStart = t  # underestimates by a little under one frame
                attribute2box.frameNStart = frameN  # exact frame index
                attribute2box.setAutoDraw(True)
            
            # *orLeftBox* updates
            if t >= 0.0 and orLeftBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                orLeftBox.tStart = t  # underestimates by a little under one frame
                orLeftBox.frameNStart = frameN  # exact frame index
                orLeftBox.setAutoDraw(True)
            
            # *orRightBox* updates
            if t >= 0.0 and orRightBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                orRightBox.tStart = t  # underestimates by a little under one frame
                orRightBox.frameNStart = frameN  # exact frame index
                orRightBox.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if requiredResponse.keys in ['', [], None]:  # No response was made
           requiredResponse.keys=None
           # was no response the correct answer?!
           if str(requiredKey).lower() == 'none': requiredResponse.corr = 1  # correct non-response
           else: requiredResponse.corr = 0  # failed to respond (incorrectly)
        # store data for SCIAT2trials (TrialHandler)
        SCIAT2trials.addData('requiredResponse.keys',requiredResponse.keys)
        SCIAT2trials.addData('requiredResponse.corr', requiredResponse.corr)
        if requiredResponse.keys != None:  # we had a response
            SCIAT2trials.addData('requiredResponse.rt', requiredResponse.rt)
        # check responses
        if feedbackResponse.keys in ['', [], None]:  # No response was made
           feedbackResponse.keys=None
           # was no response the correct answer?!
           if str(feedbackKey).lower() == 'none': feedbackResponse.corr = 1  # correct non-response
           else: feedbackResponse.corr = 0  # failed to respond (incorrectly)
        # store data for SCIAT2trials (TrialHandler)
        SCIAT2trials.addData('feedbackResponse.keys',feedbackResponse.keys)
        SCIAT2trials.addData('feedbackResponse.corr', feedbackResponse.corr)
        if feedbackResponse.keys != None:  # we had a response
            SCIAT2trials.addData('feedbackResponse.rt', feedbackResponse.rt)
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nBlockRepeats repeats of 'SCIAT2trials'
    
# completed 1 repeats of 'SCIAT2blocks'


# set up handler to look after randomisation of conditions etc
likertValence = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('trials_likerts_flowers&insects.xlsx'),
    seed=None, name='likertValence')
thisExp.addLoop(likertValence)  # add the loop to the experiment
thisLikertValence = likertValence.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLikertValence.rgb)
if thisLikertValence != None:
    for paramName in thisLikertValence.keys():
        exec(paramName + '= thisLikertValence.' + paramName)

for thisLikertValence in likertValence:
    currentLoop = likertValence
    # abbreviate parameter names if possible (e.g. rgb = thisLikertValence.rgb)
    if thisLikertValence != None:
        for paramName in thisLikertValence.keys():
            exec(paramName + '= thisLikertValence.' + paramName)
    
    #------Prepare to start Routine "likertScales"-------
    t = 0
    likertScalesClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    rating.reset()
    instructionBox.setText(instruction)
    image.setImage(exemplar)
    # keep track of which components have finished
    likertScalesComponents = []
    likertScalesComponents.append(rating)
    likertScalesComponents.append(instructionBox)
    likertScalesComponents.append(image)
    for thisComponent in likertScalesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "likertScales"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = likertScalesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating* updates
        if t >= 0.5 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t  # underestimates by a little under one frame
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # *instructionBox* updates
        if t >= 0 and instructionBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionBox.tStart = t  # underestimates by a little under one frame
            instructionBox.frameNStart = frameN  # exact frame index
            instructionBox.setAutoDraw(True)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in likertScalesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "likertScales"-------
    for thisComponent in likertScalesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for likertValence (TrialHandler)
    likertValence.addData('rating.response', rating.getRating())
    # the Routine "likertScales" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'likertValence'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(text)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 1 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    if text.status == STARTED and t >= (1 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



win.close()
core.quit()
