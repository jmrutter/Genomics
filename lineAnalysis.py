# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:37:48 2018

@author: jonmi
"""

"""
CSV Reader, classification
"""

import csv
import numpy as np

key = []

with open('genomeKey.csv', 'r') as gKeyFile:
    gkReader = csv.reader(gKeyFile)
    for row in gkReader:
        strHelper = []
        for item in row:
            strHelper.append(item)
        key.append(strHelper)
gKeyFile.close()
    
key[0][0] = "0"

abberations = np.zeros(shape=(1573))

internal = -1
for i in range(0, 16):
    filename = "variations" + str(i) + ".csv"
    print("Reading " + filename)
    fileContents = []
    with open(filename, 'r') as gDataFile:
        gdReader = csv.reader(gDataFile)
        for row in gdReader:
            strHelper = []
            for item in row:
                strHelper.append(item)
            fileContents.append(strHelper)
    gDataFile.close()
    for j in range(0, len(fileContents)):
        internal = internal + 1
        if (j + 1) % 50 == 0:
            print("Reading line " + str(j + 1))
        reference = internal / 2
        liner = fileContents[j]
        if j % 2 == 0:
            abberations[int(reference)] = len(liner)