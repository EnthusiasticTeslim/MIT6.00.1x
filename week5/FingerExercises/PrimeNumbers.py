# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:57:39 2019

@author: olayi
"""

def genPrimes():
    """
    Write a generator, genPrimes, that returns the sequence of prime numbers on
    successive calls to its next() method
    Example: 2, 3, 5, 7, 11
    
    Hint: 
        A candidate number x is prime if (x % p) != 0 for all earlier primes p
    """
    start = 1
    prime_numbers = []
    while True:
        start += 1
        for val in prime_numbers:
            if start % val == 0:
                break
        else:
            prime_numbers.append(start)
            next = start
            yield next
            
            