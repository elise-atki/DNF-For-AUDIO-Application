#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:01:50 2022

@author: elise
"""

# need to plot dB values somehow

amplitude = 10 #any val to test

outsig = amplitude*array_dnfsig #amplifies signal

sf.write("dnfsig.wav",outsig,44100) #converts to .wav (does this too quickly)
#-------------
