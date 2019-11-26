#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()

option_chosen = event.getKeys(keyList=('a', 'b'))
option_A_chosen_own = 0
option_B_chosen_own = 0
option_A_chosen_other = 0
option_B_chosen_other = 0

option_A_self = [1, 2, 5]
option_A_other = [5, 10, 15]

option_B_self = [5, 10, 15]
option_B_other = [-10, -15, -20]

trials = 20

#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things


# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']


# make your loop
for t in range(trials):
    team = 'Your Team'
    if t >= 10:
        team = 'Other Team'

    option_A = visual.TextStim(win=win, name='option_A',
    text='   Option A\n\n    You: +' + str(option_A_self[random.randint(0, 2)]) + '\n' + team + ': +' + str(option_A_other[random.randint(0, 2)]) + '',
    font='Arial',
    pos=(-0.4, -0.2), height=0.1,
    color='black', depth=0.0);
    option_A.draw()
    option_B = visual.TextStim(win=win, name='option_B',
    text='    Option B\n\n     You: +' + str(option_B_self[random.randint(0, 2)]) + '\n' + team + ': ' + str(option_B_other[random.randint(0, 2)]) + '',
    font='Arial',
    pos=(0.4, -0.2), height=0.1,
    color='black', depth=-1.0);
    option_B.draw()
    win.flip()

    if option_chosen[0] == 'a':
        if t >= 10:
            option_A_chosen_other += 1
        else:
            option_A_chosen_own += 1
        event.clearEvents()
        option_A.hide()
        option_B.hide()
        win.flip()
    if option_chosen[0] == 'b':
        if t >= 10:
            option_B_chosen_other += 1
        else:
            option_B_chosen_own += 1
        event.clearEvents()
        option_A.hide()
        option_B.hide()
        win.flip()
    
    # include your trial code in your loop but replace anything that should 
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!


#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
