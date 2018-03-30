# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:28:24 2018

@author: jonmi
"""

import h5py
import numpy as np

filename = 'g2f_2014_zeagbsv27.raw.h5'

f = h5py.File(filename, 'r')

print("Keys: %s" % f.keys())

a_group_key = list(f.keys())


genotypes = list(f['Genotypes'].keys())

positions = list(f['Positions'].keys())

chrom = isinstance(f['Positions']['Chromosomes'], h5py.Dataset)

indices = f['Positions']['ChromosomeIndices']

external = 0
for ind in indices:
    external = external + 1
    print(ind)
    if external > 20:
        break





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

"""
posit = []
for i in range(0, calls.size):
    posit.append([[],[],[],[],[],[],[],[],[],[],[],[],[]])

for genome in indexer:
    print("Starting " + genome)
    exp = list(indexer[genome].keys())
    valid = False
    for v in exp:
        if v == 'calls':
            valid = True
    if valid:
        # data entry
        ind = indexer[genome]['calls']
        for i in range(0, ind.size):
            if ind[i] == 0:
                posit[i][0].append(genome)
            elif ind[i] == 17:
                posit[i][1].append(genome)
            elif ind[i] == 34:
                posit[i][2].append(genome)
            elif ind[i] == 51:
                posit[i][3].append(genome)
            elif ind[i] == 32 or ind[i] == 2:
                posit[i][4].append(genome)
            elif ind[i] == 19 or ind[i] == 49:
                posit[i][5].append(genome)
            elif ind[i] == 33 or ind[i] == 18:
                posit[i][6].append(genome)
            elif ind[i] == 3 or ind[i] == 48:
                posit[i][7].append(genome)
            elif ind[i] == 35 or ind[i] == 50:
                posit[i][8].append(genome)
            elif ind[i] == 1 or ind[i] == 16:
                posit[i][9].append(genome)
            elif ind[i] == 5 or ind[i] == 53 or ind[i] == 21 or ind[i] == 37 or ind[i] == 81 or ind[i] == 82 or ind[i] == 83 or ind[i] == 80:
                posit[i][10].append(genome)
            elif ind[i] == 85:
                posit[i][11].append(genome)
            elif ind[i] != -1:
                # list of other values, and their positions
                posit[i][12].append(genome + ": " + str(i) + ": " + str(ind[i]))
    else:
        print(genome + " has something up with it.")
        multiIndex.append(genome)
    print("Finishing " + genome)

"""
    
