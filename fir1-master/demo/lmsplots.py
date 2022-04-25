#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:10:11 2022

@author: elise

"""

import numpy as np
import matplotlib.pyplot as plt


#audio clip is approx. 34s long 
sample_rate = 44100

lms_raw = np.loadtxt("recording2voxs+n.dat")[:,1]#, delimiter = ",", usecols = (0)) #loads in data file to float array    , usecols = (0)
#print(lms_raw)

#plots of raw lms (channel1)
max_time1 = lms_raw.size/sample_rate

time_steps1 = np.linspace(0,max_time1,lms_raw.size)

plt.figure()
plt.plot(time_steps1,lms_raw)
plt.title('Channel 1 (x[n])')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude(t)')
plt.show()



lms_noise= np.loadtxt("recording2bassn.dat")[:,1]#, delimiter = ",", usecols = (0)) #loads in data file to float array    , usecols = (0)
#print(lms_noise)

#plots of noise lms (channel2)
max_time2 = lms_noise.size/sample_rate

time_steps2 = np.linspace(0,max_time2,lms_noise.size)

plt.figure()
plt.plot(time_steps2,lms_noise)
plt.title('Channel 2 (y[n])')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude(t)')
plt.show()



lms_filtered = np.loadtxt("recfilteredout.dat")[:,0]#, delimiter = ",", usecols = (0)) #loads in data file to float array    , usecols = (0)
#print(lms_filtered)

#plots of lms and fft

max_time = lms_filtered.size/sample_rate

time_steps = np.linspace(0,max_time,lms_filtered.size)

plt.figure()
plt.plot(time_steps,lms_filtered)
plt.title('LMS Filtered Output (e[n])')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude(t)')
plt.show()

f = np.abs(np.fft.fft(lms_filtered))
freq_steps = np.fft.fftfreq(lms_filtered.size,d=1/sample_rate)


plt.figure()
plt.plot(freq_steps,f)
plt.title('LMS Filtered: Fourier Transform')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude(Hz)')
plt.show()



