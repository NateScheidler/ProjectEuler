# -*- coding: utf-8 -*-
"""
Created on Tue Nov 04 16:04:31 2014

@author: nscheidler
"""

def factorial(n):
    ret = 1
    for i in xrange(1,n+1):
        ret = ret*i
    return ret

largeNumber = factorial(100)

k = 0
for digit in str(largeNumber):
    k += int(digit)
print k
        