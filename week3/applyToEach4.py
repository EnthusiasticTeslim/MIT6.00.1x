# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:41:02 2019

@author: olayi
"""

def applyToEach4(j):
    '''
    j: entry data
    absolute: compute the one plus j
    out: positive format
    '''
    if j >= 0:
        out = j**3
    else:
        out = -1 * j**3
    return out

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
testList = [1, -4, 8, -9]
applyToEach(testList, applyToEach4)