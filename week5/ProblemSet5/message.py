# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:06:15 2019

@author: olayi
"""
import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # cipher dict = cipher_dict
        self.cipher_dict = {}
        self.shift = shift
        # databank
        data = string.ascii_lowercase + string.ascii_uppercase
        if self.shift < 0 or self.shift > 26:
            raise ValueError("Incorrect value for Shift")
        # Creating a value
        invalid = string.punctuation + ' ' + string.digits
        for char in data:
            if char not in invalid:
                if char.isupper() == True:
                    databank = string.ascii_uppercase
                else:
                    databank = string.ascii_lowercase
                plain = databank.index(char)
                cipher = (self.shift + plain) % 26
                self.cipher_dict[char] =  databank[cipher]   
        return self.cipher_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #special char
        self.cipher_dict = self.build_shift_dict(shift)
        self.cipherText = ''
        invalid = string.punctuation + ' ' + string.digits
        for ch in self.message_text:
            if ch not in invalid:
                self.cipherText += self.cipher_dict[ch]
            
            else:
                self.cipherText += ch
        
        return self.cipherText
    
    
#Example test case (PlaintextMessage)
plain = 'we are taking 6.00.1x'
test = Message(plain)
shift = 2
print(test.apply_shift(shift))
#print(Message.build_shift_dict(test,shift))
#print('PlainText: ',plain)
#print('Expected Output: jgGnnq')
#print('Actual Output:', test.apply_shift(shift))