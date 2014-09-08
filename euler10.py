# Euler 9

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

pr = sieveOfEratosthenes(2000000)

sumPrimes = 0

def printPrimes(sieve):
	for i in xrange(0, len(sieve)):
		if (sieve[i]): print i

for i in xrange(0, len(pr)):
	if (pr[i]): sumPrimes = sumPrimes + i

print sumPrimes
