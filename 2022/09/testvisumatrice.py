import pandas as pd

lines = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

hPosition = [-20,-20]
tPosition = [20,20]

if hPosition[0] > tPosition[0]:
    minX = tPosition[0]
else:
    minX = hPosition[0]

if hPosition[1] > tPosition[1]:
    minY = tPosition[1]
else:
    minY = hPosition[1]

print(minX, minY)

lines[0][0] = minY + 2
lines[1][0] = minY + 1
lines[2][0] = minY
lines[3][0] = minY -1
lines[4][0] = minY -2
lines[5][0] = minY -3

lines[5][0] = ""
lines[5][1] = minX -2
lines[5][2] = minX -1
lines[5][3] = minX
lines[5][4] = minX +1
lines[5][5] = minX +2

hCoordinates = [0,0]
tCoordinates = [0,0]

for i in range(len(lines)-1):
    if lines[i][0] == hPosition[1]:
        hCoordinates[1] = i
    if lines[i][0] == tPosition[1]:
        tCoordinates[1] = i

for j in range(0,6):
    if lines[5][j] == hPosition[0]:
        hCoordinates[0] = j
    if lines[5][j] == tPosition[0]:
        tCoordinates[0] = j

lines[hCoordinates[1]][hCoordinates[0]] = "H"
lines[tCoordinates[1]][tCoordinates[0]] = "T"


#print(f"h of position {hPosition} will go in hCoordinates {hCoordinates}, t of position {tPosition} will go intCoordinates {tCoordinates}")

visu = pd.DataFrame(lines)

visu = visu.to_string(index=False)

print(visu)

