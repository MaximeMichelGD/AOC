import os

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

best_sum = 0
actual_sum = 0
elf_number = 1

for i in range(lines):
    if lst[i] == "\n":
        elf_number += 1
        if actual_sum > best_sum:
            best_sum = actual_sum
            print(f"elf {elf_number} is carrying {actual_sum} calories")
        actual_sum = 0
    else:
        actual_sum += int(lst[i])

print(best_sum)
