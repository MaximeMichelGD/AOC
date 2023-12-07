import os
import string
import pandas as pd

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

dataframe = 0
listletter = list(string.ascii_uppercase)

stacks = []
numberOfStacks = 0

for i in range(lines):
    line = list(lst[i])

    if list(lst[i].strip())[0] == "1":
        dataframe = i-1
        break

    numberOfStacks += 1
    stacks.append(line)

iterations = len(stacks[0])
indexToDelete = []
toDelete = False

for j in range(iterations):

    for k in range(len(stacks)):

        if stacks[k][j] == "[" or stacks[k][j] == "]":
            indexToDelete.append(j)
            break
        if stacks[k][j] == " ":
            toDelete = True
            continue
        if stacks[k][j] in listletter:
            toDelete = False
            break
    
    if toDelete:
        indexToDelete.append(j)
        continue
    toDelete = False

newIndexToDelete = []
for l in indexToDelete:
    if l not in newIndexToDelete:
        newIndexToDelete.append(l)

indexDelete = 0

for m in range(len(stacks)):
    for n in reversed(newIndexToDelete):
        del(stacks[m][n])

stacksPD = pd.DataFrame(stacks)
columns = list(range(len(stacksPD.axes[1])))

stacksFinal = []
stack = []

for i in columns:
    stackList = list(reversed(stacksPD[i].tolist()))
    try:
        while True:
            stackList.remove(" ")
    except ValueError:
        pass
    stacksFinal.append(stackList)

#print(stacksFinal)

fromStack = 0
number = 0
toStack = 0
sliceToMove = []

for i in range(numberOfStacks+2,lines):
    line = lst[i].strip()
    line = line.replace("move ","")
    line = line.replace(" from ","-")
    line = line.replace(" to ","-")
    line = line.split("-")

    number = int(line[0])
    fromStack = int(line[1])-1
    toStack = int(line[2])-1

    sliceToMove = stacksFinal[fromStack][-number:]

    #print(f"il faut bouger {sliceToMove} de {stacksFinal[fromStack]} à {stacksFinal[toStack]}")

    for j in reversed(sliceToMove):
        stacksFinal[toStack].append(j)

    del(stacksFinal[fromStack][-number:])

answer = ""
for i in stacksFinal:
    answer += i[-1]

print(answer)