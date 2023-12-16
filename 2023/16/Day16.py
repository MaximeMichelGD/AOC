#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 16
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time
from collections import deque

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 16

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

pointsVisited = set() # On initie position de départ et les points visités qui vont venir s'agrémenter uniquement des positions non déjà vue grâce au set
pointsVisitedDirection = set()
startingPoint = (0,-1) # y,x
beams = deque()

direction = (0,1) # y,x
beams.append((startingPoint, direction))
pointsVisitedDirection.add((startingPoint, direction))

lenGrid = len(lines)

def ValidPoint(input): # Le but est de vérifier qu'on reste dans les limites de la grille => 0,0 ok, 5,5 ok, -1,5 non, 5,10 non
    if input[0] > -1 and input[0] < len(lines) and input[1] > -1 and input[1] < len(lines):
        return True

while beams:
    p,d = beams.popleft() # On récupère position (p) beams et sa direction (d)

    if ValidPoint(p):
        pointsVisited.add(p)
        
    a = (p[0] + d[0], p[1] + d[1])

    if (a,d) in pointsVisitedDirection: # Permet de ne pas traiter la beam si sa position est direction ont déjà été ajoutées (on va refaire un chemin déjà fait sinon)
        continue

    if ValidPoint(a):
        pointsVisited.add(a)
        pointsVisitedDirection.add((a, d))
    else:
        continue

    if lines[a[0]][a[1]] == ".": # On continue dans la même direction et on update la position à la position courante
        if ValidPoint(a):
            beams.append((a, d))
        continue

    elif lines[a[0]][a[1]] == "|":
        if d[1] == 1 or d[1] == -1 and d[0] == 0: # On arrive de face, donc on split en 2
            dOne = (-1,0)
            dTwo = (1,0)

            if ValidPoint(a):
                beams.append((a, dOne))
            
            if ValidPoint(a):
                beams.append((a, dTwo))
        
        else: # On continue dans la même direction
            if ValidPoint(a):
                beams.append((a, d))

    elif lines[a[0]][a[1]] == "-":
        if d[1] == 1 or d[1] == -1 and d[0] == 0: # On arrive de côté, donc on continue dans la direction
            if ValidPoint(a):
                beams.append((a, d))

        else: # On arrive de face donc on split en 2
            dOne = (0,-1)
            dTwo = (0,1)

            if ValidPoint(a):
                beams.append((a, dOne))
            
            if ValidPoint(a):
                beams.append((a, dTwo))
            
    elif lines[a[0]][a[1]] == "/":
        if d[1] == 1 and d[0] == 0: # On arrive du côté gauche, donc on va vers le haut
            d = (-1,0)

            if ValidPoint(a):
                beams.append((a, d))
        
        elif d[1] == -1 and d[0] == 0: # On arrive du côté droit, donc on va vers le bas
            d = (1,0)

            if ValidPoint(a):
                beams.append((a, d))
        
        elif d[1] == 0 and d[0] == 1: # On arrive du haut, donc on va à gauche
            d = (0,-1)

            if ValidPoint(a):
                beams.append((a, d))
        
        elif d[1] == 0 and d[0] == -1: # On arrive du bas, donc on va à droite
            d = (0,1)

            if ValidPoint(a):
                beams.append((a, d))

    elif lines[a[0]][a[1]] == "\\":
        if d[1] == 1 and d[0] == 0: # On arrive du côté gauche, donc on va vers le bas
            d = (1,0)
            if ValidPoint(a):
                beams.append((a, d))
        
        elif d[1] == -1 and d[0] == 0: # On arrive du côté droit, donc on va vers le haut
            d = (-1,0)

            if ValidPoint(a):
                beams.append((a, d))
        
        elif d[1] == 0 and d[0] == 1: # On arrive du haut, donc on va à droite
            d = (0,1)

            if ValidPoint(a):
                beams.append((a, d))
        
        elif d[1] == 0 and d[0] == -1: # On arrive du bas, donc on va à gauche
            d = (0,-1)

            if ValidPoint(a):
                beams.append((a, d))
            
        else:
            print("Didnt find any")

result = len(pointsVisited)

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

def ValidPoint(input): # Le but est de vérifier qu'on reste dans les limites de la grille => 0,0 ok, 5,5 ok, -1,5 non, 5,10 non
    if input[0] > -1 and input[0] < len(lines) and input[1] > -1 and input[1] < len(lines):
        return True

