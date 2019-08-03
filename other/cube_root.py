# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 01:58:47 2019

@author: olayi
"""

cube = int(input("Enter the desired number: "))
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guess = 0

while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guess += 1
    
print("number of guesses =", num_guess)
if abs(guess**3 - cube)>= epsilon:
    print("failed on the Cube root of", cube)
else:
    print(guess,"is close to the cube root of",cube)