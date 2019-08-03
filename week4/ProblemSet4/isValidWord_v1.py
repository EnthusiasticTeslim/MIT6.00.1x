# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:31:06 2019

@author: olayi

FAILURE: test_isValidWord()
        Expected False, but got True for word: 'rapture' and hand: {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
FAILURE: test_isValidWord()
        Expected False, but got True for word: 'honey' and hand: {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}
FAILURE: test_isValidWord()
        Expected False, but got True for word: 'even' and hand: {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
        (If this is the only failure, make sure isValidWord() isn't mutating its inputs)
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    if word not in wordList:
        return False
    hand_cp = hand.copy()
    for letter in word:
        if letter not in hand:
            return False
        if letter in hand:
            hand_cp[letter] -= 1
        if hand_cp[letter] < 0:
            return False
    
    return True

word = 'even'
hand = {'e': 2, 'v': 2, 'n': 1, 'i': 1, 'l': 2} 
print(isValidWord(word, hand, wordList))