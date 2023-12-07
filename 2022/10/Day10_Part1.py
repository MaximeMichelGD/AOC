import os
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

cycle = 0
x = 1

values = []

for i in range(lines):
    instruction = list(lst[i].split())
    #print(instruction)

    if instruction[0] == "noop":
        cycle += 1
        print(f"cycle {cycle} and x of {x}")

        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            values.append(x)
        continue
    
    elif instruction[0] == "addx":
        cycle += 1

        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            values.append(x)
        
        cycle += 1

        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            values.append(x)
        
        x += int(instruction[1])

        print(f"cycle {cycle} and x of {x}")



print(values)
strength = values[0] * 20 + values[1] * 60 + values[2] * 100 + values[3] * 140 + values[4] * 180 + values[5] * 220

print(f"answer is {strength}")