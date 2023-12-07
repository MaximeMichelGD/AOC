#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 05
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 4

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

# Part 1
for i in range(len(lines)):
    line = lines[i].strip()

    cardSeparatorIndex = line.find(":")
    numbersSeparatorIndex = line.find(" | ")

    winningNumbers = line[cardSeparatorIndex+2:numbersSeparatorIndex]
    winningNumbers = winningNumbers.split()

    gotNumbers = line[numbersSeparatorIndex+2:len(line)]
    gotNumbers = gotNumbers.split()

    firstMatch = True
    points = 0

    for number in gotNumbers:
        if number in winningNumbers:
            if not firstMatch:
                points *= 2
                continue
            else:
                points = 1
                firstMatch = False

    result += points

print(f"Part 1 result : {result}")
solutionEnd = time.time()
partOneTime = solutionEnd - solutionStart
print(f"Part 1 Time : {partOneTime}")

#---------------------------------------------------------------------------------------------------------------
# Part 2 !
#---------------------------------------------------------------------------------------------------------------
solutionStart = time.time()

cardSeparatorIndex = lines[-1].find(":")
cardMax = int(lines[-1][5:cardSeparatorIndex])

result = 0
copies = {}

for i in range(len(lines)):
    line = lines[i].strip()

    cardSeparatorIndex = line.find(":")
    numbersSeparatorIndex = line.find(" | ")

    cardNumber = int(line[5:cardSeparatorIndex])

    winningNumbers = line[cardSeparatorIndex+2:numbersSeparatorIndex]
    winningNumbers = winningNumbers.split()

    gotNumbers = line[numbersSeparatorIndex+2:len(line)]
    gotNumbers = gotNumbers.split()

    try:
        currentCopies = copies[cardNumber] + 1
    except:
        currentCopies = 1

    copies[cardNumber] = currentCopies # Permet d'updater de suite le nombre de copies de la carte en cours

    matching = 0
    for number in gotNumbers:
        if number in winningNumbers:
            matching += 1

    # On a récup le nombre de matching numbers pour la ligne
    # On doit donc générer autant de copies de cartes concernées. Si 2 matching dans n, on génère 1 copie de n+1 et 1 copie de n+2
    # Dans tous les cas on génère 1 copie de n => généré par le try except ci-dessus
        
    for j in range(1,matching+1):
        try:
            copies[cardNumber+j] += 1 * currentCopies
        except:
            if cardNumber+j <= cardMax:
                copies[cardNumber+j] = 1 * currentCopies

result = sum(copies.values())
    
print(f"Part 2 result : {result}")

solutionEnd = time.time()
partTwoTime = solutionEnd - solutionStart
print(f"Part 2 Time : {partTwoTime}")

#---------------------------------------------------------------------------------------------------------------
# Time !
#---------------------------------------------------------------------------------------------------------------

totalTime = partOneTime + partTwoTime
print(f"Total Time: {totalTime}")