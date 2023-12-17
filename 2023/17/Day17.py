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
realDataSet = False
day = 17

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

grid = [list(line) for line in lines]

ROWS = len(grid)
COLUMNS = len(grid[0])

result = 0

Q = deque([(0,0,0,0,0)]) # Deque: Row, Column, Somme, Dir, CountDir
# Besoin d'avoir un moyen d'identifier précédente direction, afin de ne pas partir à l'inverse (interdit selon l'énoncé) + avoir un moyen d'identifier si déjà 3 fois la même direction

has_a_final_result = False

while Q:
    row,column,sum,direction,countDir = Q.popleft()
    #print(f"r {row}, c {column}, sum {sum}, direction {direction}, countDir {countDir}")

    if row == ROWS and column == COLUMNS:
        has_a_final_result = True
        if sum < result:
            result = sum
            continue
    
    if has_a_final_result:
        if sum >= result:
            continue

    for i, dir in enumerate([[0,1], [0,-1], [1,0], [-1,0]]): # [x,y]

        new_row = row + dir[0]
        new_column = column + dir[1]
        new_sum = sum + int(grid[new_row][new_column])
        if i == direction:
            new_count = countDir + 1
        else:
            new_count = 1
        
        print(f"direction {direction} i {i},   new_count {new_count} and 0 <= {new_row}<={ROWS} and 0<={new_column}<={COLUMNS}")

        if direction == i :
            if new_count <= 3:
                if 0<=new_row<=ROWS and 0<=new_column<=COLUMNS:
                    Q.append([new_row, new_column, new_sum, i, new_count])
        else:
            if 0<=new_row<=ROWS and 0<=new_column<=COLUMNS:
                    Q.append([new_row, new_column, new_sum, i, new_count])


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