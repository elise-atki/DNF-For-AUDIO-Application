#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:09:06 2022

@author: elise
"""
import csv
import pandas as pd
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

#reads in .tsv and conversts to .csv in an array
tsv_file='weight_distance.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv("weight.csv",index=False)

array_weight = np.loadtxt("weight.csv", delimiter = ",", usecols = (0)) #loads in data file to float array 
print(array_weight)

sample_rate =441000

max_time1 = array_weight.size/sample_rate
time_steps1 = np.linspace(0,max_time1,array_weight.size)

plt.figure()
plt.plot(time_steps1,array_weight)
plt.title('Weight Distance')
plt.xlabel('Time [ms]')
plt.ylabel('Weight Distance')
plt.show()

