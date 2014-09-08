# Euler Project 49
import numpy as np
"""
The idea is:
First, find the 4-digit primes
Next, group them according to permutation
Finally, find the differences
"""

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

fourDigitPrimes = sieveToArray(sieveOfEratosthenes(10000))

a = [1,2,3,0]
b = sorted(a)
print b

def strip_down(a):
    return int("".join(sorted(str(a))))


def hash_up(a_list):
    n = len(a_list)
    table = {}
    for i in range(0,n):
        a_i = a_list[i]
        a_key = strip_down(a_i)
        if a_key in table:
            table[a_key].append(a_i)
        else:
            table[a_key] = [a_i]
    return table

def get_large_sets(hashT,n):
    for key in hashT:
        sortedVals = sorted(hashT[key])
        if len(sortedVals) >= n:
            dif = find_differences

def find_differences(orderedList):
    n = len(orderedList)
    dif = []
    for i in range(0,n):
        for j in range(0,i):
            dif.append(orderedList[i]-orderedList[j])
    return dif
    
print find_differences(b)










