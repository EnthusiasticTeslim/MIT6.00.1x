# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 21:55:23 2019

@author: olayi
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    odd = ()
    length = len(aTup)
    for loc in range(length):
        if loc % 2 == 0:
            odd += (aTup[loc],)
    return odd

aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))
            