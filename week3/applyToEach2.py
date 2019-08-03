# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:35:58 2019

@author: olayi
"""

def applyToEach2(j):
    '''
    j: entry data
    absolute: compute the one plus j
    out: positive format
    '''
    out = 1 + j
    return out

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
testList = [1, -4, 8, -9]
applyToEach(testList, applyToEach2)