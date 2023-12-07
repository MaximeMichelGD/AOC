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

numbers = {"red": 12, "green": 13, "blue": 14}

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

id_multiplication = 0

for i in range(len(lines)): #On itère sur les lignes de data
    line = lines[i].strip()
    line = line.replace("; ","-")
    line = line.replace(",","")

    gameSeparatorIndex = line.find(":")

    gameID = int(line[5:gameSeparatorIndex])
    lenLine = len(line)

    lineBis = line[gameSeparatorIndex+2:lenLine]
    lineBis = lineBis.split("-")

    set_possible = True
    game_possible = True

    #print("-"*50)
    #print(f"Game {gameID}")
    
    green_current_value = 0
    blue_current_value = 0
    red_current_value = 0

    for lists in lineBis: #Itération sur les listes d'instructions comprises dans une ligne de data
        lists = lists.split(" ")

        #print(lists)

        for i in range(len(lists)): #Itération sur les instructions comprises dans la liste d'instruction de la boucle en cours
            if lists[i].isnumeric():
                current_value = int(lists[i])
            elif lists[i] == "green":
                if current_value > green_current_value:
                    green_current_value = current_value
            elif lists[i] == "blue":
                if current_value > blue_current_value:
                    blue_current_value = current_value
            elif lists[i] == "red":
                if current_value > red_current_value:
                    red_current_value = current_value

    #print(f"red {red_current_value} - green {green_current_value} - blue {blue_current_value}")
    id_multiplication += (green_current_value * red_current_value * blue_current_value)
    
print(id_multiplication)
