# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:27:27 2019

@author: olayi
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    '''
    cipher("abcd", "dcba", "dab")  --- ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
    '''
    key_code = {}
    decoded = ''
    if len(map_from) != len(map_to):
        raise ValueError("Two unmatched strings")
    
    length = len(map_from)
    
    #mappind the two strings
    for loc in range(length):
        key_code[map_from[loc]] = map_to[loc]
    
    # Decoding the code using the dict
    for char in code:
        try:
            decoded += key_code[char]
        except KeyError:
            raise KeyError("Dictionary has no keys or values")
        
    return (key_code, decoded)
        