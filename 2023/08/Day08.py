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
from functools import reduce

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

lst = ""
if realDataSet:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").read().strip()
else:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\dataexemplepart2.txt", "r").read().strip()

lines = [x for x in lst.split('\n')]

solutionStart = time.time()

result = 0

map = dict()
startingPaths = []

for line in lines[2:]: # On met en forme la data pour pouvoir la traiter + facilement
    #line = lines[i].strip().split()
    line = line.split(" = ")
    line[1] = line[1].strip("(").strip(")").split(", ")

    map[line[0]] = line[1]

    if line[0][2] == "A":
        startingPaths.append(line[0])

current_block = "AAA"
result = 0
j = 0
steps = lines[0].strip()
all_arrived = False
test = 1

multipliers = set()

for i in range(len(startingPaths)):
    j = 0
    multiplier = 0
    current_block = startingPaths[i]
    while current_block[2] != "Z":
        if lines[0][j % len(steps)] == "L": # Check if current block = instruction map
            current_block = map[current_block][0]
        else:
            current_block = map[current_block][1]
        
        j += 1
        multiplier += 1
    
    multipliers.add(multiplier)

result = 1

def pgcd(a,b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b,r)

def lcm(a,b):
    return a * b // pgcd(a,b)

result = reduce(lambda x, y:lcm(x,y), multipliers)

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