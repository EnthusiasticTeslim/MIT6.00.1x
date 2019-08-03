# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:53:34 2019

@author: olayi
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    dimension: A dictionary, wehre the size are stored
    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    dimension = {}
    for name in aDict:
        size = len(aDict[name])
        dimension[name] = size
        
        
    return max(dimension)


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'],'d': ['donkey','dog','dingo']}
print(biggest(animals))