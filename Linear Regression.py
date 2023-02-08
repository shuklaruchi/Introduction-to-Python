##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 4  : Shukla_Lab3_Q2.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 23:45:26 2021
@author: ruchishukla
"""
##Import python libraries
import numpy as np

## To visualize
import matplotlib.pyplot as plt

## To read data
import pandas as pd

from sklearn.linear_model import LinearRegression

## load data set from csv file
data = pd.read_excel('Insurance_charges.xlsx')
## values converts it into a numpy array 
X = data.iloc[:, 2].values.reshape(-1, 1) 
## -1 means that calculate the dimension of rows, but have 1 column  
Y = data.iloc[:, 6].values.reshape(-1, 1)

## Labeling the Scatterplot
plt.title('Insurance charges vs BMI')
plt.xlabel('BMI')
plt.ylabel('Insurance Charges')

## create object for the class LinearRegression
linear_regressor = LinearRegression()

## perform linear regression
linear_regressor.fit(X,Y)

## make predictions 
Y_pred = linear_regressor.predict(X)
  
##scattered plot using X and Y
plt.scatter(X, Y)

##line plot with red color
plt.plot(X, Y_pred, color='red') 

##display plots
plt.show()