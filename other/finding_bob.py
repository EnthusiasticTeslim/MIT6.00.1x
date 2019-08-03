# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:03:14 2019

@author: olayi
"""
count = 0
s = 'azcbobobegghakl'
word = 'bob'
n = len(word)
m = len(s)
for i in range(m+1):
    if s[i:i+n] == word:
        count += 1

print(count)