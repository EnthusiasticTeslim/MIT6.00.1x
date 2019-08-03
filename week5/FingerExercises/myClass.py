# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:05:48 2019

@author: olayi
"""

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'