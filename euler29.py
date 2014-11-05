# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 09:56:56 2014

@author: nscheidler
"""


# Calculates number of distinct factors of an integer
# Does not count the integer itself and 1 as factors
def countFactors(n):
    numFactors = 0
    for i in range(2,n/2+1):
        if n%i == 0:
            numFactors += 1
    return numFactors

# Summing up all these distinct factors yields the number
# of repeated spots in a grid of a^b vs b^a
numRepeats = 0
for i in range(2,5):
    numRepeats += countFactors(i)
print numRepeats

print 16 - numRepeats
# Never mind, this doesn't work
# Putting a pin in it.