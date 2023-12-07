import os
import string
from collections import deque

# Set realDataSet to True to test with real dataset
realDataSet = True

lst = ""
if realDataSet:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").read().strip()
else:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\dataexemple.txt", "r").read().strip()
lines = [x for x in lst.split('\n')]

positions_numbers = []

for i in range(len(lines)): #On itère sur les lignes de data
    positions_to_check = []
    current_number = ""
    set_positions = set({})
    for char in range(len(lines[i])):
        if lines[i][char].isnumeric(): #Si nombre est numeric
            current_number = current_number + str(lines[i][char])
            position_to_check = str(i) + " " + str(char)
            positions_to_check.append(position_to_check)

            if char == len(lines[i])-1:
                positions_to_check.insert(0, current_number)
                positions_numbers.append(positions_to_check)
                current_number = ""
                positions_to_check = []

        elif current_number != "":
            positions_to_check.insert(0, current_number)
            positions_numbers.append(positions_to_check)
            current_number = ""
            positions_to_check = []

result = 0
numbers_added = []

for item in positions_numbers:
    current_number = item[0]
    valid_number = False

    for j in range(1, len(item)):
        if valid_number == True:
            break
        
        x = int(item[j].split()[0])
        y = int(item[j].split()[1])

        for k in range(-1,2):
            if valid_number == True:
                break
            for l in range(-1,2):
                try:
                    if not lines[x+k][y+l].isnumeric() and lines[x+k][y+l] != ".":
                        valid_number = True
                        result += int(current_number)
                        numbers_added.append(current_number)
                        break
                except:
                    continue

print(result)