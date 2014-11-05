# PRIME GENERATORS
# these are fun!

import numpy as np

# Simple implimentation; checks all ints less than sqrt(n) every time

def naivePrimes(n):
	if (n < 2): return [1]
	primes = [1]
	for i in range(2,n):
		iIsPrime = True
		for j in range(1, len(primes)):
			if (primes[j] > np.sqrt(i)): break
			if (i%primes[j] == 0):
				iIsPrime = False
				break
		if (iIsPrime):
			primes.append(i)
	return primes

# Better implimentation; only checks against previously discovered primes
# Still prohibitively slow for primes > 10E5 or so

def doubleFrontPrimes(n):
	primes = [2,3,5]
	for i in range(7, n):
		add = True
		for j in range(0, len(primes)):
			if (i%primes[j] == 0):
				add = False
				break
			if (primes[j] > np.sqrt(i)): break
		if (add): primes.append(i)
		if (len(primes) == 10001):
			print i
			break
	return primes

# Sieve of Eratosthenes
# Does not generate list of primes, rather, it
# produces a binary list whose "True" entries are at prime indices
# Much much faster than either previous generator

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

p1e7 = sieveToArray(sieveOfEratosthenes(2000000))

z=0
for primes in p1e7:
   z+=primes

print z
    
print p1e7[1],p1e7[10000], p1e7[10001], p1e7[10002]
