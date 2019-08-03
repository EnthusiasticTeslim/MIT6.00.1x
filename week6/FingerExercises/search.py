# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 13:27:12 2019

@author: olayi
"""

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

testList = [1,2,3,5,7,9,18,27]