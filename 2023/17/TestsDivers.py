for i, (d,r) in enumerate([[-1,0], [0,1], [1,0], [0,-1]]):
    print(i, (d,r))

x = 5

if 0<x<99:
    print(True)


row = 5
column = 3
direction = 1
sumOne = 5
sumTwo = 10

visited = dict()

visited[row,column,direction] = sumOne

print(visited)

if visited[row,6,direction] < sumTwo:
    print(True)

# if visited[row,column,direction] < sumTwo:
