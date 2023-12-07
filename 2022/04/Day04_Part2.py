import os
import string

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)
pair = []

firstNum = 0
secondNum = 0
thirdNum = 0
fourthNum = 0

number = 0

for i in range(lines):
    firstNum = lst[i].strip().split("-")[0]
    secondNum = lst[i].strip().split("-")[1].split(",")[0]
    thirdNum = lst[i].strip().split("-")[1].split(",")[1]
    fourthNum = lst[i].strip().split("-")[2]
    pair.append(firstNum)
    pair.append(secondNum)
    pair.append(thirdNum)
    pair.append(fourthNum)

    if ((int(pair[2]) >= int(pair[0])) and (int(pair[2]) <= int(pair[1]))) or ((int(pair[3]) >= int(pair[0])) and (int(pair[3]) <= int(pair[1]))) or ((int(pair[0]) >= int(pair[2])) and (int(pair[0]) <= int(pair[3]))) or ((int(pair[1]) >= int(pair[2])) and (int(pair[1]) <= int(pair[3]))):
        number += 1
        #print(f"pair {pair}. {pair[2]} >= {pair[0]} {pair[2] >= pair[0]} // {pair[3]} <= {pair[1]} {pair[3] <= pair[1]} // {pair[0]} >= {pair[2]} {pair[0] >= pair[2]} // {pair[1]} <= {pair[3]} {pair[1] <= pair[3]}")

    pair = []

print(number)
