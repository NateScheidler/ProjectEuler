# euler NUM

import numpy as np

def erat(n):
	primes = [True]*n
	primes[0] = False
	primes[1] = False
	for i in xrange(2,int(np.sqrt(n))):
		if (primes[i]):
			for j in xrange(i**2, n, i):
				primes[j] = False
	prim = []
	for i in xrange(0, n):
		if(primes[i]):
			prim.append(i)
	return prim

def countDivs(primeList):
	numDivs = 1
	i = 0
	while(i < len(primeList)):
		cur = primeList[i]
		numCur = primeList.count(primeList[i])
		numDivs = numDivs*(numCur+1)
		i = i + numCur
	return numDivs

def primeFactors(n):
	pL = erat(n)
	pFL = []
	m = int(n)
	i = 0
	while(i < len(pL)):
		if (m%pL[i] == 0):
			pFL.append(pL[i])
			m = m/pL[i]
		else: i = i + 1
	if (len(pFL) == 0):
		pFL = [n]
	return pFL

def tri(n):
	return (n*(n+1))/2

k = 76576500
v = countDivs(primeFactors(tri(k)))
w = countDivs(primeFactors(tri(k-1)))

print v
print w
