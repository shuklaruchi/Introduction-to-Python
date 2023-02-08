##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 3   : Shukla_Lab2_Q2.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:07:47 2021

@author: ruchishukla
"""
## OS to remove and rename functions
import os  

# Constants to get employees details by selecting choice
ADD_CHOICE = 1
SHOW_CHOICE = 2
SEARCH_CHOICE = 3
MODIFY_CHOICE = 4
DELETE_CHOICE = 5
QUIT_CHOICE = 6

## main function.
def main():
## The choice variable controls the loop.
    choice = 0
    
    while choice != 6:
## display the contact directory
        display_directory()
        
## Get the user's choice.
        choice = int(input('Enter your choice: '))
        
## Perform the selected action.
        if choice == 1:
            add()             
        elif choice == 2:
            show()             
        elif choice == 3:
            search()
        elif choice == 4:
            modify()
        elif choice == 5:
            delete()
        elif choice == 6:
            print('Exit the program')
        else:
            print('invalid selection')
    
## display_contact_info function displays the employees details.
def display_directory():
    print('\nEmployees contact Directory App\n')
    print('1. Add a name')
    print('2. Show the list of contacts')
    print('3. Search for a name in the list')
    print('4. Modify a contact')
    print('5. Delete a contact form the list')    
    print('6. Quit')
    
def add():
## Create a variable to control the loop.
    another = 'y'

## Open the employees.txt file in append mode.
    contact_file = open('contact.txt', 'a')

## Add contacts to the file.
    while another == 'y' or another == 'Y':
## Get the employees details data.
        print('Enter the following details:')
        name = input('Name: ')
        email = input('email address: ')
        phone_number = input('phone number: ')

## Append the data to the file.
        contact_file.write(name + '\n')
        contact_file.write((email) + '\n')
        contact_file.write((phone_number) + '\n')

## Ask whether the user wants to add another data to the file.
        print('Do you want to add another data?')
        another = input('Y = yes, anything else = no ')

## Close the file.
    contact_file.close()
    print('Data appended to contact.txt')
   
def show():
    
    try:
## Open the contact.txt file.
        contact_file = open('contact.txt', 'r')
## Read the first contact name field.
        name = contact_file.readline()
## Read the rest of the file.
        while name != '':
## Read the email field
            email = (contact_file.readline())
## Read the phone number field.
            phone_number = (contact_file.readline())
# Strip the \n from the description.
            name = name.rstrip('\n')
            email = email.rstrip('\n')
## Display the record.
            print('List of contact(s)')
            print('\tContact #')
            print('\t\t','Name:', name)
            print('\t\t','email address:', email)
            print('\t\t','phone number:', phone_number)
            print('--------------------------------------')

## Read the next description.
            name = contact_file.readline()

## Close the file.
        contact_file.close()
        
    except IOError as err:
        print(err)

def search():
## Create a boolean variable
    found = False
## Get the search value.
    search = input('Enter a name to search for: ')
## Open the contact.txt file.
    contact_file = open('contact.txt', 'r')
    
## Read the first record
    name = contact_file.readline()
## Read the rest of the file.
    while name != '':
## Read the email field.
        email = (contact_file.readline())
## Read the phone number field.
        phone_number = (contact_file.readline())
## Strip the \n
        name = name.rstrip('\n')
        email = email.rstrip('\n')
## check whether this record matches with the search value.
        if name == search:
## Display the data.
            print('Name of employee:', name)
            print('email address:', email)
            print('phone number:', phone_number)
## Set the found to True.
            found = True
## Read the next description.
        name = contact_file.readline()
## Close the file.
    contact_file.close()

## If the search value was not found in the file
## display a message.
    if not found:
        print('The item was not found in the file.')
 
def modify():
## Create a boolean variable
    found = False
## Get the search value and the new data.
    search = input('Enter a name to search for: ')
    new_email = input('Enter the new email: ')
    new_phone_number = input('Enter the new phone number: ')
## Open the original contact.txt file.
    contact_file = open('contact.txt', 'r')
## Open the temporary file.
    temp_file = open('temp.txt', 'w')
## Read the first record
    name = contact_file.readline()
## Read the rest of the file.
    while name != '':
## Read the email field
        email = (contact_file.readline())
## Read the phone number field.
        phone_number = (contact_file.readline())
## Strip the \n from the name & email.
        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phone_number = phone_number.rstrip('\n')
## Write either this data to the temporary file,
## or the new data if this is the one that is to be modified.
        if name == search:
## Write the modified data to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(str(new_email) + '\n')
            temp_file.write(str(new_phone_number) + '\n')
## Set the found to True.
            found = True
        else:
## Write the original data to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(str(email) + '\n')
            temp_file.write(str(phone_number) + '\n')
## Read the next data.
        name = contact_file.readline()
## Close the contact file and the temporary file.
    contact_file.close()
    temp_file.close()

## Delete the original contact.txt file.
    os.remove('contact.txt')

## Rename the temporary file.
    os.rename('temp.txt','contact.txt')
## If the search value was not found in the file, display a message.
    if found:
        print('The file has been updated.')
    else:
        print('The item was not found in the file.')
    
def delete():
## Create a bool variable.
    found = False
## Get the name to delete.
    search = input('Which employee information do you want to delete? ')
## Open the original contact.txt file.
    contact_file = open('contact.txt', 'r')
## Open the temporary file.
    temp_file = open('temp.txt', 'w')
## Read the first data field.
    name = contact_file.readline()
## Read the rest of the file.
    while name != '':
## Read the email field
        email = (contact_file.readline())
## Read the phone number field.
        phone_number = (contact_file.readline())
## Strip the \n from the description.
        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phone_number = phone_number.rstrip('\n')
## If this is not the data to delete,then write it to the temporary file.
        if name != search:
## Write the data to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(str(email) + '\n')
            temp_file.write(str(phone_number) + '\n')
        else:
##Set the found flag to True.
            found = True
## Read the next description.
        name = contact_file.readline()
## Close the contact file and the temporary file.
    contact_file.close()
    temp_file.close()
## Delete the original contact.txt file.
    os.remove('contact.txt')
## Rename the temporary file.
    os.rename('temp.txt', 'contact.txt')
## If the search value was not found in the file, display a message.
    if found:
        print('The file has been updated.')
    else:
        print('The item was not found in the file.')
main()