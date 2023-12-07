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

npForest = np.zeros((forest.shape[0], forest.shape[1]))
forestSee = pd.DataFrame(npForest)

def Check(value, liste):
    for m in range(len(liste)):
        for n in range(len(liste[m])):
            if int(value) <= int(liste[m][n]):
                break
            elif n == len(liste[m])-1:
                return 1
    return 0

for i in range(forestSee.shape[0]):
    for j in range(forestSee.shape[1]):
        forestSee[i][0] = 1
        forestSee[i][forestSee.shape[0]-1] = 1
        forestSee[0][j] = 1
        forestSee[forestSee.shape[1]-1][j] = 1

for k in range(forest.shape[0]):
    for l in range(forest.shape[1]):
        liste = []
        top = []
        bottom = []
        if forestSee[l][k]:
            continue
        valueToCheck = forest[l][k] 
        left = forest.iloc[k:k+1,0:l].values.tolist()[0]
        right = forest.iloc[k:k+1, l+1:forest.shape[0]].values.tolist()[0]
        top = np.array(forest.iloc[0:k,l:l+1].squeeze()).tolist()
        bottom = np.array(forest.iloc[k+1:forest.shape[1],l:l+1].squeeze()).tolist()

        liste.append(left)
        liste.append(right)
        liste.append(top)
        liste.append(bottom)
        
        forestSee[l][k] = Check(valueToCheck,liste)

print(f"answer is {forestSee.sum().sum()}")
