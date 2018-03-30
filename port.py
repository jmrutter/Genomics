# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:57:36 2018

@author: jonmi
"""

import h5py
import numpy as np
import math
import csv

filename = 'g2f_2014_zeagbsv27.raw.h5'

f = h5py.File(filename, 'r')

print("Keys: %s" % f.keys())

a_group_key = list(f.keys())


genotypes = list(f['Genotypes'].keys())

positions = list(f['Positions'].keys())

chrom = isinstance(f['Positions']['Chromosomes'], h5py.Dataset)

chromosomes = f['Positions']['Chromosomes']

print(chromosomes.size)


geno = f['Genotypes']['PHN11_Oh43_0075:100000004']


print(list(geno.keys()))

calls = geno['calls']
print(calls.size)

indexer = f['Genotypes']
multiIndex = []

'''

Letter                Corresponding Number
A     A:A             0
C     C:C             17
G     G:G             34
T     T:T             51
R     A:G             32 (2)
Y     C:T             19 (49)
S     C:G             33 (18)
W     A:T             3 (48)
K     G:T             35 (50)
M     A:C             1 (16)
+     +:+ (insertion) 
0     +:-             5 (53) (21) (37) (81) (80 - Light Blue) (82) (83)
-     -:- (deletion)  85
N     Unknown         -1  

'''
  
blockSize = 50000


lines = []

times = math.floor(calls.size / blockSize) + 1

for benchmark in range(0, times):
    writingInfo = []
    indexFriend = 0
    for i in range(0, blockSize):
        writingInfo.append([])
    print("Starting benchmark at: " + str(benchmark))
    for genome in indexer:
        print("Reading: " + genome)
        if genome != 'AlleleStates':
            exp = list(indexer[genome].keys())
            valid = False
            for v in exp:
                if v == 'calls':
                    valid = True
            if valid:
                if benchmark == 0:
                    lines.append([indexFriend, genome])
                    # data entry
                ind = indexer[genome]['calls'][()]
                print("Reading " + genome + " was successful!")
                end = (benchmark + 1) * blockSize
                if end > ind.size:
                    end = ind.size
                for i in range(benchmark * blockSize, end):
                    if ind[i] != -1:
                        writingInfo[i - benchmark * blockSize].append(str(indexFriend) + ": " + str(ind[i]))
                indexFriend = indexFriend + 1
            else:
                print("Genome is in different hierarchy.")
    filename = "genome" + str(benchmark) + ".csv"
    print("Writing: " + filename)
    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for i in range(0, len(writingInfo)):
            helper = i % 5000
            if helper == 0:
                print("Writing line: " + str(i))
            wr.writerow(writingInfo[i])
    myfile.close()


        