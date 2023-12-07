import os
import string
from collections import deque

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").read().strip()
lines = [x for x in lst.split('\n')]

current_value = 0
sum_value = 0

for line in lines:
    first_digit = ""
    last_digit = ""
    for char in line:
        if char.isnumeric():
            if first_digit == "":
                first_digit = char
            else:
                last_digit = char
        
    if last_digit == "":
        last_digit = first_digit
    current_value = str(first_digit) + str(last_digit)

    sum_value += int(current_value)

print(sum_value)