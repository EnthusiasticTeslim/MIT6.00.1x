# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 01:27:12 2019

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

balance = 4773
annualInterestRate = 0.2
month_pay = 10
updatedBalance = 0


def balance_calc(balance, annualInterestRate, month_pay):
    for i in range(12):
    # Minimum monthly payment Interest %
        monthInterestRate = (annualInterestRate)/12
        # month unpaid balance
        if i == 0:
            updatedBalance = balance - month_pay
        else:
            updatedBalance = updatedBalance - month_pay
        # New Balance
        updatedBalance = updatedBalance + monthInterestRate * updatedBalance
    return updatedBalance

# updated unpaid balance calculation
updatedBalance = balance_calc(balance, annualInterestRate, month_pay)

while updatedBalance > 0:
    if updatedBalance <= 0:
        month_pay = month_pay
    else:
        month_pay += 10
        updatedBalance = balance_calc(balance, annualInterestRate, month_pay)

print("Lowest Payment:",round(month_pay,2))