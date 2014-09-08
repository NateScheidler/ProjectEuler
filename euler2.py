# Euler Project 2

def fib_gen(maxVal):
	output = [1,2]
	nextVal = 3
	while nextVal < maxVal:
		output.append(nextVal)
		nextVal = output[len(output)-1] + output[len(output)-2]
	return output

fibList = fib_gen(4*10**6)
evenSum = 0
for i in range(1,len(fibList), 3):
    evenSum += fibList[i]

print evenSum