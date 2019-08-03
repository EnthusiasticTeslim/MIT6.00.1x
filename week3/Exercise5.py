# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:57:42 2019

@author: olayi
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], 3.0))
print(applyEachTo([inc, int], -3))

