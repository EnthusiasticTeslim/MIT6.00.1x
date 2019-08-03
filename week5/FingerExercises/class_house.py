# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:20:51 2019

@author: olayi
"""

class House(object):
    def __init__(self, street, rooms, bathrooms):
        self.street = street
        self.rooms = rooms
        self.bathrooms = bathrooms
        # Not provided as input
        self.clean = True
        
    def cleanHouse(self):
        if not self.clean:
            self.clean = True
            print("This house is now clean")
        else:
            print("This house is already clean")
    
    def unCleanHouse(self):
        if self.clean:
            self.clean = False
            print("This house is now dirty")
        else:
            print("This house was dirty already")
    
    def talk(self, phrase):
        print(phrase)
        
house1 = House(35, 15, 16)
house2 = House(50, 25, 86)
