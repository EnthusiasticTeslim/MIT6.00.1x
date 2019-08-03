# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:00:47 2019

@author: olayi
"""

def setDummyHand(handString):
    '''
    Allows you to set a dummy hand. Useful for testing your implementation.
    
    handString: A string of letters you wish to be in the hand. Length of this
    string must be equal to self.HAND_SIZE.
    This method converts sets the hand attribute to a dictionary
    containing the letters of handString.
    '''
    assert len(handString) == HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), HAND_SIZE)
    hand = {}
    for char in handString:
        print(char)
        hand[char] = hand.get(char, 0) + 1
        print(hand)



HAND_SIZE = 7
setDummyHand('aazzmsp')

print("\n")
print(myHand)
            