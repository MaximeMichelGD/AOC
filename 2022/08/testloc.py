import os
import string
import pandas as pd
import numpy as np

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\dataexemple.txt", "r").readlines()
lines = len(lst)

forest = pd.DataFrame()
forestList = []

for i in range(lines):
    trees = list(lst[i].strip())
    forestList.append(trees)

forest = forest.append(forestList, ignore_index = True)

print(forest)

for k in range(forest.shape[0]):
    for l in range(forest.shape[1]):
        liste = []

        right = forest.iloc[k:k+1, l+1:forest.shape[0]].values.tolist()[0]
        top = np.array(forest.iloc[0:k,l:l+1].squeeze())

        print(right)
        print(type(right))
        print("\n")

        print(top)
        print(type(top))
        print("----------------------------------------------")
        print("----------------------------------------------")
