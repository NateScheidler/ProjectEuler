# Euler 13

import numpy as np

data = np.loadtxt('euler13_data.txt')

chop = 10**33
print chop
dataSum = 0
for i in xrange(0, len(data)):
	data[i] = data[i] / chop
	print data[i]
	dataSum = dataSum + data[i]

print dataSum
