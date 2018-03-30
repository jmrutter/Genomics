# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 09:29:53 2018

@author: jonmi
"""

"""
Histograms
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

frequencyLoci = []

with open("FrequencyLoci.csv", 'r') as fl:
    flReader = csv.reader(fl)
    for row in flReader:
        frequencyLoci.append(row[0])
fl.close()

freq = []

freq.append(48)

for i in range(1, len(frequencyLoci)):
    freq.append(int(frequencyLoci[i]))

"""
histograms = 100
num_bins = round(len(frequencyLoci) / histograms, 0)
for i in range(0, histograms):
    selection = []
    binsize = int(num_bins)
    if i < histograms - 1:
        start = num_bins * i
        end = num_bins * (i + 1)
        selection = freq[int(start):int(end)]
    else:
        start = num_bins * i
        selection = freq[int(start):]
        binsize = len(selection)
    n, bins, patches = plt.hist(selection, binsize, facecolor = 'blue', alpha = 0.5)
    plt.show()
"""
xcoord = []
for i in range(0, len(freq)):
    xcoord.append(i)
    
area = np.pi * .00002

chromosomePositions = [570, 148752, 115173, 108224, 94726, 110328, 76475, 80517, 81431, 72368, 67126]

plt.scatter(xcoord, freq, s=area, c=(0,0,0), alpha = 0.5)
plt.show()

area = np.pi * .2

for i in range(0, len(chromosomePositions)):
    print("Chromosome: " + str(i))
    if i > 0:
        area = np.pi * .002
    runningTotal = 0
    for j in range(0, i):
        runningTotal = runningTotal + chromosomePositions[j]
    xs = []
    ys = []
    end = runningTotal + chromosomePositions[i]
    for j in range(0, chromosomePositions[i]):
        xs.append(j)
    for j in range(runningTotal, end):
        ys.append(freq[j])
    plt.scatter(xs, ys, s=area, c=(0, 0, 0), alpha = 0.5)
    plt.show()
    
    
lineVariations = []

with open("LineVariat.csv", 'r') as lv:
    lvReader = csv.reader(lv)
    for row in lvReader:
        lineVariations.append(row[0])
lv.close()

lines = []

lines.append(586231)

for i in range(1, len(lineVariations)):
    lines.append(int(lineVariations[i]))
    
xco = []
for i in range(0, len(lines)):
    xco.append(i)

area = np.pi

plt.scatter(xco, lines, s=area, c=(0,0,0), alpha = 0.5)