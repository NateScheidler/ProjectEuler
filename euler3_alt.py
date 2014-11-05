# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 11:36:07 2014

@author: nscheidler
"""

#Euler 3 ALT
"""
My other solution to Euler 3 was really old, and I wrote it before I knew about
non-stupid ways to calculate prime numbers.
Here is an actually decent solution.
"""
import numpy as np

k = 600851475143

def sieveOfEratosthenes(n):
	sieve = [True]*n
	sieve[0] = False
	sieve[1] = False
	for i in xrange(2,int(np.sqrt(len(sieve)))):
		if(sieve[i]):
			for p in xrange(int(i*i), int(n), i):
				sieve[p] = False
	return sieve

def sieveToArray(sieve):
	z = []
	for i in xrange(0,len(sieve)):
		if(sieve[i]):
			z.append(i)
	return z

p_list = sieveToArray(sieveOfEratosthenes(np.sqrt(k)))

for p in p_list:
    if (k % p == 0):
        k = k/p
        print p