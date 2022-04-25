#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:17:36 2022

@author: elise
"""

import csv
import pandas as pd
import numpy as np

voxdat = np.empty(0, dtype = 'float')
bassdat = np.empty(0, dtype = 'float')

voxsn = np.loadtxt("recording2voxs+n.dat")[:,1] #outer
print(voxsn)

bassn = np.loadtxt("recording2bassn.dat")[:,1] #inner
print(bassn)

voxdat = np.append(voxdat,voxsn)
bassdat = np.append(bassdat,bassn)

output = pd.DataFrame(voxdat,bassdat)
output.to_csv("rawp300t.csv")

#df = pd.read_csv('outer_file.csv', usecols = ['-0.0006103515625'], low_memory = False) !trying to select the column

#with df as csvin, open ('testtsvout.tsv', 'w') as tsvout:
 #   csvin = csv.reader(csvin)
  #  tsvout = csv.writer(tsvout, delimiter = '\t')

   # for row in csvin:
    #    tsvout.writerow(row)
    
with open('rawp300t.csv', 'r') as csvin, open ('rawp300t.tsv', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter = '\t')

    for row in csvin:
        tsvout.writerow(row)
