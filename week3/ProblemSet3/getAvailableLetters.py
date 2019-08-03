#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:54:23 2019

@author: teslim
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabets =  string.ascii_lowercase
    not_among = ""
    for letter in alphabets:
        if letter not in lettersGuessed:
            not_among += letter
    return not_among


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print(getAvailableLetters(lettersGuessed))