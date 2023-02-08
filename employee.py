##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 4  : Shukla_Lab3_Q3.py
##Submitted by  : Ruchi Shukla (1001977095)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:23:42 2021
@author: ruchishukla
"""
# The Employee class holds the information about employees.
class Employee:
    # The __init__ method initializes the attributes.
    def __init__(self, name, ID_number,department, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    # The set_name method sets the name attribute.
    def set_name(self, name):
        self.__name = name

    # The set_ID_number method sets the ID attribute.
    def set_ID_number(self, ID_number):
        self.__ID_number = ID_number

    # The set_department method sets the department attribute.
    def set_department(self, department):
        self.__department = department
        
    # The set_job_title method sets the job_title attribute.
    def set_job_title(self, job_title):
        self.__job_title = job_title

    # The get_name method returns the name attribute.
    def get_name(self):
        return self.__name

    # The get_ID_number method returns the ID_number attribute.
    def get_ID_number(self):
        return self.__ID_number

    # The get_department method returns the department attribute.
    def get_department(self):
        return self.__department
    
    # The get_job_title method returns the job_title attribute.
    def get_job_title(self):
        return self.__job_title

    # The __str__ method returns the object's state
    # as a string.
    def __str__(self):
        return 'Name: ' + self.__name + \
               '\nID_number: ' + self.__ID_number + \
               '\nDepartment: ' + self.__department + \
               '\nJob_title: ' + self.__job_title  
