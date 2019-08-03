# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:11:50 2019

@author: olayi
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        try:
            return item / denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
        