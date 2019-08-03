# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 07:33:54 2019

@author: olayi
"""

def applyToEach1(j):
    '''
    j: entry data
    absolute: compute the absolute value of inp
    out: positive format
    '''
    if j >= 0:
        return j
    else:
        return -1*j

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
testList = [1, -4, 8, -9]
applyToEach(testList, applyToEach1)

            