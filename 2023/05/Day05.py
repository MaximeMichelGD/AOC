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
import sys

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 5

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

seedsStart = lines[0][6:len(lines[0])].strip().split()
bloc_step = -1

seedsEnd = []

for i in range(len(seedsStart)):
    seeds = []
    seed = int(seedsStart[i])
    seeds.append(seed)
    seedsEnd.append(seeds) #On crée une liste de seeds type: [[79], [14], [55], [13]], ca va permettre de gérer l'ajout d'étape => [[79, 81], [14, 14], [55, 55], [13, 13]]

# Part 1
for i in range(2,len(lines)):
    line = lines[i].strip().split()

    if line == [] or i == len(lines)-1: # On passe à une ligne vide ou la dernière valeure de la data, donc un nouveau bloc, on check si chaque valeur précédente a pu obtenir une valeur
        #print(f"Checking if all seeds had a value added")
        for j in range(len(seedsStart)):
            #print(f"Checking for seed {seedsEnd[j]} with a len of {len(seedsEnd[j])} and a check if < to bloc_step +1 {bloc_step +2} ")
            if len(seedsEnd[j]) < bloc_step +2:
                seedsEnd[j].append(seedsEnd[j][-1])
        continue

    if not line[0].isnumeric():
        bloc_step += 1
        continue

    # Ici on check que la seed en cours, donc 1ère itération = 79, est dans la range des seeds concernées par la ligne
    # Ligne 1 de l'exemple: 98 + 2 => de 98 à 99 donc 79 non
    # Ligne 2 de l'exemple: 50 + 48 => de 50 à 97 donc 79 oui ==> On applique donc à 79 la correspondance de source - destination => 52 - 50 = 2. La seed 79 a donc une correspondance 81
    for k in range(len(seedsStart)):
        # print(f"k {k}")
        if seedsEnd[k][bloc_step] <= (int(line[1]) + int(line[2]) - 1) and seedsEnd[k][bloc_step] >= int(line[1]):
            seedsDestination = seedsEnd[k][bloc_step] + int(line[0]) - int(line[1])
            seedsEnd[k].append(seedsDestination)

result = 99999999999999999
for i in range(len(seedsEnd)):
    if seedsEnd[i][-1] < result:
        result = seedsEnd[i][-1]

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

seeds = []

seedsLine = lines[0].split(": ")[1].split(" ")

firstSeed = 0
for i in range(len(seedsLine)):
    if i % 2 == 0:
        firstSeed = int(seedsLine[i])
    else:
        seedRange = [0,0]
        seedRange[0] = firstSeed
        seedRange[1] = firstSeed + int(seedsLine[i])
        seeds.append(seedRange)

minimum = 0
current_score = 0
seedsToDelete = []
seedsConverted = []

for i in range(2,len(lines)):
    line = lines[i].split()
    #print(line)
    
    if line == [] or i == len(lines)-1:	# Nouveau bloc
        for k in range(len(seedsConverted)):
            seeds.append(seedsConverted[k])
        
        seedsConverted = []
        continue
    
    if not line[0].isnumeric():
        continue
			
    if line[0].isnumeric() and seedsToDelete != []:		# On veut supprimer des seeds à analyser les seeds déjà analysées
        seedsToDeleteBis = list(reversed(seedsToDelete))
        for seedToDelete in seedsToDeleteBis:	# on parcours en reverse car si on doit supprimer index 2 et 3 d'une liste [0,1,2,3,4], en supprimant index 2 donc 2, l'index 3 qu'on voulait supp au départ qui était 3, devient le chiffre 4 dans la nouvelle liste
		    # On supprime donc d'abord l'index 3 puis l'index 2
            del(seeds[int(seedToDelete[0])])

        seedsToDelete = []
        
    for j in range(len(seeds)):
        if (seeds[j][0] >= int(line[1]) and seeds[j][0] <= int(line[1]) + int(line[2])) and (seeds[j][1] >= int(line[1]) and seeds[j][1] <= int(line[1]) + int(line[2])):	# La deuxième seed de la range est comprise dans la range de la data
			
            seeds[j][0] += int(line[0]) - int(line[1])
            seeds[j][1] += int(line[0]) - int(line[1])
            if seeds[j][0] > seeds[j][1]:
                seeds[j][0], seeds[j][1] = seeds[j][1], seeds[j][0]
            seedsConverted.append(seeds[j])
            seedsToDelete.append([j])
			
        elif (seeds[j][0] >= int(line[1]) and seeds[j][0] <= int(line[1]) + int(line[2])) and (seeds[j][1] >= int(line[1]) and seeds[j][1] > int(line[1]) + int(line[2])):	# La première seed de la range, la deuxième dépasse
            rangeConverted =[0,0]
			
            rangeConverted[0] = seeds[j][0] + int(line[0]) - int(line[1])
            rangeConverted[1] = int(line[0]) + int(line[2])
            if rangeConverted[0] > rangeConverted[1]:
                rangeConverted[0], rangeConverted[1] = rangeConverted[1], rangeConverted[0]
            
            seeds[j][0] = int(line[1]) + int(line[2]) + 1

            if seeds[j][0] > seeds[j][1]:
                seeds[j][0], seeds[j][1] = seeds[j][1], seeds[j][0]
			
            seedsConverted.append(rangeConverted)
			
        elif (seeds[j][1] >= int(line[1]) and seeds[j][1] <= int(line[1]) + int(line[2])):	# La deuxième seed de la range est comprise dans la range de la data, donc la première doit dépasser puisqu'elle n'est pas comprise dans le 1er bloc
            rangeConverted =[0,0]
			
            rangeConverted[0] = int(line[0])
            rangeConverted[1] = seeds[j][1] + int(line[0]) - int(line[1])

            if rangeConverted[0] > rangeConverted[1]:
                rangeConverted[0], rangeConverted[1] = rangeConverted[1], rangeConverted[0]
			
            seeds[j][1] = int(line[1]) - 1

            if seeds[j][0] > seeds[j][1]:
                seeds[j][0], seeds[j][1] = seeds[j][1], seeds[j][0]
			
            seedsConverted.append(rangeConverted)
			
        elif seeds[j][0] <= int(line[1]) and seeds[j][1] >= int(line[1]) + int(line[2]):
            #nothing
            rangeConverted =[0,0]
            newRange =[0,0]
			
            rangeConverted[0] = int(line[0])
            rangeConverted[1] = int(line[0]) + int(line[2])

            if rangeConverted[0] > rangeConverted[1]:
                rangeConverted[0], rangeConverted[1] = rangeConverted[1], rangeConverted[0]
            
            newRange[0] = int(line[1]) + int(line[2]) + 1
            newRange[1] = seeds[j][1]

            if newRange[0] > newRange[1]:
                newRange[0], newRange[1] = newRange[1], newRange[0]
			
            seeds[j][1] = int(line[1]) - 1

            if seeds[j][0] > seeds[j][1]:
                seeds[j][0], seeds[j][1] = seeds[j][1], seeds[j][0]
			
            seedsConverted.append(rangeConverted)
            seeds.append(newRange)

result = 99999999999999
for x in range(len(seeds)):
    if seeds[x][0] <= result:
        result = seeds[x][0]

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