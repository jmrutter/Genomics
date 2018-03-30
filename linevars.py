# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:27:50 2018

@author: jonmi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:28:24 2018

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

gen = isinstance(geno, h5py.Group)

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
blockSize = 100


times = math.floor(len(indexer) / blockSize) + 1

for i in range(0, times):
    internal = -1
    lines = []
    for genome in indexer:
        lineVar = []
        internal = internal + 1
        if internal < (i + 1) * blockSize and internal >= i * blockSize:
            print("Reading " + genome)
            if genome != 'AlleleStates':
                exp = list(indexer[genome].keys())
                valid = False
                for v in exp:
                    if v == 'calls':
                        valid = True
                if valid:
                    line = indexer[genome]['calls'][()]
                    print("Reading " + genome + " was successful.")
                    for j in range(0, len(line)):
                        if line[j] != -1:
                            lineVar.append(str(j) + ":" + str(line[j]))
                    lines.append(lineVar)
    filename = "variations" + str(i) + ".csv"
    print("Writing: " + filename)
    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for p in range(0, len(lines)):
            helper = p % 25
            if helper == 0:
                print("Writing line: " + str(p))
            wr.writerow(lines[p])
    myfile.close()
                        
    
"""
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
    
"""


        