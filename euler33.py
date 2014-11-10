# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 13:14:10 2014

@author: nscheidler
"""

def improper_cancellation(a,b):
    correctResult = (a+0.)/b
    a_s, b_s = str(a), str(b)
    if a_s[1] == 0 or b_s[1] == 0:
        return
    elif (a_s[0] == b_s[0]):
        a_fake = int(a_s[1])
        b_fake = int(b_s[1])
        fakeResult = (a_fake+0.)/b_fake
        if fakeResult == correctResult: print a,b
    elif (a_s[0] == b_s[1]):
        a_fake = int(a_s[1])
        b_fake = int(b_s[0])
        fakeResult = (a_fake+0.)/b_fake
        if fakeResult == correctResult: print a,b
    elif (a_s[1] == b_s[0]):
        a_fake = int(a_s[0])
        b_fake = int(b_s[1])
        fakeResult = (a_fake+0.)/b_fake
        if fakeResult == correctResult: print a,b
    elif (a_s[1] == b_s[1]):
        a_fake = int(a_s[0])
        b_fake = int(b_s[0])
        fakeResult = (a_fake+0.)/b_fake
        if fakeResult == correctResult: print a,b
            
for a in range(11,99):
    for b in range(a+1,99):
        improper_cancellation(a,b)