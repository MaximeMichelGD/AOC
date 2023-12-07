import os
import string

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

listletter = list(string.ascii_lowercase + string.ascii_uppercase)

points = 0
line = ""

iteration = 0

firstLine = []
secondLine = []
thirdLine = []

for i in range(lines):
    iteration += 1
    if iteration == 3:
        firstLine = list(lst[i-2].strip())
        secondLine = list(lst[i-1].strip())
        thirdLine = list(lst[i].strip())
        iteration = 0
        for j in range(len(firstLine)):
            if (firstLine[j] in secondLine) and (firstLine[j] in thirdLine):
                points += (listletter.index(firstLine[j])+1)
                break

print(points)