import os

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

best_sum = 0
actual_sum = 0
elf_number = 1
calories = []

for i in range(lines):
    if lst[i] == "\n":
        elf_number += 1
        calories.append(actual_sum)
        if actual_sum > best_sum:
            best_sum = actual_sum
            #print(f"elf {elf_number} is carrying {actual_sum} calories")
        actual_sum = 0
    else:
        actual_sum += int(lst[i])

print(f"1 - The elf who carrys the most, carry {best_sum} calories")

calories.sort()
calories = calories[-3:]

top3 = sum(calories)


print(f"2 - Top 3 elf carry a total of {top3} calories")
