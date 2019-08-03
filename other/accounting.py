# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:00:19 2019

@author: olayi
"""

n =  int(input("Number of months: "))
amount = float(input("Enter the amount owed: "))
min_int = float(input("Minimum monthly payment rate: "))
r = float(input("Enter rate: "))
if n == 0:
    multi = 0
else:
    multi = 1
    
#month_pay = amt * min_int
#ub = amount - month_pay 
for i in range(n):
   # amount owed
   month_pay = amount * (min_int/100)
   print('Monthly pay at',str(i),"is",month_pay)
   ub = amount - month_pay
   print('Unpaid balance at beginning at',str(i),"is",ub)
   int = (r/100)*ub/12
   print('Interest at',str(i),"is",int)
   amount = ub + int
   print('Amount owed at',str(i),"is",amount)
   


