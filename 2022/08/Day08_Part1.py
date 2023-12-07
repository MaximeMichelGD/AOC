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

def Check(value, liste):
    #print(liste)
    for m in range(len(liste)):
        toReturn = 0
        #print(f"toreturn set back to 0")
        #print(f"iterating with n = {range(len(liste[m][0]))}")
        for n in range(len(liste[m][0])):
            #print(f"[{m}][0][{n}]")
            #print(f"len liste {len(liste)}, liste {liste[m][0]} has a len of {len(liste[m][0])}")
            if int(value) > int(liste[m][0][n]):
                toReturn += 1
                #print(f"checking {value} against list {liste[m][0]} element {liste[m][0][n]} and got {toReturn}")
            # else:
            #     print(f"checking {value} against list {liste[m][0]} element {liste[m][0][n]} and got 0")
            
        if toReturn == len(liste[m][0]):
            #print(f"returned 1 because toReturn is equal {toReturn} and lenListe[m][0][n] is equal {len(liste[m][0][n])}")
            #print("\n")
            return 1
        
    #print("\n")
    
    return 0

for i in range(forestSee.shape[0]):
    for j in range(forestSee.shape[1]):
        forestSee[i][0] = 1
        forestSee[i][forestSee.shape[0]-1] = 1
        forestSee[0][j] = 1
        forestSee[forestSee.shape[1]-1][j] = 1

#print(forestSee)

for k in range(forest.shape[0]):
    for l in range(forest.shape[1]):
        liste = []
        top = [[]]
        bottom = [[]]
        if forestSee[l][k]:
            #print(f"continue because already see")
            continue
        valueToCheck = forest[l][k] 
        left = forest.iloc[k:k+1,0:l].values.tolist()
        right = forest.iloc[k:k+1, l+1:forest.shape[0]].values.tolist()
        topTemporary = forest.iloc[0:k,l:l+1].values.tolist()
        #print(f"len de toptemporary is {len(topTemporary)}")
        for x in range(len(topTemporary)):
            top[0].append(topTemporary[x][0])
        
        bottomTemporary = forest.iloc[k+1:forest.shape[1],l:l+1].values.tolist()
        for z in range(len(bottomTemporary)):
            bottom[0].append(bottomTemporary[z][0])

        liste.append(left)
        liste.append(right)
        liste.append(top)
        liste.append(bottom)
        
        # print(f"value to check {valueToCheck}")
        # print(f"left \n {left}")
        # print(f"right \n {right}")
        # print(f"top \n {top}")
        # print(f"bottom \n {bottom}")
        # print("\n")

        # print(f"checking forest[{l}][{k}] = {forest[l][k]} ")
        forestSee[l][k] = Check(valueToCheck,liste)

        # print(forestSee)

print(f"answer is {forestSee.sum().sum()}")
