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

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 9

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

for line in lines:
    line = line.strip().split(" ")
    
    sequences = []
    sequences.append(line)
    not_found = True
    current_number = 0
    current_number += int(line[-1])

    i = 0

    while not_found:
        new_sequence = []
        for j in range(1,len(sequences[i])):
            new_sequence.append(int(sequences[i][j]) - int(sequences[i][j-1]))
        
        current_number += new_sequence[-1] # Censé être que des int
        
        if len(set(new_sequence)) == 1: # La new_sequence a déterminé un seul nombre, peu importe que ce soit 0 ou non, on sait que c'est le chiffre a remonté
            not_found = False
            result += current_number
            break
        else:
            sequences.append(new_sequence)
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

for line in lines:
    line = line.strip().split(" ")
    
    sequences = []
    sequences.append(line)
    not_found = True
    current_number = 0
    current_number += int(line[0])

    i = 0

    while not_found:
        new_sequence = []
        for j in range(1,len(sequences[i])):
            new_sequence.append(int(sequences[i][j]) - int(sequences[i][j-1]))
        
        if i % 2 == 0:
            current_number -= new_sequence[0]
        else: 
            current_number += new_sequence[0]

        if len(set(new_sequence)) == 1: # La new_sequence a déterminé un seul nombre, peu importe que ce soit 0 ou non, on sait que c'est le chiffre a remonté
            sequences.append(new_sequence)
            not_found = False
            result += current_number
            break
        else:
            sequences.append(new_sequence)
            i += 1

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