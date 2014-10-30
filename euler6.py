# Euler 6

import matplotlib.pyplot as plt

sqList = []
cbList = []
sumSqList = []
diffList = []

sz = 30

for i in range(1,sz+1):
	sqList.append(i*i)
	cbList.append(i*i*i)


sqSum = 0
for i in range(0,sz):
	sqSum = sqSum + sqList[i]
	sumSqList.append(sqSum)

print sumSqList
for i in range(0,sz):
	diffList.append(cbList[i] - sumSqList[i])

print diffList

def diff(x):
	return x**3 

sumsq = 0
for i in range(0,101):
    sumsq += i**2

sqsum = 5050**2 # 

print sqsum - sumsq


plt.plot(diffList)
plt.show()

# Used first 4 vals from diffList to find third degree polynomial for sum(n**2)
