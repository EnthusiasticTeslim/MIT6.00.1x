# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:49:53 2019

@author: olayi
"""

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        print(i,L[size-i-1])
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

def search(L, e):
    for i in range(len(L)):
        print(L[i])
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


testList = [1,2,3,5,7,9,18,27]