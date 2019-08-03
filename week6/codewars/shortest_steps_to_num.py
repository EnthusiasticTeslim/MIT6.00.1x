# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 18:38:51 2019

@author: olayi
"""

def shortest_steps_to_num(num):
    # Good Luck!
    if num < 1 or num > 10000:
        raise ValueError("Verify your input")
        
    trans = 1
    count = 0
    while trans < num:
        trans += trans
        count += 1
        
    return '{0} steps'.format(count)
    