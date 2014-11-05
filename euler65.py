# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 09:07:51 2014

@author: nscheidler
"""

# First, generate continued fraction for e

eContinuedFraction = [1]*100
eContinuedFraction[0] = 2
for i in range(0,100):
    if i % 3 == 2:
        eContinuedFraction[i] = 2*(i+1)/3




numerator = 1
denominator = eContinuedFraction[99]

for i in range(98,-1,-1):
    numerator += denominator*eContinuedFraction[i]
    temp = numerator
    numerator = denominator
    denominator = temp

temp = numerator
numerator = denominator
denominator = temp

sumDigits = 0
for digit in str(numerator):
    sumDigits += int(digit)
    
print sumDigits

print 28433*(2**7830457)+1