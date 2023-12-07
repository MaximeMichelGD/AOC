import os
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

cycle = 0
draw = []
line_draw = []

NUMBER_OF_COLUMNS = 40
NUMBER_OF_LINES = 6

x = 1

for i in range (NUMBER_OF_LINES):
    line_draw = []
    for i in range(NUMBER_OF_COLUMNS):
        line_draw.append("")
    draw.append(line_draw)

def Draw(cycle, x):
    #print(f"calling Draw({cycle}, {x})")
    index = 0

    if cycle-1 <= 39:
        index = 0
    elif cycle-1 <= 79:
        cycle -= 40
        index = 1
    elif cycle-1 <= 119:
        cycle -= 80
        index = 2
    elif cycle-1 <= 159:
        cycle -= 120
        index = 3
    elif cycle-1 <= 199:
        cycle -= 160
        index = 4
    elif cycle-1 <= 239:
        cycle -= 200
        index = 5

    if cycle-1 == x-1 or cycle-1 == x or cycle-1 == x+1:
        #print(f"will draw a # in draw[{index}][{cycle-1}]")
        draw[index][cycle-1] = "#"
    else:
        #print(f"will draw a . in draw[{index}][{cycle-1}]")
        draw[index][cycle-1] = " "

for j in range(lines):
    instruction = list(lst[j].split())
    #print(instruction)

    if instruction[0] == "noop":
        cycle += 1
        #print(f"cycle {cycle} and x of {x}")

        Draw(cycle, x)
    
    elif instruction[0] == "addx":
        cycle += 1
        Draw(cycle, x)

        cycle += 1
        Draw(cycle, x)

        x += int(instruction[1])
        #print(f"cycle {cycle} and x of {x}")

line = ""
for elt in draw:
    line = ""
    for pixel in elt:
        line += pixel
        line += " "
    print(line)