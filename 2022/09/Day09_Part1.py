import os
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

#For simplification in code comments and in code variables: T = tail, H = head

#Defining starting position of x = 0 and y = 0
hPosition = [0,0]
tPosition = [0,0]

def Mooving(direction, position):
        if direction == "R":
            position[0] += 1
        elif direction == "L":
            position[0] -= 1
        elif direction == "U":
            position[1] += 1
        elif direction == "D":
            position[1] -= 1
        return position

positionsVisitedOnce = set()

for i in range(lines):
    instruction = list(lst[i].split())
    #print(instruction)

    direction = instruction[0]
    length = int(instruction[1])

    for j in range(length):
        hPosition = Mooving(direction, hPosition)

        #print(f"h is in {hPosition} and t is in {tPosition}")

        #checking if H over T
        if hPosition == tPosition:
            #print(f"h is in {hPosition} and t is in {tPosition}")
            #We do not moove T
            positionsVisitedOnce.add(tuple(tPosition))
            continue

        distance = [h_elt - t_elt for t_elt, h_elt in zip(tPosition, hPosition)]

        totalDistance = abs(distance[0]) + abs(distance[1])

        if totalDistance == 1:
            #It means T is already just behind H
            #print(f"h is in {hPosition} and t is in {tPosition}")
            positionsVisitedOnce.add(tuple(tPosition))
            continue
        elif totalDistance == 2:
            #It means H is either in diagonal of T, or mooving in a direction that T needs to follow

            #checking if H in diagonal of T
            if hPosition[0] != tPosition[0] and hPosition[1] != tPosition[1]:
                #We do not moove T
                #print(f"h is in {hPosition} and t is in {tPosition}")
                positionsVisitedOnce.add(tuple(tPosition))
                continue

            #checking if H in same line or column of T
            if hPosition[0] == tPosition[0] or hPosition[1] == tPosition[1]:
                #It means H is moving in same line or column as T, so we need to apply same moovement to T
                tPosition = Mooving(direction, tPosition)
                positionsVisitedOnce.add(tuple(tPosition))
                #print(f"h is in {hPosition} and t is in {tPosition}")
                continue

        elif totalDistance == 3:
            #It means H is in diagonal AND 1 step away from T, so T needs 1 moovement in both axis to get back to H
            xDifference = hPosition[0] - tPosition[0]
            yDifference = hPosition[1] - tPosition[1]
            if xDifference == 2 or xDifference == -2:
                #it means H is 2 step away in x axis from T, T needs to moove 1 step in x axis
                tPosition[0] += int(xDifference/2)
                tPosition[1] = hPosition[1]
                positionsVisitedOnce.add(tuple(tPosition))
                #print(f"h is in {hPosition} and t is in {tPosition}")
                continue
            elif yDifference == 2 or yDifference == -2:
                tPosition[1] += int(yDifference/2)
                tPosition[0] = hPosition[0]
                positionsVisitedOnce.add(tuple(tPosition))
                #print(f"h is in {hPosition} and t is in {tPosition}")


#print(positionsVisitedOnce)
print(f"answer is {len(positionsVisitedOnce)}")