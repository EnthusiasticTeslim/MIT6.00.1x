# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    right = []
    wrong = []
    for guess in lettersGuessed:
        if guess in secretWord:
            right.append(guess)
        else:
            wrong.append(guess)
    #print(right)
    #print(wrong)
    pick = ""
    for word in secretWord:
        if word in right:
            pick += word
    if pick == secretWord:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guess += letter
        else:
            guess +='_'
    return guess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabets =  string.ascii_lowercase
    not_among = ""
    for letter in alphabets:
        if letter not in lettersGuessed:
            not_among += letter
    return not_among


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
    
    * Nomenclature:
        secretWord: The word to guess.
        lettersGuessed: The letters that have been guessed so far.
        mistakesMade: The number of incorrect guesses made so far.
        availableLetters: The letters that may still be guessed after removing the guess less from A-Z
    
    '''
    # FILL IN YOUR CODE HERE...

    lettersGuessed = ""
    correct = ""
    mistakesMade = ""
    TotalCount = 8
    print("Welcome to the game, Hangman!")
    wordlength = len(secretWord)
    #print("Secret word is {}".format(secretWord))
    print("I am thinking of a word that is {} letters long".format(wordlength))
    availableLetters = getAvailableLetters(lettersGuessed)
        
    print("-----------")
        
    print("You have {} guesses left".format(TotalCount))
        
    print("Available Letters: {}".format(availableLetters))
        
    
    while True:
               
        pick = input("Please guess a letter: ").lower()
             
        if pick in secretWord:
            if pick not in lettersGuessed:
                correct += pick
                print("Good guess:",getGuessedWord(secretWord, correct))
            else:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, correct))
        else:
            if pick in lettersGuessed:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, correct))
            else:
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord, correct))
            
            mistakesMade += pick
        print("-----------")
        
        final = getGuessedWord(secretWord, correct) 

       
        if TotalCount <= 1 or secretWord == final:
            if secretWord == final:
                print("Congratulations, you won!")
            else:
                print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
            break
        if pick in correct or pick in lettersGuessed:
            print("You have {} guesses left".format(TotalCount))
        else:
            if TotalCount > 1 and secretWord != final:
                TotalCount -=1
                print("You have {} guesses left".format(TotalCount))
                
        if pick in lettersGuessed:
            lettersGuessed = lettersGuessed
        else:
            lettersGuessed += pick       
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters: {}".format(availableLetters))


# (TotalCount >= 0 or secretWord != lettersGuessed)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
