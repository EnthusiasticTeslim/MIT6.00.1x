#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:58:11 2019

@author: teslim
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    lettersGuessed = ""
    correct = ""
    mistakesMade = ""
    TotalCount = 8
    print("Welcome to the game, Hangman!")
    wordlength = len(secretWord)
    print("Secret word is {}".format(secretWord))
    print("I am thinking of a word that is {} letters long".format(wordlength))

    
    
    while True:
        availableLetters = getAvailableLetters(lettersGuessed)
        
        print("-------------")
        
        print("You have {} guesses left.".format(TotalCount))
        
        print("Available letters: {}".format(availableLetters))
        
        pick = input("Please guess a letter: ").lower()
             
                
        if pick in secretWord:
            if pick not in lettersGuessed:
                correct += pick
                print("Good guess:",getGuessedWord(secretWord, correct))
        else:
            if pick in lettersGuessed:
                print("Oops! You've already guess that letter:",getGuessedWord(secretWord, correct))
            else:
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord, correct))
            
            mistakesMade += pick
        
        if pick in lettersGuessed:
            lettersGuessed = lettersGuessed
        else:
            lettersGuessed += pick
            
            
        if pick in secretWord:
            print("You have {} guesses left.".format(TotalCount))
        else:
            TotalCount -=1
            print("You have {} guesses left.".format(TotalCount))
        
        
        final = getGuessedWord(secretWord, correct)
        #print(final)
        if TotalCount <= 0 or secretWord == final:
            print("-------------")
            if secretWord == final:
                print("Congratulations, you won!")
            else:
                print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
            break
            