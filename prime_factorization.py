# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 11:33:31 2014

@author: nscheidler
"""
"""
NOTE: Does not actually work.
In fact, will crash most of the time. Need to work out infinite loop issue
"""

def g(x):
    return (x**2+1)

def gcd(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
  
def rho_algorithm_step(n):
    x,y,d = 2,2,1
    while(d == 1):
        x = g(x) % n
        y = g(g(y) % n) % n
        d = gcd(abs(x-y),n)
    if d == n:
        return -1
    else: return d

def rho_algorithm(n):
    ret = []
    isPrime = False
    while(isPrime == False):
        primeFactor = rho_algorithm_step(n)
        if primeFactor > 0:
            ret.append(primeFactor)
        else: 
            isPrime = True
            ret.append(n)
        n = n/primeFactor
    return ret

print rho_algorithm(877)