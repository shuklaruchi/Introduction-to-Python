##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 2   : Shukla_LAB1_Ques_5.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:48:24 2021

@author: ruchishukla
"""
##any non-negative integer = n 
##input the number
number = int(input('Enter a non-negative integer(n):'))
while number < 1:
    number = int(input('Enter a non-negative integer(n) again:'))

factorial = 1 
for number in range(1, number + 1):
    factorial = factorial * number
    
print ('The factorial of', number, 'is', factorial,'.')
    

