#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:15:43 2022

@author: elise
"""
import numpy as np

import soundfile as sf

filteredaud = np.empty(0, dtype = 'float')

filteredaud = np.loadtxt("recfilteredout.dat")[:,0] #getting output audio data from lms #recording2bassn
print(filteredaud)

#https://www.tutorialspoint.com/read-and-write-wav-files-using-python-wave <- code based on this webpage
#https://stackoverflow.com/questions/16778878/python-write-a-wav-file-into-numpy-float-array

sf.write('recoutput_mainsremoved.wav',filteredaud,44100) #rec2bass
    