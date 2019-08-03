# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:53:38 2019

@author: olayi
"""

def fib(n):
    """
    int n: number of occurences
    fib: name of the model i.e. Fibonnaci
    fib returns the Fibonnaci of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(5))