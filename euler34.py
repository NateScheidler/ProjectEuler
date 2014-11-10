# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 15:41:01 2014

@author: nscheidler
"""
import math


factList = []
for i in range(10):
    factList.append(math.factorial(i))

def digit_factorial_sum(n):
    z=0
    for digit in str(n):
        z += factList[int(digit)]
    return z
ans = 0
for i in range(3,3*10**6):
    if i == digit_factorial_sum(i):
        print i
        ans += i
print ans