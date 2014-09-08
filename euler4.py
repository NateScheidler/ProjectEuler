import numpy as np

def toArray(n):
	m = len(str(n))
	charray = []
	for i in range(0,m):
		q = n/(10**(m-i-1))
		charray.append(q)
		n = n - q*10**(m-i-1)
	return charray

print toArray(15432)

def isPalindrome(n):
	arr = toArray(n)
	l = len(arr)
	for i in range(0, l/2):
		if (arr[i] != arr[l-i-1]): return False
	return True

for i in range (900, 999):
	for j in range(900, 999):
		if (isPalindrome(i*j)): print i, j, i*j	
