#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 08
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time
from functools import reduce

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 6

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

result = 1

times = lines[0].strip(": ").split()[1:]
distances = lines[1].strip(": ").split()[1:]

timesBeat = []

for i in range(len(times)):
    waysToBeat = 0

    timeRace = int(times[i])
    distanceRecord = int(distances[i])

    for j in range(1,timeRace+1):
        hold = j
        leftToRace = timeRace - hold

        distanceMade = hold * leftToRace

        if distanceMade > distanceRecord:
            waysToBeat += 1
    
    timesBeat.append(waysToBeat)
            
for times in timesBeat:
    result *= times

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

times = lines[0].strip(": ").split()[1:]
distances = lines[1].strip(": ").split()[1:]

timesBeat = []
waysToBeat = 0

if realDataSet:
    timeRace = int(times[0]+times[1]+times[2]+times[3])
    distanceRecord = int(distances[0]+distances[1]+distances[2]+distances[3])
else:
    timeRace = int(times[0]+times[1]+times[2])
    distanceRecord = int(distances[0]+distances[1]+distances[2])

for j in range(1,timeRace+1):
    hold = j
    leftToRace = timeRace - hold

    distanceMade = hold * leftToRace

    if distanceMade > distanceRecord:
        result += 1



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