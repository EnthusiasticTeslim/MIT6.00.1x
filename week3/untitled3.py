#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:26:40 2019

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
    answer = list(secretWord)
    loc = 0
    for guess in lettersGuessed:
        if guess in secretWord:
            right.append(guess)
        else:
            wrong.append(guess)
    #print(right)
    #print(wrong)
    pick = []
    while loc < len(secretWord):
        for word in right:
            if word == secretWord[loc]:
                pick.append(secretWord[loc])
        loc += 1
    if pick == answer:
        return True
    else:
        return False