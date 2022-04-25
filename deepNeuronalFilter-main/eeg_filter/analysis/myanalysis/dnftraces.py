#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:31:20 2022

@author: elise
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reads in .tsv and conversts to .csv in an array

tsv_file='inner.tsv'
csv_table=pd.read_table(tsv_file,sep='\t') #ch1
csv_table.to_csv("inner2.csv",index=False)

tsv_file2='outer.tsv'
csv_table2=pd.read_table(tsv_file2,sep='\t') #ch2
csv_table2.to_csv("outer2.csv",index=False)

tsv_file3='dnf.tsv'
csv_table3=pd.read_table(tsv_file3,sep='\t') #dnf output
csv_table3.to_csv("dnf2.csv",index=False)

tsv_file4='lms.tsv'
csv_table4=pd.read_table(tsv_file4,sep='\t') #lms out
csv_table4.to_csv("lms2.csv",index=False)


sample_rate =44100
#-------

array_rawsig = np.loadtxt("inner2.csv", delimiter = ",", usecols = (0)) #loads in data file to float array
print(array_rawsig)

max_time1 = array_rawsig.size/sample_rate
time_steps1 = np.linspace(0,max_time1,array_rawsig.size)

plt.figure()
plt.plot(time_steps1,array_rawsig)
plt.title('Channel 1 (x[n])')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude(t)')
plt.show()


f1 = np.abs(np.fft.fft(array_rawsig))
freq_steps1 = np.fft.fftfreq(array_rawsig.size,d=1/sample_rate)

plt.figure()
plt.plot(freq_steps1,f1)
plt.title('Channel 1 (x[n]): Fourier Transform')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude(Hz)')
plt.show()

#------------
array_noisesig = np.loadtxt("outer2.csv", delimiter = ",", usecols = (0)) #loads in data file to float array
print(array_noisesig)

myint= 100

red_array_noisesig = [x/myint for x in array_noisesig]

max_time2 = (array_noisesig.size/sample_rate)
time_steps2 = np.linspace(0,max_time2,array_noisesig.size)

plt.figure()
plt.plot(time_steps2,red_array_noisesig)
plt.title('Channel 2 (y[n])')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude(t)')
plt.show()

#-----
array_dnfsig = np.loadtxt("dnf2.csv", delimiter = ",", usecols = (0)) #loads in data file to float array
print(array_dnfsig)

max_time3 = array_dnfsig.size/sample_rate
time_steps3 = np.linspace(0,max_time3,array_dnfsig.size)


plt.figure()
plt.plot(time_steps3,array_dnfsig)
plt.title('DNF Output (e[n])')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude(t)')
plt.show()


f = np.abs(np.fft.fft(array_dnfsig))
freq_steps = np.fft.fftfreq(array_dnfsig.size,d=1/sample_rate)

plt.figure()
plt.plot(freq_steps,f)
plt.title('DNF Filtered: Fourier Transform')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude(Hz)')
plt.show()


#-------

array_dnfcanceller = np.loadtxt("dnf2.csv", delimiter = ",", usecols = (1)) #loads in data file to float array
print(array_dnfcanceller)


max_time4 = array_dnfcanceller.size/sample_rate
time_steps4 = np.linspace(0,max_time4,array_dnfcanceller.size)


plt.figure()
plt.plot(time_steps4,array_dnfcanceller)
plt.title('DNF Canceller (z[n])')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude(t)')
plt.show()

#lms dat for comparison
array_lmssig = np.loadtxt("lms2.csv", delimiter = ",", usecols = (0)) #loads in data file to float array
print(array_lmssig)

max_time5 = array_lmssig.size/sample_rate
time_steps5 = np.linspace(0,max_time5,array_lmssig.size)


plt.figure()
plt.plot(time_steps5,array_lmssig)
plt.title('LMS Output')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude(t)')
plt.show()


#-----
array_lmsremover = np.loadtxt("lms2.csv", delimiter = ",", usecols = (2)) #loads in data file to float array
print(array_lmsremover)

myint3= 1000

red_array_lmsremover = [x/myint3 for x in array_lmsremover]

max_time6 = array_lmsremover.size/sample_rate
time_steps6 = np.linspace(0,max_time6,array_lmsremover.size)

plt.figure()
plt.plot(time_steps6,red_array_lmsremover)
plt.title('LMS Canceller')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude(t)')
plt.show()


























