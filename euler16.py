# Euler 16

def toArray(n):
	m = len(str(n))
	charray = []
	for i in range(0,m):
		q = n/(10**(m-i-1))
		charray.append(q)
		n = n - q*10**(m-i-1)
	return charray

vln = toArray(2**1000)

k = 0
for i in xrange(0,len(vln)):
	k = vln[i] + k
print k
