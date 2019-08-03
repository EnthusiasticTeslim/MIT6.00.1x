# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 02:44:23 2019

@author: olayi
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return (base * recurPower(base, exp - 1))
    


print(recurPower(5,4))