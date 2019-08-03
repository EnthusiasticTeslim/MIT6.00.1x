# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:28:51 2019

@author: olayi
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # mapping the word entries to a dict
    entry = {}
    for x in word:
        entry[x] = entry.get(x,0) + 1
    print(entry)
    #creating a new dict with the remaining letters available for selection
    updated_entry = hand
    for keys,values in hand.items():
        if keys in word:
            check = values - entry[keys]
        else:
            check = values
        updated_entry[keys] = check
    return updated_entry
hand = {'k': 1, 'n': 2, 'o': 1, 't': 1, 'm': 1, 'b': 1, 'i': 1, 'l': 1}
word = 'milk'

print(updateHand(hand,word))