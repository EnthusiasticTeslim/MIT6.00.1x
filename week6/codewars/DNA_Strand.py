# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:52:21 2019

@author: olayi
"""

def DNA_strand(dna):
    DNA = ''
    for char in dna:
        if char == 'A':
            DNA += 'T'
        elif char == 'T':
            DNA += 'A'
        elif char == 'G':
            DNA += 'C'
        else:
            DNA += 'G'
    return DNA
             