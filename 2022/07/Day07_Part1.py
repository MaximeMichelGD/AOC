import os
import string
import pandas as pd

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

directorys = {}

current_dir = []
current_directory_sum = 0
for i in range(len(lst)):
    line = lst[i].split()

    if line[0] == "$":
        if line[1] == "cd" and line[2] != "..":
            current_dir.append(line[2])
            if line[2] not in directorys:
                directorys.update({"/".join(current_dir) : 0})
        elif line[1] == "cd" and line[2] == "..":
            del(current_dir[-1])

    if line[0].isnumeric():
        for j in range(len(current_dir)):
            directorys["/".join(current_dir[0:j+1])] += int(line[0])

sum_size = 0
for key in directorys:
    if directorys[key] <= 100000:
        sum_size += directorys[key]

print(f"final answer is {sum_size}")