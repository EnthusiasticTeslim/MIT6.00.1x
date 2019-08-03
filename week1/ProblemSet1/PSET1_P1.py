# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:45:38 2019

@author: olayi
"""
# n: number of months

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

n = 12
for i in range(n):
   # Minimum monthly payment
   month_pay = balance * (monthlyPaymentRate)
   
   # Unpaid balance
   ub = balance - month_pay
   
   # Interest %
   interest = (annualInterestRate)*ub/12
   
   # New Balance
   balance = ub + interest


print("Remaining balance:",round(balance,2))
   
