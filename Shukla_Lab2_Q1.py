##INSY 5336-001 : PYTHON PROGRAMMING Fall 2021
##Assigment 3   : Shukla_Lab2_Q1.py
##Submitted by  : Ruchi Shukla (1001977095)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:42:50 2021

@author: ruchishukla
"""


def main():
    ## variable declaration
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    score5 = 0
    average_score = 0
    score = 0
    score1, score2, score3, score4, score5 = enter_score()
    average_score = calc_average(score1, score2, score3, score4, score5)
    score = determine_grade(score)
    avglgrade = determine_avglgrade(average_score)
    
    ## display output
    print('\nScore\t\tNumeric Grade\t\tLetter Grade')
    print('------------------------------------------')
    print('score1:','\t\t',score1,'\t\t','\t\t',determine_grade(score1))
    print('score2:','\t\t',score2,'\t\t','\t\t',determine_grade(score2))
    print('score3:','\t\t',score3,'\t\t','\t\t',determine_grade(score3))
    print('score4:','\t\t',score4,'\t\t','\t\t',determine_grade(score4))
    print('score5:','\t\t',score5,'\t\t','\t\t',determine_grade(score5))
    print('------------------------------------------')
    print('average score:',average_score,'\t\t\t\t',avglgrade)

## ask user to enter five scores    
def enter_score():
    score1 = float(input('Enter score 1: '))
    score2 = float(input('Enter score 2: '))
    score3 = float(input('Enter score 3: '))
    score4 = float(input('Enter score 4: '))
    score5 = float(input('Enter score 5: '))
    return score1, score2, score3, score4, score5
    
## calculate average score (total of all scores divide by 5)  
def calc_average(score1, score2, score3, score4, score5):
    average_score = (score1 + score2 + score3 + score4 + score5)/5
    return average_score

## check score and determine grade
def determine_grade(score):
    ## determine if the score is between 90-100
    if score >= 90 and score <= 100:
        return 'A'
    ## determine if the score is between 80-89
    elif score >= 80 and score <= 89:
        return 'B'
    ## determine if the score is between 70 and 79
    elif score >= 70 and score <= 79:
        return 'C'
    ## determine if the score is between 60-69
    elif score >= 60 and score <= 69:
        return 'D'
    ## determine if the score is below 60
    else:
        return 'F'

## check average grade
def determine_avglgrade(average_score):
    ## determine if the average_score is between 90-100
    if average_score >= 90 and average_score <= 100:
        return 'A'
    ## determine if the average_score is between 80-89
    elif average_score >= 80 and average_score <= 89:
        return 'B'
    ## determine if the average_score is between 70 and 79
    elif average_score >= 70 and average_score <= 79:
        return 'C'
    ## determine if the average_score is between 60-69
    elif average_score >= 60 and average_score <= 69:
        return 'D'
    ## determine if the average_score is below 60
    else:
        return 'F'


main()