# Euler Project 3

import numpy as np
import time

startTime = time.clock()
def elapsed():
	return time.clock()-startTime

def naivePrimesLessThan(n):
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


def isPrimeToList(n, checkList):
	for i in range(1, len(checkList)):
		if (n%checkList == 0): return False
	return True

def smartPrimeHelper(primeList):
	maxPrime = primeList(len(primeList)-1)
	newPrimeList = list(primeList)
	for i in range(maxPrime, maxPrime**2):
		if (isPrimeToList(i, primeList)): newPrimeList.append(i)
	return newPrimeList

def smartPrimesLessThan(n):
	m = np.ceil(np.log2(len(str(n))))
	primeList = naivePrimesLessThan(int(np.power(n, 1/(2*m))))
	_primeList = list(primeList)
	while(m > 1):
		m = m - 1
		_primeList = smartPrimeHelper(primeList)
		primeList = list(_primeList)
	




# the PrimesLessThan function takes a rather long time (~1 min for n = 300k).
# It would be perhaps more useful to check each factor of z individually

def isPrime(n):
	cL = naivePrimesLessThan(int(np.sqrt(n)))
	for i in range(1,len(cL)):
		if (n%cL[i] == 0): return False
	return True

print isPrime(73)

z_ = 600851475143
z = 1234567
smartPrimesLessThan(z_)

factorList = []
nextPrime = 2

while (False):
	for i in range(nextPrime, z+1):
		if (z%i == 0):
			factorList.append(i)
			z = z/i
			nextPrime = i
			break
		print z

