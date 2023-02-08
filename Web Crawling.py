##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 4  : Shukla_Lab3_Q1.py
##Submitted by  : Ruchi Shukla (1001977095)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:15:44 2021
@author: ruchishukla
"""
import re
from urllib.request import urlopen
def emails(website):
##declaring the list
    list = []
    
## applying for loop to print email address in the list
    for email in re.findall(r'[\w\.]+@[\w\.]+', website):
##check if email is not in the list 
        if not email in list: 
            list.append(email)
##add the email to the list
    return(list)
##assigning the webpage
url = 'https://www.uta.edu/academics/schools-colleges/business/departments/marketing'
website = urlopen(url).read().decode()
##call the function
list = emails(website)
print(list)
