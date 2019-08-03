# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 00:54:31 2019

@author: olayi
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    low = 0
    high = len(aStr)
    mid = (low + high)//2
    if len(aStr) == 0 or len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    else:
        if char < aStr[mid]:
            high = mid
            return isIn(char,aStr[:mid])
        elif char > aStr[mid]:
            low = mid
            return isIn(char, aStr[mid+1:])
        else:
            return isIn(char, aStr[mid])
         
        mid = (low + high)//2

#aStr = 'abcdefghi'
char = 'r'
#char = 'j'
aStr = "acceghiijkmqtuvxyyyz"
print(isIn(char, aStr))