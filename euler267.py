# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 14:58:47 2014

@author: nscheidler
"""
"""
I figured most of this out on paper beforehand.
The contents of this file are just a tool for determining the max # of tails
and a quick calculation of the fraction of total scenarios that represents.

Pascal's triangle for the win!

Also, this is a bad way to play triple-or-nothing: choose f=0.25 instead.
Or f=1.0, and get a bajillion dollars once in a long while.
"""



import scipy.misc as sc



def flip(heads, f):
    z = 1
    for i in range(heads):
        z = z * (1 + 2*f)
    for i in range(1000-heads):
        z = z * (1 - f)
    return z

def minHeads(f):
    heads = 500
    minimum = False
    while(heads > 0 and minimum == False):
        cash = flip(heads, f)
        if cash < 10**9:
            minimum = True
            heads += 2
        heads -= 1
    return heads

#for f in np.arange(0.13,0.16,0.0001):
#    if minHeads(f) < 431: print "dude, yes"

# 431 is the smallest we can get at, sadly.
# We need to sum the 100th row of Pascal's triangle up through #431

numLosses = 0
for i in range(0,432):
    numLosses += sc.comb(1000,i)
totalTries = 2**1000

print (totalTries-numLosses)/(totalTries)