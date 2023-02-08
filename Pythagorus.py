##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 5  : Shukla_Lab4_Q1.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 14:30:01 2021

@author: ruchishukla
"""

## create a GUI program to calculate hypotanese of a right 
## angle triangle when two other sides are given.

import tkinter
import math
class Pythagoras:
    def __init__(self):
        ## Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Right Triangle Calculator')
    
        
        ## Create four frames
        self.sideA_frame = tkinter.Frame(self.main_window)
        self.sideB_frame = tkinter.Frame(self.main_window)
        self.sideC_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
    

        ## Create and pack the widgets for side A
        self.sideA_label = tkinter.Label(self.sideA_frame,text='Side A:')
        self.sideA_entry = tkinter.Entry(self.sideA_frame,width=20)
        self.sideA_label.pack(side='left')
        self.sideA_entry.pack(side='left')

        ## Create and pack the widgets for side B
        self.sideB_label = tkinter.Label(self.sideB_frame,text='Side B:')
        self.sideB_entry = tkinter.Entry(self.sideB_frame,width=20)
        self.sideB_label.pack(side='left')
        self.sideB_entry.pack(side='left')
        
        
        ## Create and pack the widgets for side C
        self.result_label = tkinter.Label(self.sideC_frame,
                                         text='Side C:')
        self.sideC = tkinter.StringVar()
        self.sideC_entry = tkinter.Entry(self.sideC_frame,
                                         textvariable=self.sideC, width=20)
        self.result_label.pack(side='left')
        self.sideC_entry.pack(side='left')
        

        ## Create and pack the widgets for the calculator
        self.exit_button = tkinter.Button(self.button_frame,text='Exit', 
                                          command=self.main_window.destroy)
        self.calc_button = tkinter.Button(self.button_frame,text='Calculate', 
                                          command=self.calc_sideC)
        self.calc_button.pack(side='left')
        self.exit_button.pack(side='right')
        

        ## Pack the frames
        self.sideA_frame.pack()
        self.sideB_frame.pack()
        self.sideC_frame.pack()
        self.button_frame.pack()

        ## Start the main loop
        tkinter.mainloop()
  
    def calc_sideC(self):
        self.sideA = float(self.sideA_entry.get())
        self.sideB = float(self.sideB_entry.get())
        
        ## Calculate the square root of boths sides
        self.hypotenuse = math.sqrt((self.sideA**2) + (self.sideB**2))
        ## formatting the value to 3 decimal place
        self.sideC.set(format(self.hypotenuse,'.3f'))
    
Pyth_Theorem = Pythagoras()