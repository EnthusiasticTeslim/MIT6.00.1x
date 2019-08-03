# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:01:10 2019

@author: olayi
"""

s = 'abcdefghijklmnoprstuvwxyz'
past = ''
present = ""
size = len(s)

for i in range(size):
    if i <= (size - 1):
        if s[i] >= s[i-1]:
            past += s[i]
        else:
            past = s[i]
        
        if len(past) > len(present):
            present = past
            
print("Longest substring in alphabetical order is: {}".format(present))
        