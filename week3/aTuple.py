# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 20:18:31 2019

@author: olayi
"""

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums += (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_num = min(nums)
    max_num = max(nums)
    unique_words = len(words)
    return (min_num,max_num,unique_words)

(small,large,unique_words) = get_data(((1,'mine'),(3,'yours'),(5,'ours'),(7,'mine')))