# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:31:56 2019

@author: olayi
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    # Formula for triangular numbers
    #K =  n * (n + 1)/2
    status = False
    a = 1
    b = 1
    c = -2*k
    root = (b*b) - (4*a*c)
    import math 
    numer1 = -b + math.sqrt(root)
    numer2 = -b - math.sqrt(root)
    denom = 2*a
    val1 = numer1/denom
    val2 = numer2/denom
    if val1 == int(val1) and val2 == int(val2):
        status = True
    return status
    