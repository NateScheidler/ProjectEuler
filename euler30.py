# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 13:49:35 2014

@author: nscheidler
"""
import numpy as np

# look! Calculate these beforehand to save a little computation
fpowSinglets = np.array([0,1,2,3,4,5,6,7,8,9])**5


print fpowSinglets


# Right about here is where I abandon all pretense of
# naming conventions
def fpow_check(n):
    n_str = str(n)
    cur_sum = 0  
    for ch in n_str:
        cur_sum += fpowSinglets[int(ch)]
    return (cur_sum == n)


i_sum = 0
for i in range(2,1000000):
    if (fpow_check(i)):
        print i
        i_sum += i
print i_sum
        