# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:57:32 2019

@author: olayi
"""

def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowels = ['a','e','i','o','u']
    for alpha in inputStr:
        if alpha in vowels:
            num_vowels += 1
    
    return num_vowels



inputStr = 'kuvelmnoapi'

print(getCount(inputStr))