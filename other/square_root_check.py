# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 01:03:51 2019

@author: olayi
"""

ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True

while ans**2 < x:
    ans = ans + 1

if ans**2 == x:
    print("Square root of x", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean",-x,"?")