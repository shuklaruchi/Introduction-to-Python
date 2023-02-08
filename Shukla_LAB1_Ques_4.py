##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 2   : Shukla_LAB1_Ques_4.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:41:09 2021

@author: ruchishukla
"""

##assigning range of celsius temp (0-21), in table form
##Display the conversion from C to F in table

print('\nBelow is the table for conversion of degree celsius into fahrenheit:')

print('\nTemperature in Celsius\t\tTemperature in Fahrenheit')
for celsius_temp in range(21):
    fahrenheit_temp = (9/5) * celsius_temp + 32
    print(celsius_temp,'\t\t\t\t\t\t\t\t\t\t',format(fahrenheit_temp,'.2f'))