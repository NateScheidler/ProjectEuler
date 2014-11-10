# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:23:52 2014

@author: nscheidler
"""
import csv
import numpy as np

filepath = "C:\Users\NScheidler\Documents\Python Scripts\ProjectEuler\p022_names.txt"

print ord("A")


with open(filepath) as f:
    fileReader = csv.reader(f, delimiter = ',',)
    nameList = []
    for name in fileReader:
        nameList = name # not exactly sure why only iterates once, but whatever

nameList = np.sort(nameList)

def value(word):
    z = 0
    for characters in word:
        z += ord(characters) - 64
    return z


ans = 0
for i in range(len(nameList)):
    ans += (i+1)*value(nameList[i])
    if nameList[i] == "COLIN":
        print "COLIN :", (i+1)*value(nameList[i]), i
    
print ans