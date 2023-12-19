#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 19
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time
from collections import deque

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 19

print(f"* Day {day} *")

#---------------------------------------------------------------------------------------------------------------
# Reading Data
#---------------------------------------------------------------------------------------------------------------

startReading = time.time()
lst = ""
if realDataSet:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").read().rstrip().split("\n\n")
else:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\dataexemple.txt", "r").read().rstrip().split("\n\n")

endReading = time.time()
readingTime = startReading - endReading
print(f"Time to read the file :  {readingTime}")


#---------------------------------------------------------------------------------------------------------------
# Part 1 !
#---------------------------------------------------------------------------------------------------------------
solutionStart = time.time()
lines = lst
# print(lines)

result = 0

partsAnalyze = []
workflow = dict()

workflows = lines[0].split('\n')
parts = lines[1].split('\n')
for i in parts:
    part = []

    splited = i[1:-1].split(',')
    x = int(splited[0].split('=')[1])
    m = int(splited[1].split('=')[1])
    a = int(splited[2].split('=')[1])
    s = int(splited[3].split('=')[1])
    partsAnalyze.append([x,m,a,s])

# print(partsAnalyze)

for line in workflows:
    line = line.split("{")
    workflow_name = line[0]
    workflow_line = line[1][:-1].split(",")
    # print(f"workflowname {workflow_name} and {workflow_line}")
    workflow[workflow_name] = workflow_line

for part in partsAnalyze:
    not_finalized = True

    # First -> workflow name = in
    instruction_name = "in"

    # print(f"Analyzing part {part} vs {workflow[instruction_name]}")
    
    while instruction_name != "A" and instruction_name != "R":
        for i in range(len(workflow[instruction_name])):
            if not ":" in workflow[instruction_name][i]:
                instruction_name = workflow[instruction_name][i]
                break
            else:
                splited = workflow[instruction_name][i].split(':')
                if '<' in workflow[instruction_name][i]:
                    if workflow[instruction_name][i][0] == 'x' and int(part[0]) < int(splited[0][2:]):
                        instruction_name = splited[1]
                        break
                    if workflow[instruction_name][i][0]=='m' and int(part[1]) < int(splited[0][2:]):
                        instruction_name = splited[1]
                        break
                    if workflow[instruction_name][i][0]=='a' and int(part[2]) < int(splited[0][2:]):
                        instruction_name = splited[1]
                        break
                    if workflow[instruction_name][i][0]=='s' and int(part[3]) < int(splited[0][2:]):
                        instruction_name = splited[1]
                        break
                elif '>' in workflow[instruction_name][i]:
                    if workflow[instruction_name][i][0]=='x' and int(part[0]) > int(splited[0][2:]):
                        instruction_name = splited[1]
                        break
                    if workflow[instruction_name][i][0]=='m' and int(part[1]) > int(splited[0][2:]):
                        instruction_name = splited[1]
                        break
                    if workflow[instruction_name][i][0]=='a' and int(part[2]) > int(splited[0][2:]):
                        instruction_name = splited[1]
                        break
                    if workflow[instruction_name][i][0]=='s'and int(part[3]) > int(splited[0][2:]):
                        instruction_name = splited[1]
                        break
    
    if instruction_name == "A":
        result += sum(part)

# Part 1 Time
print(f"Part 1 result : {result}")
solutionEnd = time.time()
partOneTime = solutionEnd - solutionStart
print(f"Part 1 Time : {partOneTime}")


#---------------------------------------------------------------------------------------------------------------
# Part 2 !
#---------------------------------------------------------------------------------------------------------------
solutionStart = time.time()

result = 0

partsAnalyze = []
workflow = dict()

workflows = lines[0].split('\n')

Q = deque([([1,4000],[1,4000],[1,4000],[1,4000],"in")])

for line in workflows:
    line = line.split("{")
    workflow_name = line[0]
    workflow_line = line[1][:-1].split(",")
    #print(f"workflowname {workflow_name} and {workflow_line}")
    workflow[workflow_name] = workflow_line

fichier = open(os.path.realpath(os.path.dirname(__file__)) + "\dataretour.txt", "w")

