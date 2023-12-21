#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 20
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time
from collections import deque

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 20

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

Q = deque()

starters = []

flipflopsOnOff = dict()
flipflopsLowHigh = dict()
flipflopsStart = dict()
converters = []
conv = dict()
modules = dict()
signals = {True: "low", False: "high"}

for line in lines: # On récupère les flipflops et converters
    line = line.split(" -> ")

    if line[0] == "broadcaster":
        starters = line[1].split(", ")
        modules["broadcaster"] = line[1].split(", ")
    elif line[0][0] == "%":
        flipflopsLowHigh[line[0].split("%")[1]] = "low"
        flipflopsOnOff[line[0].split("%")[1]] = False
        modules[line[0].split("%")[1]] = line[1].split(", ")
    elif line[0][0] == "&":
        converters.append(line[0].split("&")[1])
        modules[line[0].split("&")[1]] = line[1].split(", ")

for line in lines:
    line = line.split(" -> ")
    
    if line[0][0] == "%":
        for elem in line[1].split(", "):
            if elem in converters:
                if elem in conv:
                    conv[elem] = conv[elem] + [line[0].split("%")[1]]
                else:
                    conv[elem] = [line[0].split("%")[1]]
    elif line[0][0] == "&":
        

print(starters)

print(f"modules {modules}")
print(f"flipflopsOnOff {flipflopsOnOff}")
print(f"flipflopsLowHigh {flipflopsLowHigh}")
print(f"converters {converters}")
print(f"conv {conv}")

low_count = 0
high_count = 0

cycle = 0

for i in range(1000):
    cycle += 1
    low_count += 1
    
    for starter in starters:
        Q.append((flipflopsLowHigh[starter],starter))
        
    while Q:
        signal, origin = Q.popleft()
        
        print(signal, origin)
        
        if signal == "high":
            high_count += 1
            inv_signal = "low"
        elif signal == "low":
            low_count += 1
            inv_signal = "high"
            
        if origin in conv:
            if len(conv[origin]) == 1:
                Q.append((inv_signal,modules[origin][0]))
                continue
            else:
                testdeux = True
                for elem in conv[origin]:
                    if flipflopsOnOff[elem] == False:
                        testdeux = False
                        break
                        
                if testdeux:
                    Q.append(("low",modules[origin][0]))
                    continue
                else:
                    Q.append(("high",modules[origin][0]))
                    continue

        if signal == "high":
            continue
        
        if origin not in modules:
            continue
        
        flipflopsLowHigh[origin] = signal
        new_signal = signals[flipflopsOnOff[origin]]
        flipflopsOnOff[origin] = not flipflopsOnOff[origin]

        new_destinations = modules[origin]
        
        for destination in new_destinations:
            Q.append((new_signal, destination))
    
    test = True
    for key,value in flipflopsOnOff.items():
        if value == True:
            test = False
            break
    
    if test:
        break


print(flipflopsLowHigh)
print(flipflopsOnOff)

print(f"result: ({low_count} * 1000 / {cycle}) * ({high_count} * 1000 / {cycle}) = {(low_count * (1000 / cycle)) * (high_count * (1000 / cycle))}")


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