# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 01:53:43 2019

@author: olayi
"""

num = 11

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
    
result = ""
if num == '0':
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

if isNeg:
    result = "-" + result
    
print(result)