#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 21
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time
from collections import deque

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 21

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

NUMBER_STEP = 64

ROWS = len(lines) - 1
COLUMNS = len(lines[0]) - 1

print(f"rows {ROWS} and columns {COLUMNS}")

starting_point = []

grid = []

for r in range(len(lines)):
    line = []
    for c in range(len(lines[r])):
        line.append(lines[r][c])
        if lines[r][c] == "S":
            starting_point = [r,c]
    grid.append(line)

Q = deque([(starting_point[0], starting_point[1], 0, 0, -1)]) #r,c, number_step, distance, direction

unique_positions = set()

visited = set()

while Q:
    r,c,num_step,distance,direction = Q.popleft()
    #print(f"r {r},c {c},num_step {num_step}, distance {distance}, direction {direction}")

    if (num_step % 2 == 0 and num_step > 0):
        unique_positions.add((r,c))
        if num_step >= NUMBER_STEP:
        #print(f"Q continued because {num_step >= NUMBER_STEP}")
            continue
    
    if distance < num_step:
        continue

    if (r,c) in visited:
        continue
    else:
        visited.add((r,c))
    
    for i, dir in enumerate([[0,1], [0,-1], [1,0], [-1,0]]): # r c
        new_r = r + dir[0]
        new_c = c + dir [1]

        if (direction == 0 and i == 1) or (direction == 1 and i == 0) or (direction == 2 and i == 3) or (direction == 3 and i == 2):
            new_dist = distance - 1
        else:
            new_dist = distance + 1

        if new_dist < (num_step + 1):
            continue
        
        if 0<=new_r<=ROWS and 0<=new_c<=COLUMNS and lines[new_r][new_c] != "#":
            Q.append((new_r,new_c,num_step+1, new_dist, i))

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if (i,j) in unique_positions:
#             grid[i][j] = "0"
#     print(grid[i])

result = len(unique_positions) + 1

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