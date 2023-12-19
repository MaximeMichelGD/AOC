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


# Set realDataSet to True to test with real dataset
realDataSet = True
day = 18

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
lines = [x for x in lst.split('\n')]

result = 0

xPosition = yPosition = 0
minxPosition = minyPosition = maxxPosition = maxyPosition = 0

for line in lines:
    direction, length, color = line.split(" ")
    length = int(length)

    if direction == "U":
        yPosition += length
    elif direction == "D":
        yPosition -= length
    elif direction == "L":
        xPosition -= length
    elif direction == "R":
        xPosition += length
    else:
        print("Bug")
    
    if xPosition < minxPosition:
        minxPosition = xPosition

    if xPosition > maxxPosition:
        maxxPosition = xPosition

    if yPosition < minyPosition:
        minyPosition = yPosition
    
    if yPosition > maxyPosition:
        maxyPosition = yPosition
    
#print(f"xMin: {minxPosition} xMax: {maxxPosition} - yMin: {minyPosition} yMax: {maxyPosition}")

current_point = [abs(minxPosition),abs(maxyPosition)]

def DefineNewPoint(direction, point, length):
    if direction == "U" or direction == "3":
        point[1] -= length
    elif direction == "D" or direction == "1":
        point[1] += length
    elif direction == "L" or direction == "2":
        point[0] -= length
    elif direction == "R" or direction == "0":
        point[0] += length
    else:
        print("Bug, direction was not of U, D, L or R. Check your data")
    
    return point

vertices = []

perimeter = 0

for line in lines:
    direction, length, color = line.split(" ")
    length = int(length)
    perimeter += length

    current_point = DefineNewPoint(direction, current_point, length)

    vertices.append([current_point[0],current_point[1]])

a_sum = 0
b_sum = 0
for j in range(len(vertices)):
    if j == len(vertices) - 1:
        a_sum += (vertices[j][0] * vertices[0][1])
        b_sum += (vertices[j][1] * vertices[0][0])
    else:
        a_sum += (vertices[j][0] * vertices[j+1][1])
        b_sum += (vertices[j][1] * vertices[j+1][0])


result = (a_sum - b_sum) / 2 + perimeter / 2 + 1

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

result = 0

xPosition = yPosition = 0
minxPosition = minyPosition = maxxPosition = maxyPosition = 0

for line in lines:
    line = line.split(" ")
    length = int(line[2][2:-2],16)
    
    direction = line[2][-2:-1]
    
    #print(f"{direction} {length}")

    if direction == "3": # Up
        yPosition += length
    elif direction == "1": # Down
        yPosition -= length
    elif direction == "2": # Left
        xPosition -= length
    elif direction == "0": # Right
        xPosition += length
    else:
        print("Bug")
    
    if xPosition < minxPosition:
        minxPosition = xPosition

    if xPosition > maxxPosition:
        maxxPosition = xPosition

    if yPosition < minyPosition:
        minyPosition = yPosition
    
    if yPosition > maxyPosition:
        maxyPosition = yPosition

vertices = []

perimeter = 0

for line in lines:
    line = line.split(" ")
    length = int(line[2][2:-2],16)
    direction = line[2][-2:-1]

    perimeter += length

    current_point = DefineNewPoint(direction, current_point, length)
    
    vertices.append([current_point[0],current_point[1]])

a_sum = 0
b_sum = 0
for j in range(len(vertices)):
    if j == len(vertices) - 1:
        a_sum += (vertices[j][0] * vertices[0][1])
        b_sum += (vertices[j][1] * vertices[0][0])
    else:
        a_sum += (vertices[j][0] * vertices[j+1][1])
        b_sum += (vertices[j][1] * vertices[j+1][0])


result = (a_sum - b_sum) / 2 + perimeter / 2 + 1

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