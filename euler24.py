# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 11:00:14 2014

@author: nscheidler
"""
import math

digitList = [0,1,2,3,4,5,6,7,8,9]
nthPermutation = []

"""
We are going to take numbers from digitList and append them to nthPermuatation
as the algorithm progresses.
"""

currentDesiredPermutation = 10**6-1

for i in range(10):
    # First, we need to figure out which digit comes next
    currentFactorial = math.factorial(len(digitList)-1)
    nextDigitIndex = currentDesiredPermutation/currentFactorial
    q = digitList[nextDigitIndex]
    digitList.remove(q)
    nthPermutation.append(q)
    currentDesiredPermutation -= currentFactorial*nextDigitIndex

print nthPermutation