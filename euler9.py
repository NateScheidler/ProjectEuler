# Euler 9

import numpy as np

def isPythagoreanTriple(a,b,c):
	return a**2+b**2 == c**2

for i in range(1,1000):
	for j in range(1,1000-i):
		k = 1000-i-j
		if(isPythagoreanTriple(i,j,k)): print i, j, k, i*j*k
