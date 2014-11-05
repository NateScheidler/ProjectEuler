# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 10:04:45 2014

@author: nscheidler
"""

"""
We need to calculate 28433×2^7830457+1, which is a REALLY big number.
I tried to calculate it straight up, and it crashed spyder (haha).

But we only need the last 10 digits.

Every digit before the last 10 won't ever influence the previous digits
the next time you multiply by 2, because they're already... You get it.
So this is pretty easy, really.

answer = 8739992577

"""

exponent = 7830457
multiplier = 28433

def last_ten_digits_calculator(n, k):
    ans = n
    for i in range(1,k):
        ans = (ans * n) % 10**10
    return ans
    
print (last_ten_digits_calculator(2,exponent)*multiplier + 1) % 10**10