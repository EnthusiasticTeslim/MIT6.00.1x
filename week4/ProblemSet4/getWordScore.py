# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:12:14 2019

@author: olayi
"""


# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    word_sum = 0
    bonus = 50
    if len(word) >= 1:
        for letter in word:
            db = SCRABBLE_LETTER_VALUES
            word_sum += db[letter]
        word_sum = word_sum * len(word)
        if len(word) == n:
            score = word_sum + bonus
        else:
            score = word_sum    
    else:
        score = 0
    
    return score




SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

word = ""
n = 7
print(getWordScore(word, n))