# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:38:26 2021

@author: Luke

HackerRank Problem - Finding the percentage

Print average mark of student with name being queried.
"""

records = {} # empty dictionary

# Test data

Harsh_marks = [25, 26.5, 28]
Anurag_marks = [26, 28, 30]

records['Harsh'] = Harsh_marks
records['Anurag'] = Anurag_marks

# test query name
query_name = 'Anurag'

if query_name in records:
    # calculate average
    avg = (records[query_name][0] + records[query_name][1] +\
           records[query_name][2])/3
    
    # format output to 2 decimal places
    print('{:.2f}'.format(avg, '.2f')) 