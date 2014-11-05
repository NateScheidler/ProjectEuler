# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 16:51:40 2014

@author: nscheidler
"""
"""
Simple problem, but note that 8128 is self-amicable!
That's pretty neat.
"""


def get_divisor_list(n):
    divisorList = []    
    for i in range(1,n/2+1):
        if n % i == 0:
            divisorList.append(i)
    return divisorList

ans = 0
for i in range(0,10000):
    divisorList = get_divisor_list(i)
    amicablePair = sum(divisorList)
    amicableDivisorList = get_divisor_list(amicablePair)
    if(sum(amicableDivisorList) == i and i != amicablePair):
        ans += i

print ans