# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:36:40 2019

@author: olayi
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
        
    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        '''
        returns the length of the attributes
        '''
        count = 0
        for value in self.vals:
            count +=1
        return count
    
    def intersect (self,other):
        '''
        return a new intSet of integers that appear 
        in both self attributes and others
        '''
        inter = []
        if len(other.vals) > 0 and len(self.vals) > 0:
            for value in other.vals:
                if value in self.vals:
                    inter.append(value)
        return '{' + ','.join([str(val) for val in inter]) + '}'

#val = intSet()
#setA =  {-19,-13,-11,-5,-1,1,9,10,13,20}
#setB =  {-17,-9,-7,2,5,7,11,19,20}
#
#val.vals = setA
#
#print(val.intersect(setB))

