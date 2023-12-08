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

map = dict()

for i in range(2,len(lines)): # On met en forme la data pour pouvoir la traiter + facilement
    #line = lines[i].strip().split()
    line = lines[i].split(" = ")
    line[1] = line[1].strip("(").strip(")").split(", ")

    map[line[0]] = line[1]

current_block = "AAA"
result = 0
i = 0
steps = lines[0].strip()

while current_block != "ZZZ":
    if lines[0][i % len(steps)] == "L": # Check if current block = instruction map
        current_block = map[current_block][0]
    else:
        current_block = map[current_block][1]

    result += 1
    i += 1

    
# Part 1 Time
print(f"Part 1 result : {result}") # Should be 15 989 (when not optimized, optimizing now)
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