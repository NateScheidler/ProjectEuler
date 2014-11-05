# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 11:05:31 2014

@author: nscheidler
"""
import numpy as np

def sieve_of_eratosthenes(n):
	sieve = [True]*n
	sieve[0] = False
	sieve[1] = False
	for i in xrange(2,int(np.sqrt(len(sieve)))):
		if(sieve[i]):
			for p in xrange(i*i, n, i):
				sieve[p] = False
	return sieve

def count_circular_primes_less_than(n):
    primeSieve = sieve_of_eratosthenes(n)
    circPrimesCount = 0
    for i in range(0,n):
        if(primeSieve[i]): # if number is prime
            #check if circular
            numDigits = len(str(i))
            curCirc = str(i)
            flag = True
            for j in range(numDigits-1):
                rotatingDigit = curCirc[0]
                curCirc = curCirc[1:]+rotatingDigit
                if(primeSieve[int(curCirc)] != True):
                    flag = False
            if(flag):
                circPrimesCount += 1
    return circPrimesCount
    
print count_circular_primes_less_than(10**6)