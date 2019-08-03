# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:04:51 2019

@author: olayi
"""
import string
def number():
    digit = list(string.digits)
    del digit['0']
    return digit

def order(sentence):
    if sentence == '':
        word = ''
    else:
        word = sorted(sentence, key = number for val in digit)
    return word
    
  