# Euler 14

import numpy as np

def collatzLength(n):
	length = 1
	while (n != 1):
		length = length + 1
		if (n%2 == 0):
			n = n/2
		else:
			n = 3*n+1
	return length

maxLen = [1,1]

for i in xrange(1, 1000000):
	testLen = collatzLength(i)
	if (testLen > maxLen[0]):
		maxLen[0] = testLen
		maxLen[1] = i
		print i,testLen

print maxLen
