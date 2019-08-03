# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:36:35 2019

@author: olayi
"""

def openOrSenior(data):
    results = []
    for values in data:
        if values[0] >= 55 and values[-1] > 7:
            results.append('Senior')
        else:
            results.append('Open')
    return results