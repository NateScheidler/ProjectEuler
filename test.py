# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:15:53 2014

@author: nscheidler
"""

n = 2**1000
digits = str(n)
z = 0
for digit in digits:
    z += int(digit)
print z