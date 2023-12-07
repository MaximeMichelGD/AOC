import pandas as pd

x = []
y = []

for i in reversed(range(0,25)):
    x = []
    for j in range(0,50):
        if i == 0:
            x.append(j-25)
        else:
            x.append(".")
    x[0] = i-12
    y.append(x)

hPosition = [-10,-5]
tPosition = [-11,-5]

hCoordinates = [0,0]
tCoordinates = [0,0]

for i in range(len(y)-1):
    if y[i][0] == hPosition[1]:
        hCoordinates[1] = i
    if y[i][0] == tPosition[1]:
        tCoordinates[1] = i

for j in range(len(y[-1])):
    if y[-1][j] == hPosition[0]:
        hCoordinates[0] = j
    if y[-1][j] == tPosition[0]:
        tCoordinates[0] = j

y[hCoordinates[1]][hCoordinates[0]] = "H"
y[tCoordinates[1]][tCoordinates[0]] = "T"

visu = pd.DataFrame(y)

visu = visu.to_string(index=False)

print(visu)
