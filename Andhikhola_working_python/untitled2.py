# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:17:38 2023

@author: kumar
"""

# open the file for reading
with open("number.txt", "r") as file:
    # read all the lines of text from the file
    lines = file.readlines()

# initialize a list to store the numbers
numbers = []

# loop over each line of text
for line in lines:
    # remove the newline character from the end of the line
    line = line.strip()

    # convert the line into a number
    number = int(line)

    # add the number to the list of numbers
    numbers.append(number)

# define a string that contains the numeral text with invalid characters
text = 'Â\xa021'

# remove the invalid characters from the string
text = text.replace("\xa0", "").replace("Â", "")

# convert the string into an integer
number = int(text)

# print the number
print(number)

