##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 2   : Shukla_LAB1_Ques_2.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 14:22:21 2021
@author: ruchishukla
"""

##Input age and determine if the person is an infant, a child, a teenager or an adult.
age = int(input('Enter the age of person: '))

##conditions and result
if age <= 1:
    print('The person is an Infant')
elif age > 1 and age < 13:
    print('The person is a Child')
elif age >=13 and age < 20:
    print('The person is a Teenager')
else:
    print ('The person is an Adult')
