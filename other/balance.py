# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:24:24 2019

@author: olayi
"""

"""
Determine:
    Lowest payment to pay off a debt in a single year
Given values:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal

Calculations:
    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) +
                            (Monthly interest rate x Monthly unpaid balance)
Variables definition:
    mmp: minimum fixed monthly payment
    b: Amount owed
    ub: updated unpaid balance
    r: annual interest rate
    mup: month unpaid balance
    mit: Monthly interest rate
"""

#r = float(input("Annual interest rate: "))
#b = float(input("Amount owed: "))
r = 0.2
b = 3329
mmp = 10
mit = r/12
mup = b - mmp
# At the begining of the first month the 
umb = mup + mit*mup

    for i in range(0,12):
        umb -= mmp
        mup = umb - mmp
        umb = umb + mit*
    mmp += 10
    
print("Lowest Payment:",mmp)
