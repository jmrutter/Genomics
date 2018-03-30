# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

chromosomes = f['Positions']['Chromosomes']

print(chromosomes.size)

geno = f['Genotypes']['PHN11_Oh43_0075:100000004']

gen = isinstance(geno, h5py.Group)

print(list(geno.keys()))

calls = geno['calls']
print(calls.size)

for i in range(0, calls.size):
    t = calls[i]
    if t != -1:
        if t != 0:
            if t != 17:
                if t != 34:
                    if t != 51:
                        if t != 32:
                            if t != 19:
                                if t != 33:
                                    if t != 3:
                                        if t != 35:
                                            if t != 2:
                                                if t != 49:
                                                    if t != 18:
                                                        if t != 48:
                                                            if t != 50:
                                                                if t != 1:
                                                                    if t != 16:
                                                                        if t != 21:
                                                                            if t != 37:
                                                                                if t != 85:
                                                                                    if t != 5:
                                                                                        if t != 80:
                                                                                            if t != 82:
                                                                                                if t != 83:
                                                                                                    if t != 53:
                                                                                                        if t != 81:
                                                                                                            line = t
                                                                                                            print(str(line) + ": " + str(i))
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
'''
ind = geno['CML343-B-B-B-B-B-B)-B-B-1-1-B-B-B-1-B12-1-B21:100000971']
print(list(ind.keys()))

calls = ind['calls']

print(calls.size)

print(ind['depth'].size)
depth = ind['depth']

d = isinstance(depth, h5py.Dataset)
print(depth[0].size)
for i in range(0, depth[0].size):
    if depth[0][i] != 0:
        print(i)
'''
