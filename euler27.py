# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 12:40:19 2014

@author: nscheidler
"""

"""
Clumsy, but it does work.
Answer is 71 primes, with a = -61, b  = 971

You can terminate the program manually with control+c before you search over 
th whole answer space.
"""


import numpy as np

def sieveOfEratosthenes(n):
	sieve = [True]*n
	sieve[0] = False
	sieve[1] = False
	for i in xrange(2,int(np.sqrt(len(sieve)))):
		if(sieve[i]):
			for p in xrange(i*i, n, i):
				sieve[p] = False
	return sieve

def sieveToArray(sieve):
	z = []
	for i in xrange(0,len(sieve)):
		if(sieve[i]):
			z.append(i)
	return z
 
primeList = sieveToArray(sieveOfEratosthenes(10**5))

def number_of_consecutive_primes(a,b):
    n = 0
    while(n**2+a*n+b in primeList):
        n += 1
    return n

curMax = 0
for a in range(-1000,1000):
    for b in range(-a,1000):
        this_primes = number_of_consecutive_primes(a,b)
        if this_primes > curMax:
            curMax = this_primes
            print curMax,a,b
    if a%200 == 0:
        print a/20, "% done"