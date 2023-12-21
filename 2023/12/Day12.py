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
day = 12

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
    data = line.split(" ")[0]
    numbers = line.split(" ")[1].split(",")

    #print(f"analyzing line {lines[x]}")

    dataBis = []

    questionsMarkIndexes = []
    max_number = 0

    for i in range(len(data)):
        char = data[i]
        dataBis.append(char)
        if char == "?":
            questionsMarkIndexes.append(i)

    max_number = 2 ** len(questionsMarkIndexes)

    bits_max_number = len(bin(max_number))-2
    
    for j in range(max_number):
        bin_number = bin(j)[2:]

        if len(bin_number) < bits_max_number:
            diff = bits_max_number - len(bin_number) - 1
            bin_number = "0" * diff + str(bin_number)
        
        #print(f"j {j} and bin_number {bin_number}")

        text = bin_number.replace("1","#").replace("0",".")

        #print(f"j {j} and bin_number {text}")

        for k in range(len(text)):
            #print(k)
            dataBis[questionsMarkIndexes[k]] = text[k]

        
        dataFinal = "".join(dataBis).split(".")
        dataFinalFinal = [x for x in dataFinal if x!=""]

        #print(f"analyzing combinaison {dataBis} with {dataFinalFinal} and {numbers}")


        good_combinaison = True
        if len(dataFinalFinal) == len(numbers):
            for z in range(len(dataFinalFinal)):
                if len(dataFinalFinal[z]) == int(numbers[z]):
                    continue
                else:
                    good_combinaison = False
                    break
        else:
            good_combinaison = False

        if good_combinaison:
            result += 1

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

dataFull = []

for line in lines:
    datatrois = ""
    numberstrois = ""
    data = line.split(" ")[0]
    numbers = line.split(" ")[1]

    for i in range(5):
        datatrois += (data + "?")
        numberstrois += (numbers + ",")

    dataFull.append(datatrois[:-1] + " " + numberstrois[:-1])

for line in dataFull:
    data = line.split(" ")[0]
    numbers = line.split(" ")[1].split(",")

    #print(f"analyzing line {lines[x]}")

    dataBis = []

    questionsMarkIndexes = []
    max_number = 0

    for i in range(len(data)):
        char = data[i]
        dataBis.append(char)
        if char == "?":
            questionsMarkIndexes.append(i)

    max_number = 2 ** len(questionsMarkIndexes)

    bits_max_number = len(bin(max_number))-2
    
    for j in range(max_number):
        bin_number = bin(j)[2:]

        if len(bin_number) < bits_max_number:
            diff = bits_max_number - len(bin_number) - 1
            bin_number = "0" * diff + str(bin_number)
        
        #print(f"j {j} and bin_number {bin_number}")

        text = bin_number.replace("1","#").replace("0",".")

        #print(f"j {j} and bin_number {text}")

        for k in range(len(text)):
            #print(k)
            dataBis[questionsMarkIndexes[k]] = text[k]

        
        dataFinal = "".join(dataBis).split(".")
        dataFinalFinal = [x for x in dataFinal if x!=""]

        #print(f"analyzing combinaison {dataBis} with {dataFinalFinal} and {numbers}")


        good_combinaison = True
        if len(dataFinalFinal) == len(numbers):
            for z in range(len(dataFinalFinal)):
                if len(dataFinalFinal[z]) == int(numbers[z]):
                    continue
                else:
                    good_combinaison = False
                    break
        else:
            good_combinaison = False

        if good_combinaison:
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