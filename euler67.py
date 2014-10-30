# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 17:19:22 2014

@author: nscheidler
"""

import numpy as np

filepath = "C:\Users\NScheidler\Documents\Python Scripts\New Folder\ProjectEuler\giant_tri.txt"

last_line = []
with open(filepath) as f:
    for line in f:
        cur_line = np.array(line.split()).astype(np.int)
        n = len(cur_line)
        
        if n == 2:
            cur_line[0] = cur_line[0] + last_line[0]
            cur_line[1] = cur_line[1] + last_line[0]   
        elif n > 2:
            cur_line[0] += last_line[0]
            cur_line[n-1] += last_line[n-2]
            for i in xrange(1,n-1):
                l,r = last_line[i-1], last_line[i]
                cur_line[i] = cur_line[i] + (l if l > r else r)
        
        last_line = cur_line
        
last_line = np.sort(last_line)
print last_line[len(last_line)-1]