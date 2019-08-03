# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:41:30 2019

@author: olayi
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    value = 0
    for key in animals:
        if len(animals[key]) == 1:
            value += 1
        else:
            for j in animals[key]:
                value += 1
                
                
    return value


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'],'d': ['donkey','dog','dingo']}
print(how_many(animals))