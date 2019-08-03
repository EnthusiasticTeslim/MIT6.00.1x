# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 04:30:29 2019

@author: olayi
"""

def printMove(fro,to):
    print('move from' + str(fro) + " to " + str(to))
    
def Towers(n, fro, to, spare):
    if n == 1:
        printMove(fro, to)
    else:
        Towers(n-1, fro, spare, to)
        Towers(1, fro, to, spare)
        Towers(n-1, spare, to, fro)
        
print(Towers(4, 'P1', 'P2', 'P3'))