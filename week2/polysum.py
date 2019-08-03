# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:59:12 2019

@author: olayi
"""

# Import the math library housing the tan and pi function handle
from math import *

def polysum(n,s):
    """
    n,s: input 
    n: number of sides
    s: length of the side
    area: area of the polygon
    per: perimeter of the polygon 
    """
    area = 0.25 * n * (s**2)/tan(pi/n)
    per = n * s
    ans =  area + per**2
    return round(ans,4)