startingBeams = []

for i in range(len(lines)):
    left = (i,0)
    top = (0,i)
    right = (i, len(lines)-1)
    bottom = (len(lines)-1,i)
    directionLeft = (0,1)
    directionRight = (0,-1)
    directionTop = (1,0)
    directionBottom = (-1,0)

    startingBeams.append((left, directionLeft))
    startingBeams.append((right, directionRight))
    startingBeams.append((top, directionTop))
    startingBeams.append((bottom, directionBottom))

for beam in startingBeams:

    pointsVisited = set() # On initie position de départ et les points visités qui vont venir s'agrémenter uniquement des positions non déjà vue grâce au set
    pointsVisitedDirection = set()

    beams = deque()
    startingPoint = beam[0] # y,x
    direction = beam[1] # y,x

    beams.append((startingPoint, direction))

    while beams:
        p,d = beams.popleft() # On récupère position (p) beams et sa direction (d)

        if ValidPoint(p):
            pointsVisited.add(p)
            
        a = (p[0] + d[0], p[1] + d[1])

        if (a,d) in pointsVisitedDirection: # Permet de ne pas traiter la beam si sa position est direction ont déjà été ajoutées (on va refaire un chemin déjà fait sinon)
            continue

        if ValidPoint(a):
            pointsVisited.add(a)
            pointsVisitedDirection.add((a, d))
        else:
            continue

        if lines[a[0]][a[1]] == ".": # On continue dans la même direction et on update la position à la position courante
            if ValidPoint(a):
                beams.append((a, d))
            continue

        elif lines[a[0]][a[1]] == "|":
            if d[1] == 1 or d[1] == -1 and d[0] == 0: # On arrive de face, donc on split en 2
                dOne = (-1,0)
                dTwo = (1,0)

                if ValidPoint(a):
                    beams.append((a, dOne))
                
                if ValidPoint(a):
                    beams.append((a, dTwo))
            
            else: # On continue dans la même direction
                if ValidPoint(a):
                    beams.append((a, d))

        elif lines[a[0]][a[1]] == "-":
            if d[1] == 1 or d[1] == -1 and d[0] == 0: # On arrive de côté, donc on continue dans la direction
                if ValidPoint(a):
                    beams.append((a, d))

            else: # On arrive de face donc on split en 2
                dOne = (0,-1)
                dTwo = (0,1)

                if ValidPoint(a):
                    beams.append((a, dOne))
                
                if ValidPoint(a):
                    beams.append((a, dTwo))
                
        elif lines[a[0]][a[1]] == "/":
            if d[1] == 1 and d[0] == 0: # On arrive du côté gauche, donc on va vers le haut
                d = (-1,0)

                if ValidPoint(a):
                    beams.append((a, d))
            
            elif d[1] == -1 and d[0] == 0: # On arrive du côté droit, donc on va vers le bas
                d = (1,0)

                if ValidPoint(a):
                    beams.append((a, d))
            
            elif d[1] == 0 and d[0] == 1: # On arrive du haut, donc on va à gauche
                d = (0,-1)

                if ValidPoint(a):
                    beams.append((a, d))
            
            elif d[1] == 0 and d[0] == -1: # On arrive du bas, donc on va à droite
                d = (0,1)

                if ValidPoint(a):
                    beams.append((a, d))

        elif lines[a[0]][a[1]] == "\\":
            if d[1] == 1 and d[0] == 0: # On arrive du côté gauche, donc on va vers le bas
                d = (1,0)
                if ValidPoint(a):
                    beams.append((a, d))
            
            elif d[1] == -1 and d[0] == 0: # On arrive du côté droit, donc on va vers le haut
                d = (-1,0)

                if ValidPoint(a):
                    beams.append((a, d))
            
            elif d[1] == 0 and d[0] == 1: # On arrive du haut, donc on va à droite
                d = (0,1)

                if ValidPoint(a):
                    beams.append((a, d))
            
            elif d[1] == 0 and d[0] == -1: # On arrive du bas, donc on va à gauche
                d = (0,-1)

                if ValidPoint(a):
                    beams.append((a, d))
                
            else:
                print("Didnt find any")

    count = len(pointsVisited)

    #print(f"beam {beam} got a count of {count}")

    if count > result:
        result = count


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