#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 09
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time
from collections import deque

# Set realDataSet to True to test with real dataset
realDataSet = False
day = 10

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

# Directions = [x,y] => need to apply a direction. For example, | means we can go either north or south, so the -1 in y needs to stay -1 if going north to south, but 1 if going south to north
directions = {"|": [0,-1], "-": [1,0], "L": [1,-1], "J": [-1,-1], "7": [-1,1], "F": [1,1]}

G = []
for line in lines:
    G.append(line)
R = len(G)
C = len(G[0])

starting_pos = tuple((0,0))

E = [[-1 for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if G[r][c]=='S':
            E[r][c] = 0
            starting_pos = (r,c)


def GottaGoSanta():
    Q = deque()
    Q.append((starting_pos, 0)) # We start with starting point


    S = set() 
    while Q:
        (r,c),d = Q.popleft()
        if (r,c) in S: # Position already seen? If yes continue to next Q
            continue
        S.add((r,c))

        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c+dc

GottaGoSanta()

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