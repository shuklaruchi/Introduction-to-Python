##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 4  : Shukla_Lab3_Q3.py
##Submitted by  : Ruchi Shukla (1001977095)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:24:20 2021
@author: ruchishukla
"""
# This program manages employee info.
import employee
import pickle

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'employee.dat'

# main function
def main():
    # Load the existing contact dictionary and
    # assign it to myemployee.
    myemployee = load_employee()

    # Initialize a variable for the user's choice.
    choice = 0

    # Process menu selections until the user
    # wants to quit the program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(myemployee)
        elif choice == ADD:
            add(myemployee)
        elif choice == CHANGE:
            change(myemployee)
        elif choice == DELETE:
            delete(myemployee)

    # Save the myemployee dictionary to a file.
    save_employee(myemployee)

def load_employee():
    try:
        # Open the employee.dat file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        employee_dct = pickle.load(input_file)

        # Close the info_inventory.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        employee_dct = {}

    # Return the dictionary.
    return employee_dct

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an existing employee')
    print('4. Delete an employee')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# The look_up function looks up an item in the
# specified dictionary.
def look_up(myemployee):
    # Get an ID to look up.
    ID_number = input('Enter a ID_number: ')

    # Look it up in the dictionary.
    print(myemployee.get(ID_number, 'That ID is not found.'))

# The add function adds a new entry into the
# specified dictionary.
def add(myemployee):
    # Get the employee info.
    name = input('Name: ')
    ID_number = input('ID_number: ')
    department = input('Department: ')
    job_title = input('Job_title: ')

    # Create a employee object named entry.
    entry = employee.Employee(name, ID_number,department, job_title)

    # If the ID_number does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if ID_number not in myemployee:
        myemployee[ID_number] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')

# The change function changes an existing
# entry in the specified dictionary.
def change(myemployee):
    # Get a ID_number to look up.
    ID_number = input('Enter a ID_number: ')

    if ID_number in myemployee:
        # Get a new name.
        name = input('Enter the new name: ')

        # Get a new department
        department = input('Enter the new department: ')
        
        # Get a new job_title
        job_title = input('Enter the new job_title: ')

        # Create a employee object named entry.
        entry = employee.Employee(name, ID_number, department, job_title)

        # Update the entry.
        myemployee[ID_number] = entry
        print('Information updated.')
    else:
        print('That ID is not found.')

# The delete function deletes an entry from the
# specified dictionary.
def delete(myemployee):
    # Get a ID_number to look up.
    ID_number = input('Enter a ID_number: ')

    # If the ID is found, delete the entry.
    if ID_number in myemployee:
        del myemployee[ID_number]
        print('Entry deleted.')
    else:
        print('That ID is not found.')

# The save_employee funtion pickles the specified
# object and saves it to the employee file.
def save_employee(myemployee):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(myemployee, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
main()

    
