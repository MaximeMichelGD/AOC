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
day = 14

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

grid_rocks = [list(ligne) for ligne in lines]

for i in range(len(grid_rocks)):
    for j in range(len(grid_rocks[i])):
        #print(f"i {i} - j {j}")
        cell = grid_rocks[i][j]

        if cell == "O":
            if i == 0:
                result += len(grid_rocks) - i
                #print(f"rock of [i,j] {i, j} added {len(grid_rocks) - i} points")
                continue
            else:
                if str(grid_rocks[i-1][j]).isnumeric():
                    toMoove = grid_rocks[i-1][j]

                    #print(f"rock of [i,j] {i, j} {grid_rocks[i][j]} mooved to {i-toMoove, j} and added {len(grid_rocks) - (i - toMoove)} points")

                    grid_rocks[i-toMoove][j] = "O"
                    grid_rocks[i][j] = toMoove
                    result += len(grid_rocks) - (i - toMoove)

                elif grid_rocks[i-1][j] == "O" or grid_rocks[i-1][j] == "#":
                    #print(f"rock of [i,j] {i, j} added {len(grid_rocks) - i} points")
                    result += len(grid_rocks) - i
        
        elif cell == ".":
            if i == 0:
                grid_rocks[i][j] = 1
            else:
                if grid_rocks[i-1][j] == "#" or grid_rocks[i-1][j] == "O":
                    grid_rocks[i][j] = 1
                else: # Pb a corrigé ici
                    grid_rocks[i][j] = grid_rocks[i-1][j] + 1


# for line in grid_rocks:
#     print(line)

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