import os
import string
import pandas as pd
import time


startReading = time.time()
lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

endReading = time.time()
readingTime = startReading - endReading
print(f"Time to read the file :  {readingTime}")

solutionStart = time.time()

TOTAL_AVAILABLE_SPACE = 70000000
UNUSED_SPACE_NEEDED = 30000000

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

totalSize = directorys["/"]
spaceToFree = totalSize - (TOTAL_AVAILABLE_SPACE - UNUSED_SPACE_NEEDED)

dirToDelete = ""
dirToDeleteSize = TOTAL_AVAILABLE_SPACE
sum_size = 0
for key in directorys:
    if directorys[key] <= 100000:
        sum_size += directorys[key]
    
    if directorys[key] >= spaceToFree and directorys[key] < dirToDeleteSize:
        dirToDeleteSize = directorys[key]
        dirToDelete = key

print(f"Total size of directory under 100 000 is {sum_size}")

print(f"The directory to delete to get enough free space is {dirToDelete} and has a size of {dirToDeleteSize}")

solutionEnd = time.time()
partOneTime = solutionEnd - solutionStart
print(f"Time : {partOneTime}")