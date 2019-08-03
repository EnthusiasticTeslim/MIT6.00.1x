# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:43:48 2019

@author: olayi
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        init_d = a
    else:
        init_d = b
    
    while a%init_d != 0 and b%init_d != 0:
        if init_d > 0:
            init_d -= 1
    
    if init_d%2 == 0:
        init_d = 2
    elif init_d%3 == 0:
        init_d = 2
    
    return init_d


print(gcdIter(9,8))
        
    