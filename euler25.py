# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 16:17:04 2014

@author: nscheidler
"""

a = 1
b = 1
c = 2
while(True):
    a = b+a
    c += 1
    if len(str(a)) == 1000: break

    b = a+b
    c += 1
    if len(str(b)) == 1000: break
print c