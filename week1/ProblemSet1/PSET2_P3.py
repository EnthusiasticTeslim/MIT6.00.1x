# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 04:27:12 2019

@author: olayi
"""
"""
Determine:
    Lowest payment to pay off a debt in a single year
Given values:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal

Calculations:
    Monthly interest rate : (Annual interest rate) / 12.0
    Monthly unpaid balance : (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month : (Monthly unpaid balance) +
                            (Monthly interest rate x Monthly unpaid balance)
Variables definition:
    month_pay: minimum fixed monthly payment
    updatedBalance: updated unpaid balance
"""

def balance_calc(balance, monthInterestRate, month_pay):
    for i in range(12):
        # month unpaid balance
        if i == 0:
            updatedBalance = balance - month_pay
        else:
            updatedBalance = updatedBalance - month_pay
        # New Balance
        updatedBalance = updatedBalance + monthInterestRate * updatedBalance
    return updatedBalance

# assumptions
balance = 999999
annualInterestRate = 0.18
monthInterestRate = (annualInterestRate)/12
lowerbd = balance / 12
upperbd = (balance*(1 + monthInterestRate)**12)/12.0
month_pay = (lowerbd + upperbd)/2
#updatedBalance = 0
tolerance = 0.1

while True:
    # updated unpaid balance calculation
    updatedBalance = balance_calc(balance, monthInterestRate, month_pay)
    if abs(updatedBalance) < tolerance:
        print("Lowest Payment:",round(month_pay,2))
        break
    else:
        if updatedBalance > 0:
            lowerbd = month_pay
        else:
            upperbd = month_pay
    month_pay = (lowerbd + upperbd)/2

print("Lowest Payment:",round(month_pay,2))
