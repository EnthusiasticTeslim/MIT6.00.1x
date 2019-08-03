#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:02:40 2019

@author: teslim
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    right = []
    wrong = []
    for guess in lettersGuessed:
        if guess in secretWord:
            right.append(guess)
        else:
            wrong.append(guess)
    #print(right)
    #print(wrong)
    pick = ""
    for word in secretWord:
        if word in right:
            pick += word
    if pick == secretWord:
        return True
    else:
        return False
secretWord = 'mechanical'
lettersGuessed = ['m', 'e', 'c', 'h', 'a', 'n', 'i', 'c', 'a', 'l']

print(isWordGuessed(secretWord, lettersGuessed))