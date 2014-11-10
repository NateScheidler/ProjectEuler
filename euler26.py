# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:15:53 2014

@author: nscheidler
"""

from decimal import *

for i in range(2,1000):
    if(len(str(decimal(1)/decimal(i)))) > 15:
        print i, 1.0/i


def cycleLength(fraction):
    curCycle = []
    for i in range(2,len(str(fraction))):
        print i
        