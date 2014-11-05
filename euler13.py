# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 13:41:37 2014

@author: nscheidler
"""

# Euler Project no. 13


"""
We just need the first 13 or so digits of the numbers to sum them
and recover the first 10 correctly. Probably. 
"""

filepath = "C:\Users\NScheidler\Documents\large_numbers.txt"

curSum = 0
with open(filepath) as f:
    for line in f:
        a = int(line) / 10**39 # After some testing, this was the largest divisor I could get away with
        curSum += a

print curSum