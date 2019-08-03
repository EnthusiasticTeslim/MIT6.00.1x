# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:14:14 2019

@author: olayi
"""

def nb_year(p0, percent, aug, p):
    # your code
    n = 0 
    while True:
        p0 = p0 + (percent/100) * p0 + aug
        n += 1
        
        if p0 > p:
            break
    return n
        
print(nb_year(150000, 2.5, 1000, 200000))