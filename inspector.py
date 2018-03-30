# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:08:25 2018

@author: jonmi
"""

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

mapped = [0, 17, 34, 51, 2, 32, 19, 49, 18, 33, 3, 48, 35, 50, 1, 16, 5, 53, 21, 37, 81, 80, 82, 83, 85, -1]

lines = []

times = math.floor(len(indexer) / blockSize) + 1

for i in range(0, times):
    internal = -1
    for genome in indexer:
        internal = internal + 1
        if internal < (i + 1) * blockSize:
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
                        newChar = True
                        for k in range(0, len(mapped)):
                            if line[j] == mapped[k]:
                                newChar = False
                        if newChar:
                            print("Found: " + str(line[j]) + " at " + genome + " position " + str(j))