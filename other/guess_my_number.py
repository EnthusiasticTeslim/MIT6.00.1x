# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 00:02:25 2019

@author: olayi
"""

print("Please think of a number between 0 and 100!")
minim = 0
maxim = 100
diff = 0

guess = (minim + maxim)/2
while True:
    print("Is your secret number {}".format(guess))
    indicator = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if indicator == "l":
        minim = guess
    elif indicator == "h":
        maxim = guess
    elif indicator == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
    
    guess = int((minim + maxim)/2)
    
print("Game over. Your secret number was: {}".format(guess))
    