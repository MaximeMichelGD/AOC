import os
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

NUMBER_OF_KNOTS = 10

#For simplification in code comments and in code variables: T = tail, H = head

#Defining starting position of x = 0 and y = 0
hPosition = [0,0]
positions = []

for i in range (NUMBER_OF_KNOTS):
    positions.append([0,0])

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
        hPosition = positions[0]
        hPosition = Mooving(direction, hPosition)
        positions[0] = hPosition

        #print("--------")
        #print(f"h is in {hPosition} and t is in {tPosition}")
        for k in range(1,10):
            #checking if H over T

            positionToFollow = positions[k-1]
            currentPosition = positions[k]

            if positionToFollow == currentPosition:
                #print(f"h is in {hPosition} and t is in {tPosition}")
                #We do not moove T
                if k == 9:
                    positionsVisitedOnce.add(tuple(currentPosition))
                    continue

            distance = [h_elt - t_elt for t_elt, h_elt in zip(currentPosition, positionToFollow)]

            totalDistance = abs(distance[0]) + abs(distance[1])

            if totalDistance == 1:
                #It means T is already just behind H
                #print(f"h is in {hPosition} and knot {k} is in {currentPosition}")
                if k == 9:
                    positionsVisitedOnce.add(tuple(currentPosition))
                    continue
            elif totalDistance == 2:
                #It means H is either in diagonal of T, or mooving in a direction that T needs to follow

                #checking if H in diagonal of T
                if positionToFollow[0] != currentPosition[0] and positionToFollow[1] != currentPosition[1]:
                    #We do not moove T
                    #print(f"h is in {hPosition} and knot {k} is in {currentPosition}")
                    if k == 9:
                        positionsVisitedOnce.add(tuple(currentPosition))
                        continue

                #checking if H in same line or column of T
                if positionToFollow[0] == currentPosition[0]:
                    #It means H is moving in same column as T, so we need to apply same moovement to T
                    yDifference = positionToFollow[1] - currentPosition[1]
                    currentPosition[1] += int(yDifference/2)

                    positions[k] = currentPosition
                    #print(f"h is in {hPosition} and knot {k} is in {currentPosition}")
                    if k == 9:
                        positionsVisitedOnce.add(tuple(currentPosition))
                        continue

                elif positionToFollow[1] == currentPosition[1]:
                    #It means H is moving in same line as T, so we need to apply same moovement to T
                    xDifference = positionToFollow[0] - currentPosition[0]
                    currentPosition[0] += int(xDifference/2)

                    positions[k] = currentPosition
                    #print(f"h is in {hPosition} and knot {k} is in {currentPosition}")
                    if k == 9:
                        positionsVisitedOnce.add(tuple(currentPosition))
                        continue

            elif totalDistance == 3:
                #It means H is in diagonal AND 1 step away from T, so T needs 1 moovement in both axis to get back to H
                xDifference = positionToFollow[0] - currentPosition[0]
                yDifference = positionToFollow[1] - currentPosition[1]
                if xDifference == 2 or xDifference == -2:
                    #it means H is 2 step away in x axis from T, T needs to moove 1 step in x axis
                    currentPosition[0] += int(xDifference/2)
                    currentPosition[1] = positionToFollow[1]
                    positions[k] = currentPosition

                    #print(f"h is in {hPosition} and knot {k} is in {currentPosition}")

                    if k == 9:
                        positionsVisitedOnce.add(tuple(currentPosition))
                        continue

                elif yDifference == 2 or yDifference == -2:
                    currentPosition[1] += int(yDifference/2)
                    currentPosition[0] = positionToFollow[0]
                    positions[k] = currentPosition

                    #print(f"h is in {hPosition} and knot {k} is in {currentPosition}")

                    if k == 9:
                        positionsVisitedOnce.add(tuple(currentPosition))
                        continue

            elif totalDistance == 4:
                #It means the knot above, which was already in diagonal, mooved again in diagonal. So it is at 2 steps on x and 2 steps on y. Need to moove 1 step on both axis to get back to a diagonal
                xDifference = positionToFollow[0] - currentPosition[0]
                yDifference = positionToFollow[1] - currentPosition[1]
                currentPosition[0] += int(xDifference/2)
                currentPosition[1] += int(yDifference/2)

                positions[k] = currentPosition

                #print(f"h is in {hPosition} and knot {k} is in {currentPosition}")
                if k == 9:
                    positionsVisitedOnce.add(tuple(currentPosition))

#print(positionsVisitedOnce)
print(f"answer is {len(positionsVisitedOnce)}")