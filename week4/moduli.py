# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 07:43:20 2019

@author: olayi
"""

def f(n):
    '''
    n: integer, n >= 0 
    '''
    if n == 0:
        return (n + 1)
    else:
        return n * f(n - 1)

print(f(3))
print(f(1))
print(f(0))