# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 03:25:03 2019

@author: olayi
"""

x = int(input('Enter the desired number: '))
root = int(input("square root - 2 or cube root - 3: "))
epsilon = 0.01
numguess = 0
if x < 0:
    low = x
    high = 0
else:
    low = 0
    high = x
    
ans = (high + low)/2.0

while abs(ans**root - x) >= epsilon:
    print('low = {} high = {} ans = {}'.format(low,high,ans))
    numguess += 1
    if ans**root < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
    
print('number of guess', numguess)
if root == 2:
    print("{} is close to square root of {}".format(ans, x))
else:
    print("{} is close to cube root of {}".format(ans, x))