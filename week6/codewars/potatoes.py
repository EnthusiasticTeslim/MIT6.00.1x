# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:25:58 2019

@author: olayi
"""

def potatoes(p0, w0, p1):
    '''
    int parameter p0 - initial percent of water
    int parameter w0 - initial weight
    int parameter p1 - final percent of water 
    '''
    # your code
    num = 100 - p0
    den = 100 - p1
    
    ratio = num/den
    
    return int(ratio * w0)