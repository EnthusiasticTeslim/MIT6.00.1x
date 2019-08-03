#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:42:25 2019

@author: teslim
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guess += letter
        else:
            guess +='_'
    return guess
    
    
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print(getGuessedWord(secretWord, lettersGuessed))