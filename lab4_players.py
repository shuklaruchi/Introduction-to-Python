##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 5  : Shukla_Lab4_Q2.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Nov 18 20:07:02 2021

@author: ruchishukla
"""
##Import the sqlite package
import sqlite3

##Establish a sqlite database connection and open the
##database file players_Data.db.
conn = sqlite3.connect('players_Data.db')

def main():
    choice = input("Command: ")
    if choice == "view":
        view()
    elif choice == "add":
        add()
    elif choice == "del":
        delete()
    elif choice == "update":
        update()
    elif choice == "exit":
        exit_program()
    
    else:
        print("Please enter a valid command: ")
        main()

##Display the command menu.
def menu():
    print("Player Manager")
    print()
    print("COMMAND MENU")
    print("view - View players")
    print("add - Add a player")
    print("delete - Delete a player")
    print("update - Update a player")
    print("exit - Exit program")
    print()
    
def table():
    conn.execute('''
    
    CREATE TABLE if not exists Player
    (
     name          TEXT          NOT NULL,
     wins          INTEGER       NOT NULL,
     losses        INTEGER       NOT NULL,
     ties          INTEGER       NOT NULL                           
     )
                
     ''')
    conn.close()

def view():
    conn = sqlite3.connect('players_Data.db')
    
    ##Execute the query to select the records ordered by
    ##number of wins in descending order.
    cur = conn.execute("SELECT name,wins,losses,ties "+
    "FROM Player ORDER by wins desc")
    
    ##Display the header of the table.
    print("{0:10}{1:8}{2:8}{3:8}{4:8}".format
    ("Name", "Wins", "Losses", "Ties", "Games"))
    print("-" * 42)
    
    ##Start the for loop till the number of rows in
    ##the cursor and display all the records.
    for r in cur:
        print("{0:6}{1:6}{2:8}{3:8}{4:8}".format
        (r[0].capitalize(), r[1], r[2], r[3], r[1] + r[2] + r[3]))
    conn.close()    
    main()
    
    
def add():
    conn = sqlite3.connect('players_Data.db')
    
    name = input("Name :")
    wins = int(input("Wins :"))
    losses = int(input("Losses :"))
    ties = int(input("Ties :"))
    records = (name, wins, losses, ties)
    add_query = 'INSERT INTO Player VALUES (?,?,?,?)'
    conn.execute(add_query, records)
    conn.commit()
    conn.close()
    print(name + " was added to the database")
    main()


def delete():
    flag = False
    delete_name = input("Name: ")
    conn = sqlite3.connect('players_Data.db')
    
    query = '''SELECT name, wins, losses, ties
                    FROM Player ORDER BY wins DESC'''
    curs = conn.execute(query)
  
    for row in curs:
        if delete_name in row:
            cursor = conn.cursor()
            delete_query = '''DELETE from Player where name = ?'''
            cursor.execute(delete_query, (delete_name,))
            conn.commit()
            flag = True
    if flag == True:
        print(delete_name + " was deleted from the database")
    else:
        print(delete_name + " was not found")
    conn.close()
    main()


def update():
    flag = False
    update_name = input("Name: ")
    conn = sqlite3.connect('players_Data.db')
    query = '''SELECT name, wins, losses, ties
                    FROM Player ORDER BY wins DESC'''
    curs = conn.execute(query)
    
    for row in curs:
            if update_name in row:
                wins_update = input("Wins: ")
                losses_update = input("Losses: ")
                ties_update = input("Ties: ")
                cursor = conn.cursor()
                delete = '''DELETE from Player where name = ?'''
                cursor.execute(delete, (update_name,))
                conn.commit()
                
                update = '''INSERT INTO Player (name, wins, losses, ties)
                             VALUES (?, ?, ?, ?)'''
                conn.execute(update, (update_name, wins_update, losses_update, ties_update))
                conn.commit()
                flag = True
    if flag == True:
        print(update_name + " was updated in the database")
    else:
        print(update_name + " was not found")
    conn.close()
    main()
    
def exit_program():
    print("Bye!")
    
table()   
menu()      
main()   