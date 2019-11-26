#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
import random
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()

option_chosen = event.getKeys(keyList=('a', 'b'))
option_A_chosen = 0
option_B_chosen = 0

option_A_self = [1, 2, 5]
option_A_other = [5, 10, 15]

option_B_self = [5, 10, 15]
option_B_other = [-10, -15, -20]


option_A = visual.TextStim(win=win, name='option_A',
    text='   Option A\n\n    You: +'+option_A_self[random.randint(0, 2)]+'\nYour Team: +'+option_A_other[random.randint(0, 2)]+'',
    font='Arial',
    pos=(-0.4, -0.2), height=0.1,
    color='black', depth=0.0);
option_A.draw()
option_B = visual.TextStim(win=win, name='option_B',
    text='    Option B\n\n     You: +'+option_B_self[random.randint(0, 2)]+'\nYour Team: '+option_B_other[random.randint(0, 2)]+'',
    font='Arial',
    pos=(0.4, -0.2), height=0.1,
    color='black', depth=-1.0);
option_B.draw()
win.flip()

if option_chosen[0] == 'a':
    option_A_chosen += 1
    event.clearEvents()
if option_chosen[0] == 'b':
    option_B_chosen += 1
    event.clearEvents()

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(3)
win.close()
