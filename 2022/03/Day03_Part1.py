import os
import string

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

listletter = list(string.ascii_lowercase + string.ascii_uppercase)

points = 0
actualLineLen = 0
line = ""
first_list = []
second_list = []

for i in range(lines):
    line = lst[i].strip()
    actualLineLen = len(line)
    first_list = list(line[:int(actualLineLen/2)])
    second_list = list(line[int(actualLineLen/2):])
    #print(f"{line} divided in {first_list} and {second_list}")
    for j in range(len(first_list)):
        if first_list[j] in second_list:
            points += (listletter.index(first_list[j])+1)
            break

print(points)