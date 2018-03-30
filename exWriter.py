# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 10:43:05 2018

@author: jonmi
"""

import csv

posStuff = []

with open('genome0.csv', 'r') as genomeFile:
    gReader = csv.reader(genomeFile)
    for row in gReader:
        helper = []
        for item in row:
            helper.append(item)
        posStuff.append(helper)
genomeFile.close()

with open('exampleGen.csv', 'w') as genFile:
    gr = csv.writer(genFile, quoting=csv.QUOTE_ALL)
    for i in range(0, 1080):
        smallrow = []
        for j in range(0, len(posStuff[i])):
            smallrow.append(posStuff[i][j])
        if i % 2 == 0:
            gr.writerow(smallrow)
genFile.close()