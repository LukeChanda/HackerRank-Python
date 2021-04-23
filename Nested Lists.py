# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:47:02 2021

@author: Luke

HackerRank Problem - Nested Lists
Given the names and grades for each student in a class of  students, store
them in a nested list and print the name(s) of any student(s) having the 
second lowest grade.

Note: If there are multiple students with the second lowest grade, order their
names alphabetically and print each name on a new line.
"""

records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41],
           ['Harsh', 39]]

# sort records in descending order with respect to the score
rec = sorted(records, key = lambda x: x[1])


# lowest score -  the greater the magnitude of the score the lower 
lowest_score = rec[0][1]

second_lowest_score = 0

# identify second lowest score value
for i in range(1,len(rec)):
    if(rec[i][1] > lowest_score):
        second_lowest_score = rec[i][1]
        break

# store student names with second lowest score
names = []
for i in range(1,len(rec)):
    if(rec[i][1] == second_lowest_score):
       names.append(rec[i][0])

[print(name) for name in sorted(names)]