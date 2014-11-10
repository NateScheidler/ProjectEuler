# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 17:04:35 2014

@author: nscheidler
"""

"""
I really need a better algorithm for this, it took like 5 minutes
The get_divisor_list can certainly be improved, it takes ~30 sec

Technically, it does get the answer: 4179871

"""

def get_divisor_list(n):
    divisorList = []    
    for i in range(1,n/2+1):
        if n % i == 0:
            divisorList.append(i)
    return divisorList


def g(x):
    return (x**2+1)

def gcd(a,b):
    while a != b:
        dif = abs(a-b)
        if a > b:
            a -= dif
        else:
            b -= dif
    return a

print gcd(5,3)
    
def rho_algorithm(n):
    x,y,d = 2,2,1
    while(d == 1):
        x = g(x)
        y = g(g(y))
        d = gcd(abs(x-y),n)



abundantNumbers = []
for i in range(0,28123):
    if i < sum(get_divisor_list(i)):
        abundantNumbers.append(i)

ans = 0
for i in range(0,28123):
    abundantSum = False
    j = 0    
    while(abundantNumbers[j] < i and j < len(abundantNumbers)/2):
        if (i - abundantNumbers[j]) in abundantNumbers:
            abundantSum = True
            break
        j += 1
    if(abundantSum != True):
        ans += i
    print i

print ans