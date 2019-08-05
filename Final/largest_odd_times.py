# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:41:00 2019

@author: olayi
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None 
    """
    assert len(L) > 0
    freq = {}
    largest = 0
 
    for val in L:
        freq[val] = freq.get(val,0) + 1
    
    for key,value in freq.items():
        if value%2 != 0 and int(key) > largest:
            largest = int(key)
    if largest == 0:
        largest = None
        
    return largest
    



#largest_odd_times([2,2,4,4]) returns None
# largest_odd_times([3,9,5,3,5,3]) returns