# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:24:12 2019

@author: olayi
"""

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

Pizza(['cheese', 'tomatoes'])
Pizza(['cheese', 'tomatoes'])