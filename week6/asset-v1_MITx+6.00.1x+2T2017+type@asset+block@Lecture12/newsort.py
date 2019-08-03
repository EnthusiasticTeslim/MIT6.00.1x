# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:27:22 2019

@author: olayi
"""

def newSort(L):
    for i in range(len(L) - 1):
        print(L)
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1