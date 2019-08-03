# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 02:29:04 2019

@author: olayi
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    answer = 1
    while exp > 0:
        answer *= base
        exp -= 1
        
    return answer

print(iterPower(2,3))