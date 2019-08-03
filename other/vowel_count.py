# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:40:11 2019

@author: olayi
"""
count = 0
s = 'azcbobobegghakl'
for let in s:
    if let == 'a' or let == 'e' or let == 'i' or let == 'o' or let == 'u':
        count += 1
        
print(count)