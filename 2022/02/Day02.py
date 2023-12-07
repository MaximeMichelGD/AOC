import os

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

points = 0
current_point = 0

# #1st part
# #A/X rock - 1 Point
# #B/Y Paper - 2 Points
# #C/Z Scissors - 3 Points
# #V = 6 points, D = 3 points, L = 0 points

# situations = {"A X": 4, "A Y": 8, "A Z": 3,"B X": 1, "B Y": 5, "B Z": 9,"C X": 7, "C Y": 2, "C Z": 6}

# for i in range(lines):
#     #print(f"Output {lst[i].strip()} result in a score of {situations[lst[i].strip()]}")
#     points += situations[lst[i].strip()]

# print(points)

#2nd part
#A rock - 1 Point
#B Paper - 2 Points
#C Scissors - 3 Points
#X = lose
#Y = draw
#Z = win
#V = 6 points, D = 3 points, L = 0 points

situations = {"A X": 3, "A Y": 4, "A Z": 8,"B X": 1, "B Y": 5, "B Z": 9,"C X": 2, "C Y": 6, "C Z": 7}

for i in range(lines):
    #print(f"Output {lst[i].strip()} result in a score of {situations[lst[i].strip()]}")
    points += situations[lst[i].strip()]

print(points)