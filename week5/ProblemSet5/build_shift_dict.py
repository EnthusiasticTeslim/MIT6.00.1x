# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:10:45 2019

@author: olayi
"""
import string

def build_shift_dict(get_valid_word, shift):
    '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
    '''
    # cipher dict = cipher_dict
    cipher_dict = {}
    invalid = string.punctuation + ' ' + string.digits
    if shift < 0 or shift > 26:
        raise ValueError("Incorrect value for Shift")
    # Creating a value
    for char in get_valid_word:
        if char not in invalid:
            if char.isupper() == True:
                databank = string.ascii_uppercase
            else:
                databank = string.ascii_lowercase
        
            plain = databank.index(char)
            cipher = (shift + plain) % 26
            cipher_dict[char] =  databank[cipher]   
    return cipher_dict


get_valid_word = 'Da,Ta'
shift = 3
print(build_shift_dict(get_valid_word, shift))
