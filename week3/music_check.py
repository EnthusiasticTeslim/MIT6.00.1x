# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:29:02 2019

@author: olayi
"""

'''
lyrics: musical lyrics; more of a list of strings
lyrics_to_frequencies: Creating dictonary
most_common_words: Using the dictionary
words_often: Leveraging dictionary properties
'''
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words,best)

def words_often(freqs, minTimes):
    result = []
    done False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result