##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 2   : Shukla_LAB1_Ques_1.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:15:14 2021

@author: ruchishukla
"""

##write the date of the month
date = int(input('Please enter the day of the month (1-31):'))
if date > 31 or date <= 0:
    print('Error: Please check the date entered')
elif date <= 31 :    
    month = int(input('Please enter the month as a number(1-12):'))
    if month > 12 or month <= 0:
        print('Error : Please check the month entered')
    else :    
        if month == 1:
            english_form = 'January'
            spanish_form = 'Enero'
        elif month == 2:
            english_form = 'Febraury'
            spanish_form = 'Febrero'
        elif month == 3:
            english_form = 'March'
            spanish_form = 'Marzo'
        elif month == 4:
            english_form = 'April'
            spanish_form = 'Abril'
        elif month == 5:
            english_form = 'May'
            spanish_form = 'Mayo'
        elif month == 6:
            english_form = 'June'
            spanish_form = 'Junio'
        elif month == 7:
            english_form = 'July'
            spanish_form = 'Julio'
        elif month == 8:
            english_form = 'August'
            spanish_form = 'Agosto'
        elif month == 9:
            english_form = 'September'
            spanish_form = 'Septembre'
        elif month == 10:
            english_form = 'October'
            spanish_form = 'Octubre'
        elif month == 11:
            english_form = 'November'
            spanish_form = 'Noviembre'
        elif month == 12:
            english_form = 'December'
            spanish_form = 'Diciembre'
            ##Output
        print(english_form, date, 'or', date, spanish_form)


 