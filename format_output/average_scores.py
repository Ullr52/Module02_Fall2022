"""
Program: Module 2 Topic 3 Basic Input and Format Output Assignment
Author: John Ord
Last date modified: 09/05/2022

This program is to take user input and output names and average of scores
"""


last_name = input('Enter your last name: ')
first_name = input('Enter your first name: ')
age = int(input('Enter your age: '))
score1 = float(input('Enter your first score: '))
score2 = float(input('Enter your second score: '))
score3 = float(input('Enter your third score: '))

average = (score1 + score2 + score3)/3

print('{}, {}, Age: {}, average grade: {:.2f}'.format(last_name, first_name,age,average))

