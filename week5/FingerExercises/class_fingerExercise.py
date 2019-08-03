# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:50:41 2019

@author: olayi
"""

class Coordinate(object):
    def __init__(self, x, y):
        # create an instance for class Coordinate with parent Object
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, others):
        '''
        method that returns True if coordinates refer to same point in the plane
        (i.e., have the same x and y coordinate)
        '''
        if (self.getX(), self.getY()) == (others.getX(), others.getY()):
            return True
        else:
            return False
        
    def __repr__(self):
        '''
        returns a string that looks like a valid Python expression 
        that could be used to recreate an object with the same value
        '''
        #return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
        return 'Coordinate({},{})'.format(self.getX(),self.getY())
        
    