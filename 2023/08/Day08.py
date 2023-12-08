#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 07
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 8

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

instructions = []

for i in range(2,len(lines)): # On met en forme la data pour pouvoir la traiter + facilement
    #line = lines[i].strip().split()
    line = lines[i].split(" = ")
    line[1] = line[1].strip("(").strip(")").split(", ")

    instructions.append(line)

current_block = "AAA"
values = {"L": 0, "R": 1}
result = 0
j = -1

while current_block != "ZZZ":
    j+=1
    for k in range(len(instructions)):
        if current_block == instructions[k][0]: # Check if current block = instruction map
            current_block = instructions[k][1][values[lines[0][j]]]
            result += 1
            break
        
        if current_block == "ZZZ":
            break

    if current_block == "ZZZ":
        break

    if j == len(lines[0])-1:
        j = -1
    
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

for i in range(len(lines)):
    line = lines[i].split()
    #print(line)


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