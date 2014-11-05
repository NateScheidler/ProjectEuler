# -*- coding: utf-8 -*-
"""
Created on Tue Nov 04 15:01:51 2014

@author: nscheidler
"""
"""
Slow solution. Takes ~2 min to solve.
Should impliment way to check if we already know that a number leads to 89 or 1
Probably double-cover a lot of ground.

ANS k = 8581146

"""

def chain_check(i):
    while(i!=1 and i!=89):
        j = 0
        for digit in str(i):
            j+=int(digit)**2
        i = j
    if i == 1:
        return 1
    if i == 89:
        return 89


k = 0
for i in range(1,10**7):
    if chain_check(i) == 89:
        k+=1
    if i % 10**5 == 0:
        print i/10**6
print k