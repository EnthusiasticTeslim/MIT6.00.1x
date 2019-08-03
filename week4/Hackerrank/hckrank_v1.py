# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 08:32:38 2019

@author: olayi
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print("Weird")
else:
    if 1 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")