import os
import string
from collections import deque

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\dataexemple.txt", "r").read().strip()
lines = [x for x in lst.split('\n')]

grid = []

for line in lines:
    grid.append(line)

rows = len(grid)
colums = len(grid[0])

map_grid = [[0 for _ in range(colums)] for _ in range(rows)]

for i in range(rows):
    for k in range(colums):
        if grid[i][k] == "S":
            map_grid[i][k] = 1
        elif grid[i][k] == "E":
            map_grid[i][k] = 26
        else: 
            map_grid[i][k] = ord(grid[i][k]) - ord("a") + 1

print(map_grid)

def Wazeing(part):
    Q = deque()
    for r in range(rows):
        for c in range(colums):
            if (part==1 and grid[r][c]=='S') or (part==2 and map_grid[r][c] == 1):
                Q.append(((r,c), 0))

    S = set()
    while Q:
        (r,c),d = Q.popleft()
        print((r,c),d)
        if (r,c) in S:
            print("----")
            continue
        S.add((r,c))
        if grid[r][c]=='E':
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c+dc

            print(f"rr {rr}, r {r}, dr {dr} / cc {cc} c {c} dc {dc}")
            print(f"checking 0<={rr}<{rows} and 0 <={cc}<{colums} and {grid[rr][cc]}<= {grid[r][c]}")
            if 0<=rr<rows and 0<=cc<colums and map_grid[rr][cc]<=1+map_grid[r][c]:
                Q.append(((rr,cc),d+1))
                print(f"q.append ({(rr,cc),d+1})")

            print("--")        
        print("---------------------------------")


Wazeing(1)