while Q:
    x,m,a,s,workflow_name = Q.popleft()
    #print(x, m, a, s, workflow_name)

    fichier.write(f"{x, m, a, s, workflow_name} \n")

    if workflow_name == "A":
        result += (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
        continue
    elif workflow_name == "R":
        continue

    instructions = workflow[workflow_name]

    new = [0,0]
    newBis = [0,0]

    for i in range(len(instructions)):
        #print(f"instructions {instructions[i]}")

        if not ":" in instructions[i]:
                workflow_name = instructions[i]
                Q.append([x, m, a, s, workflow_name])
                break
        else:
            splited = instructions[i].split(':')
            workflow_value = int(splited[0][2:])
            if '<' in instructions[i]:
                if instructions[i][0] == 'x':
                    if x[0] < workflow_value < x[1]: # il faut couper la tranche en 2
                        new = [0,0]
                        new[0] = x[0]
                        new[1] = workflow_value - 1
                        Q.append([new, m, a, s, splited[1]])
                        newBis = [0,0]
                        newBis[0] = workflow_value
                        newBis[1] = x[1]
                        Q.append([newBis, m, a, s, workflow_name])
                        break
                    elif x[0] > workflow_value: # La tranche est au dessus de workflow value et on cherche de <, on passe au next step
                        continue
                    elif x[1] < workflow_value: # la tranche est en dessous de workflow value et on cherche de <, on append donc la condition
                        print("append")
                        Q.append([x, m, a, s, splited[1]])
                        break
                elif instructions[i][0]=='m':
                    if m[0] < workflow_value < m[1]: # il faut couper la tranche en 2
                        new = [0,0]
                        new[0] = m[0]
                        new[1] = workflow_value - 1
                        Q.append([x, new, a, s, splited[1]])
                        newBis = [0,0]
                        newBis[0] = workflow_value
                        newBis[1] = m[1]
                        Q.append([x, newBis, a, s, workflow_name])
                        break
                    elif m[0] > workflow_value: # La tranche est au dessus de workflow value et on cherche de <, on passe au next step
                        continue
                    elif m[1] < workflow_value: # la tranche est en dessous de workflow value et on cherche de <, on append donc la condition
                        print("append")
                        Q.append([x, m, a, s, splited[1]])
                        break
                elif instructions[i][0]=='a':
                    if a[0] < workflow_value < a[1]: # il faut couper la tranche en 2
                        new = [0,0]
                        new[0] = a[0]
                        new[1] = workflow_value - 1
                        Q.append([x, m, new, s, splited[1]])
                        newBis = [0,0]
                        newBis[0] = workflow_value
                        newBis[1] = a[1]
                        Q.append([x, m, newBis, s, workflow_name])
                        break
                    elif a[0] > workflow_value: # La tranche est au dessus de workflow value et on cherche de <, on passe au next step
                        continue
                    elif a[1] < workflow_value: # la tranche est en dessous de workflow value et on cherche de <, on append donc la condition
                        Q.append([x, m, a, s, splited[1]])
                        break
                elif instructions[i][0]=='s':
                    if s[0] < workflow_value < s[1]: # il faut couper la tranche en 2
                        new = [0,0]
                        new[0] = s[0]
                        new[1] = workflow_value - 1
                        Q.append([x, m, a, new, splited[1]])
                        newBis = [0,0]
                        newBis[0] = workflow_value
                        newBis[1] = s[1]
                        Q.append([x, m, a, newBis, workflow_name])
                        break
                    elif s[0] > workflow_value: # La tranche est au dessus de workflow value et on cherche de <, on passe au next step
                        continue
                    elif s[1] < workflow_value: # la tranche est en dessous de workflow value et on cherche de <, on append donc la condition
                        print("append")
                        Q.append([x, m, a, s, splited[1]])
                        break
            elif '>' in instructions[i]:
                if instructions[i][0] == 'x':
                    if x[0] < workflow_value < x[1]: # il faut couper la tranche en 2
                        new = [0,0]
                        new[0] = workflow_value + 1
                        new[1] = x[1]
                        Q.append([new, m, a, s, splited[1]])
                        newBis = [0,0]
                        newBis[0] = x[0]
                        newBis[1] = workflow_value
                        Q.append([newBis, m, a, s, workflow_name])
                        break
                    elif x[1] < workflow_value: # La tranche est en dessous de workflow value et on cherche de >, on passe au next step
                        continue
                    elif x[0] > workflow_value: # la tranche est en dessus de workflow value et on cherche de >, on append donc la condition
                        Q.append([x, m, a, s, splited[1]])
                        break
                elif instructions[i][0]=='m':
                    if m[0] < workflow_value < m[1]: # il faut couper la tranche en 2
                        new = [0,0]
                        new[0] = workflow_value + 1
                        new[1] = m[1]
                        Q.append([x, new, a, s, splited[1]])
                        newBis = [0,0]
                        newBis[0] = m[0]
                        newBis[1] = workflow_value
                        Q.append([x, newBis, a, s, workflow_name])
                        break
                    elif m[1] < workflow_value: # La tranche est en dessous de workflow value et on cherche de >, on passe au next step
                        continue
                    elif m[0] > workflow_value: # la tranche est en dessus de workflow value et on cherche de >, on append donc la condition
                        Q.append([x, m, a, s, splited[1]])
                        break
                elif instructions[i][0]=='a':
                    if a[0] < workflow_value < a[1]: # il faut couper la tranche en 2
                        new = [0,0]
                        new[0] = workflow_value + 1
                        new[1] = a[1]
                        Q.append([x, m, new, s, splited[1]])
                        newBis = [0,0]
                        newBis[0] = a[0]
                        newBis[1] = workflow_value
                        Q.append([x, m, newBis, s, workflow_name])
                        break
                    elif a[1] < workflow_value: # La tranche est en dessous de workflow value et on cherche de >, on passe au next step
                        continue
                    elif a[0] > workflow_value: # la tranche est en dessus de workflow value et on cherche de >, on append donc la condition
                        Q.append([x, m, a, s, splited[1]])
                        break
                elif instructions[i][0]=='s':
                    if s[0] < workflow_value < s[1]: # il faut couper la tranche en 2
                        new = [0,0]
                        new[0] = workflow_value + 1
                        new[1] = s[1]
                        Q.append([x, m, a, new, splited[1]])
                        newBis = [0,0]
                        newBis[0] = s[0]
                        newBis[1] = workflow_value
                        Q.append([x, m, a, newBis, workflow_name])
                        break
                    elif s[1] < workflow_value: # La tranche est en dessous de workflow value et on cherche de >, on passe au next step
                        continue
                    elif s[0] > workflow_value: # la tranche est en dessus de workflow value et on cherche de >, on append donc la condition
                        Q.append([x, m, a, s, splited[1]])
                        break

# Part 2 Time
print(f"Part 2 result : {result}")
solutionEnd = time.time()
partTwoTime = solutionEnd - solutionStart
print(f"Part 2 Time : {partTwoTime}")

#---------------------------------------------------------------------------------------------------------------
# Time !
#---------------------------------------------------------------------------------------------------------------

totalTime = partOneTime + partTwoTime
print(f"Total Time: {totalTime}")