# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:47:34 2019

@author: olayi
"""

varA = 'hola'
varB = 'hola'
if type(varA) == str or type(varB) == str:
    print("string involved")
   
elif varA > varB:
    print("bigger")
 
elif varA == varB:
    print("equal")
else:
     print("smaller")