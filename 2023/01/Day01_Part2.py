import os
import string
from collections import deque

# Set realDataSet to True to test with real dataset
realDataSet = True

lst = ""
if realDataSet:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").read().strip()
else:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\dataexemplepart2.txt", "r").read().strip()

lines = [x for x in lst.split('\n')]

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

current_value = 0
sum_value = 0

for line in lines:
    first_digit = ""
    last_digit = ""
    try_digit = ""
    i = -1
    for char in line:
        i += 1
        if char.isnumeric(): #This character is numeric so we can take it as is
            if first_digit == "":
                first_digit = char
            else:
                last_digit = char

        else:
            try_digit = ""
            threeLetterNumber = line[i:i+3]
            fourLetterNumber = line[i:i+4]
            fiveLetterNumber = line[i:i+5]

            if threeLetterNumber in numbers:
                try_digit = numbers[threeLetterNumber]
            
            if fourLetterNumber in numbers:
                try_digit = numbers[fourLetterNumber]

            if fiveLetterNumber in numbers:
                try_digit = numbers[fiveLetterNumber]
            
            if try_digit != "":
                if first_digit == "":
                    first_digit = try_digit
                else:
                    last_digit = try_digit

    if last_digit == "":
        last_digit = first_digit
    current_value = str(first_digit) + str(last_digit)

    sum_value += int(current_value)

print(sum_value)