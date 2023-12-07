import os
import string
import pandas as pd

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

lst = list(lst[0].strip())

NUMBER_TO_CHECK = 4

for i in range(len(lst)):
    txt = ""
    toAnalyse = lst[i:i+NUMBER_TO_CHECK]

    uniques = []
    for letter in toAnalyse:
        if letter in uniques:
            continue
        else:
            uniques.append(letter)

    if len(uniques) == NUMBER_TO_CHECK:
        print(f"Answer is {i+NUMBER_TO_CHECK}")
        break
