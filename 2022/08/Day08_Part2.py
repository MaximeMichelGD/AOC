import os
import string
import pandas as pd
import numpy as np

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

forest = pd.DataFrame()
forestList = []

for i in range(lines):
    trees = list(lst[i].strip())
    forestList.append(trees)

forest = forest.append(forestList, ignore_index = True)

#print(forest)
#print(f"forest shape of {forest.shape}")
# print(forest.shape[0])
# print(forest.shape[1])

npForest = np.zeros((forest.shape[0], forest.shape[1]))
forestSee = pd.DataFrame(npForest)

def Check(value, left, right, top, bottom):
    #print(liste)

    left = list(reversed(left))
    top = list(reversed(top))

    fromLeft = CalculateView(value, left)
    fromRight = CalculateView(value, right)
    fromTop = CalculateView(value, top)
    fromBottom = CalculateView(value, bottom)

    return fromLeft * fromRight * fromTop * fromBottom

def CalculateView(value, liste):
    #print(f"checking value {value} in liste {liste}")
    if len(liste) == 0:
        return 0

    toReturn = 0
    for i in range(len(liste)):
        toReturn += 1
        if liste[i] >= value:
            break
    return toReturn

for i in range(forestSee.shape[0]):
    for j in range(forestSee.shape[1]):
        forestSee[i][0] = 1
        forestSee[i][forestSee.shape[0]-1] = 1
        forestSee[0][j] = 1
        forestSee[forestSee.shape[1]-1][j] = 1

#print(forestSee)

scenicActualScore = 0
scenicBestScore = 0

for k in range(forest.shape[0]):
    for l in range(forest.shape[1]):
        if forestSee[l][k]:
            #print(f"continue because already see")
            continue
        valueToCheck = forest[l][k] 
        left = forest.iloc[k:k+1,0:l].values.tolist()[0]
        right = forest.iloc[k:k+1, l+1:forest.shape[0]].values.tolist()[0]
        top = np.array(forest.iloc[0:k,l:l+1].squeeze()).tolist()
        bottom = np.array(forest.iloc[k+1:forest.shape[1],l:l+1].squeeze()).tolist()

        # print(f"value to check {valueToCheck}")
        # print(f"left \n {left}")
        # print(f"right \n {right}")
        # print(f"top \n {top}")
        # print(f"bottom \n {bottom}")
        # print("\n")

        # print(f"checking forest[{l}][{k}] = {forest[l][k]} ")
        scenicActualScore = Check(valueToCheck, left, right, top, bottom)

        if scenicActualScore > scenicBestScore:
            scenicBestScore = scenicActualScore
#print(forestSee)

print(f"answer is {scenicBestScore}")
