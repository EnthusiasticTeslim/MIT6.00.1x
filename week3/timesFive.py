# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 07:49:12 2019

@author: olayi
"""

def timesFive(a):
    return a * 5 

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
testList = [1, -4, 8, -9]
timesFive(testList)
#applyToEach(testList, timesFive)