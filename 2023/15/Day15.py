#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 15
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time
from collections import deque

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 15

print(f"* Day {day} *")

#---------------------------------------------------------------------------------------------------------------
# Reading Data
#---------------------------------------------------------------------------------------------------------------

startReading = time.time()
lst = ""
if realDataSet:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").read().strip()
else:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\dataexemple.txt", "r").read().strip()

endReading = time.time()
readingTime = startReading - endReading
print(f"Time to read the file :  {readingTime}")

#---------------------------------------------------------------------------------------------------------------
# Part 1 !
#---------------------------------------------------------------------------------------------------------------
solutionStart = time.time()
lines = [x for x in lst.split(',')]

result = 0

for line in lines:

    current_value = 0

    for char in line:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    result += current_value

# Part 1 Time
print(f"Part 1 result : {result}")
solutionEnd = time.time()
partOneTime = solutionEnd - solutionStart
print(f"Part 1 Time : {partOneTime}")

#---------------------------------------------------------------------------------------------------------------
# Part 2 !
#---------------------------------------------------------------------------------------------------------------
solutionStart = time.time()

result = 0

boxes = [ [] for _ in range(256) ]

for line in lines:
    box_number = 0
    i = 0

    label = ""
    value = 0

    for char in line:
        if char == "=" or char == "-":
            label = line[:i]
        
        if char == "=":
            value = int(line[i+1:])
            placed = False
            for lenses in boxes[box_number]:
                if lenses[0] == label:
                    lenses[1] = value
                    placed = True
                    break
                
            if placed == False:
                boxes[box_number].append([label, value])

        if char == "-":
            for i in range(len(boxes[box_number])):
                if boxes[box_number][i][0] == label:
                    del(boxes[box_number][i])
                    break

        box_number += ord(char)
        box_number *= 17
        box_number = box_number % 256

        i+=1

    #print(f"line {line} should go in {box_number}")

for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        result += (i+1) * (j+1) * boxes[i][j][1]


# Part 2 Time
print(f"Part 2 result : {result}")
solutionEnd = time.time()
partTwoTime = solutionEnd - solutionStart
print(f"Part 2 Time : {partTwoTime}")

#---------------------------------------------------------------------------------------------------------------
# Time !
#---------------------------------------------------------------------------------------------------------------

totalTime = partOneTime + partTwoTime
print(f"Total Time: {totalTime}")