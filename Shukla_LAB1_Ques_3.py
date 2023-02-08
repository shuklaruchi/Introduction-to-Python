##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 2   : Shukla_LAB1_Ques_3.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:00:54 2021

@author: ruchishukla
"""

##each packages costs $99. 
##determine amount of package and discount
##calculate final cost after discount applied

cost_of_package = 99.00
quantity_of_packages_purchased = 0.0

quantity_of_packages_purchased = int(input('Enter the quantity purchased: '))

##conditions
if quantity_of_packages_purchased < 10:
    discount = 0
    print('Number of packages should atleast be 10 for any discount')
    
else:
    if quantity_of_packages_purchased >=10\
        and quantity_of_packages_purchased <=19:
        discount = .10 #10% discount applied
    elif quantity_of_packages_purchased >=20\
        and quantity_of_packages_purchased <=49:
        discount = .20 #20% discount applied
    elif quantity_of_packages_purchased >=50\
        and quantity_of_packages_purchased <=99:
        discount = .30 #30% discount applied
    elif quantity_of_packages_purchased >=100:
        discount = .40 #40% discount applied

##Calculate discount applied and total amount
amount_total = quantity_of_packages_purchased * cost_of_package
discount_amount = amount_total * discount
total_amount_after_discount = amount_total - discount_amount

##Output/Result
print('Total amount of package = $',format(amount_total, '.2f'))
print('Amount of discount applied = $',format(discount_amount, '.2f'))
print('The total amount after discount = $'\
      ,format(total_amount_after_discount, '.2f'))