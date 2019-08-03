# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 02:09:18 2019

@author: olayi
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(10))
