#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:03:33 2022

@author: elise
"""
from scipy import signal
import pandas as pd
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import freqz
import statistics as stat

#Plots the PSD and calculates the SNR of the signals


#reading in the signals as arrays

tsv_file='inner.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv("inner2.csv",index=False)

tsv_file2='outer.tsv'
csv_table2=pd.read_table(tsv_file2,sep='\t')
csv_table2.to_csv("outer2.csv",index=False)

tsv_file3='dnf.tsv'
csv_table3=pd.read_table(tsv_file3,sep='\t')
csv_table3.to_csv("dnf2.csv",index=False)

tsv_file4='lms.tsv'
csv_table4=pd.read_table(tsv_file4,sep='\t')
csv_table4.to_csv("lms2.csv",index=False)


#ch1
array_rawsig = np.loadtxt("inner2.csv", delimiter = ",", usecols = (0)) #loads in data file to float array
print(array_rawsig)

array_dnfsig = np.loadtxt("dnf2.csv", delimiter = ",", usecols = (0)) #loads in data file to float array
print(array_dnfsig)

array_lmssig = np.loadtxt("lms2.csv", delimiter = ",", usecols = (0)) #loads in data file to float array
print(array_lmssig)

#ch2

array_noisesig = np.loadtxt("outer2.csv", delimiter = ",", usecols = (0)) #loads in data file to float array
print(array_noisesig)


array_dnfsig_remove= np.loadtxt("dnf2.csv", delimiter = ",", usecols = (1)) #loads in data file to float array
print(array_dnfsig_remove)


array_lmssig_remove = np.loadtxt("lms2.csv", delimiter = ",", usecols = (1)) #loads in data file to float array
print(array_lmssig_remove)

# welch power : https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.welch.html

#noise psd    

rng = np.random.default_rng()
fs = 44100 #sampfreq in Hz.
N = len(array_rawsig)

noise = array_noisesig

fn, Pxx_denn = signal.welch(noise, fs, nperseg=2048)
fn_med, Pxx_den_medn = signal.welch(noise, fs, nperseg=2048, average='median')

ch1 = array_rawsig

fch1, Pxx_dench1 = signal.welch(ch1, fs, nperseg=2048)
f_medch1, Pxx_den_medch1 = signal.welch(ch1, fs, nperseg=2048, average='median')
print(ch1)

plt.figure()
plt.semilogy(fn_med, Pxx_den_medn, label='Channel 1 Noise median',color = 'green')
plt.xlabel('frequency [Hz]')
plt.ylabel('Noise Power Spectral Density [V**2/Hz]')
plt.legend()
plt.show()


noise_power = np.sum(Pxx_den_medn[41:1000])
print(noise_power)


ch1_power = np.sum(Pxx_den_medch1)
print(ch1_power)


SNRraw = np.log10(np.square(ch1_power/noise_power))*10
print(SNRraw)
                  
                  
#dnf noise psd    

rng = np.random.default_rng()
fs = 44100 #sampfreq in Hz.
N = len(array_rawsig)


dnfnoise = array_dnfsig_remove

dnfout = array_dnfsig

fndnfn, Pxx_denndnfn = signal.welch(dnfnoise, fs, nperseg=2048)
fn_meddnfn, Pxx_den_medndnfn = signal.welch(dnfnoise, fs, nperseg=2048, average='median')

fdnfout, Pxx_dendnfout = signal.welch(dnfout, fs, nperseg=2048)
f_meddnfout, Pxx_den_meddnfout = signal.welch(dnfout, fs, nperseg=2048, average='median')
print(dnfout)

plt.semilogy(fn_meddnfn, Pxx_den_medndnfn, label='DNF Noise median',color = 'blue')
plt.legend()
plt.show()


dnfnoise_power = np.sum(Pxx_den_medndnfn[41:1000])
print(dnfnoise_power)

dnfout_power = np.sum(Pxx_den_meddnfout)
print(dnfout_power)


SNRdnf = np.log10(np.square(dnfout_power/dnfnoise_power))*10
print(SNRdnf)
                  



#lms noise psd


myint3= 1000

red_array_lmsremover = [x/myint3 for x in array_lmssig_remove]

lmsnoise = [x*myint3 for x in array_lmssig_remove]


lmsout = array_lmssig

fnlmsn, Pxx_dennlmsn = signal.welch(lmsnoise, fs, nperseg=2048)
fn_medlmsn, Pxx_den_mednlmsn = signal.welch(lmsnoise, fs, nperseg=2048, average='median')


flmsout, Pxx_denlmsout = signal.welch(lmsout, fs, nperseg=2048)
f_medlmsout, Pxx_den_medlmsout = signal.welch(lmsout, fs, nperseg=2048, average='median')
print(lmsout)



plt.semilogy(fn_medlmsn, Pxx_den_mednlmsn, label='LMS Noise median',color = 'red')
plt.legend()
plt.show()


lmsnoise_power = np.sum(Pxx_den_mednlmsn[41:1000])
print(lmsnoise_power)


lmsout_power = np.sum(Pxx_den_medlmsout)
print(lmsout_power)

SNRlms = np.log10(np.square(lmsout_power/lmsnoise_power))*10
print(SNRlms, "dB")

SNRdnf = np.log10(np.square(dnfout_power/dnfnoise_power))*10
print(SNRdnf, "dB")
             

SNRraw = np.log10(np.square(ch1_power/noise_power))*10
print(SNRraw, "dB")
                  
                


#signal psd's (don't necessary)


#raw signal PSD
x = array_rawsig
x += rng.normal(scale=np.sqrt(noise_power))#,size=time.shape)


f, Pxx_den = signal.welch(x, fs, nperseg=2048)
f_med, Pxx_den_med = signal.welch(x, fs, nperseg=2048, average='median')

plt.figure()
#plt.semilogy(f, Pxx_den, label='mean')
plt.semilogy(f_med, Pxx_den_med, label='Raw median')
plt.xlabel('frequency [Hz]')
plt.ylabel('Power Spectral Density [V**2/Hz]')
plt.legend()
plt.show()

##lms PSD
y = array_lmssig
y += rng.normal(scale=np.sqrt(noise_power))#,size=time.shape)


##x[int(N//2):int(N//2)+10] *= 50.
f2, Pxx_den2 = signal.welch(y, fs, nperseg=2048)
f_med2, Pxx_den_med2 = signal.welch(y, fs, nperseg=2048, average='median')

##plt.semilogy(f, Pxx_den, label='mean')
plt.semilogy(f_med2, Pxx_den_med2, label='LMS median',color = 'orange')
plt.xlabel('frequency [Hz]')
plt.ylabel('Power Spectral Density [V**2/Hz]')
plt.legend()
plt.show()


#dnf PSD
z = array_dnfsig
z += rng.normal(scale=np.sqrt(noise_power))#,size=time.shape)


#x[int(N//2):int(N//2)+10] *= 50.
f3, Pxx_den3 = signal.welch(z, fs, nperseg=2048)
f_med3, Pxx_den_med3 = signal.welch(z, fs, nperseg=2048, average='median')

#plt.semilogy(f, Pxx_den, label='mean')
plt.semilogy(f_med3, Pxx_den_med3, label='DNF median',color = 'red')
plt.xlabel('frequency [Hz]')
plt.ylabel('Power Spectral Density [V**2/Hz]')
plt.legend()
plt.show()









