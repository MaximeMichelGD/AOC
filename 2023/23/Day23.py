#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 23
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time
from collections import deque

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 23

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

ROWS = len(lines) - 1
COLUMNS = len(lines[0]) - 1

print(f"rows {ROWS} and columns {COLUMNS}")

starting_point = [0,1]
ending_point = (ROWS,COLUMNS-1)

grid = []

for r in range(len(lines)):
    line = []
    for c in range(len(lines[r])):
        line.append(lines[r][c])
        # if lines[r][c] == "S":
        #     starting_point = [r,c]
    grid.append(line)

Q = deque([(0, 1, 0,-1)]) #r,c,num_step, dir

dir_arrow = {"<" : [0,-1,0], ">": [0,1,1], "^": [-1,0,2], "v": [1,0,3]} # r, c, dir

while Q:
    r,c,num_step,direction = Q.popleft()
    #print(f"r {r}, c {c} grid = {grid[r][c]},num_step {num_step}")

    if (r,c) == ending_point:
        #print(f"arrived in {num_step} steps")
        if num_step > result:
            result = num_step
        continue

    new_step = num_step + 1
    
    if grid[r][c] == "<" or grid[r][c] == ">" or grid[r][c] == "^" or grid[r][c] == "v":
        new_r = r + dir_arrow[grid[r][c]][0]
        new_c = c + dir_arrow[grid[r][c]][1]
        if (direction == 0 and dir_arrow[grid[r][c]][2] == 1) or (direction == 1 and dir_arrow[grid[r][c]][2] == 0) or (direction == 2 and dir_arrow[grid[r][c]][2] == 3) or (direction == 3 and dir_arrow[grid[r][c]][2] == 2):
            continue
        else:
            Q.append((new_r,new_c,new_step, dir_arrow[grid[r][c]][2]))
    else:
        for i, dir in enumerate([[0,-1], [0,1], [-1,0], [1,0]]): # r c
            new_r = r + dir[0]
            new_c = c + dir[1]

            if 0<=new_r<=ROWS and 0<=new_c<=COLUMNS and lines[new_r][new_c] != "#":
                if (direction == 0 and i == 1) or (direction == 1 and i == 0) or (direction == 2 and i == 3) or (direction == 3 and i == 2):
                    continue
                else:
                    Q.append((new_r,new_c,new_step, i))

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if (i,j) in unique_positions:
#             grid[i][j] = "0"
#     print(grid[i])

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

Q = deque([(0, 1, 0,-1, [[0,0]])]) #r,c,num_step, dir, path

visited = dict()

while Q:
    r,c,num_step,direction, path = Q.popleft()
    #print(f"r {r}, c {c} grid = {grid[r][c]},num_step {num_step}, path {path}")

    if (r,c) in visited:
        if visited[r,c] >= num_step:
            continue
        else:
            visited[r,c] = num_step

    if (r,c) == ending_point:
        print(f"arrived in {num_step} steps. Still {len(Q)} paths in course")
        if num_step > result:
            result = num_step
        continue

    if [r,c] in path:
        continue

    new_step = num_step + 1

    for i, dir in enumerate([[0,-1], [0,1], [-1,0], [1,0]]): # r c
        new_r = r + dir[0]
        new_c = c + dir[1]

        if 0<=new_r<=ROWS and 0<=new_c<=COLUMNS and lines[new_r][new_c] != "#":
            if (direction == 0 and i == 1) or (direction == 1 and i == 0) or (direction == 2 and i == 3) or (direction == 3 and i == 2):
                continue
            else:
                Q.append((new_r,new_c,new_step, i, path + [[r,c]]))


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