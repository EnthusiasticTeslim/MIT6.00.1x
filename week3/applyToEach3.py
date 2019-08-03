# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:39:02 2019

@author: olayi
"""

def applyToEach3(j):
    '''
    j: entry data
    absolute: compute the one plus j
    out: positive format
    '''
    out = j**2
    return out

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
testList = [1, -4, 8, -9]
applyToEach(testList, applyToEach3)