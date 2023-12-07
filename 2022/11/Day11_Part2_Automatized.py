#/!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\

#That's it, you are in the optimized version. Any given data, for any number of monkeys should work
#Only limits are:
#   - the test should always be a division
#   - the operation should stay + or * => cannot perform division
#2023-06-20
# PS: automatized version was done in the very same day

#/!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\

import os
import string

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").readlines()
lines = len(lst)

items = []
operations = []
tests = []
throw = []
monkeyInspect = []

for i in range(lines):
    instruction = list(lst[i].split())

    if instruction == []:
        continue

    elif instruction[0] == "Starting":
        monkeyInspect.append(0)
        monkeyItems = []
        for j in range(2,len(instruction)):
            monkeyItems.append(int(instruction[j].replace(",","")))
        items.append(monkeyItems)
    
    elif instruction[0] == "Operation:":
        monkeyOperation = []
        monkeyOperation.append(instruction[3])
        monkeyOperation.append(instruction[4])
        monkeyOperation.append(instruction[5])
        operations.append(monkeyOperation)
    
    elif instruction[0] == "Test:":
        tests.append(int(instruction[3]))
    
    elif instruction[0] == "If" and instruction[1] == "true:":
        monkeyThrow = []
        monkeyThrow.append(instruction[5])
    
    elif instruction[0] == "If" and instruction[1] == "false:":
        monkeyThrow.append(int(instruction[5]))
        throw.append(monkeyThrow)


# The supermodulo ensure that a number will never go higher than the supermodulo. Allowing this algorith to go for 10 000 rounds and more
# Without this, numbers can go really quick to 100 000(+) digits and the loop could never end, unless maybe you have access to some NASA supercalculator?
# We apply this to every item a monkey inspect
# Let's say we have Monkey 1 inspecting item 55 with rule of divisible by 5, and Monkey 2 inspecting item 72 with rule of divisible by 7
# Supermodulo would be 5 * 7 = 35
# 1st monkey is testing 55 % 5 = 0 (11 * 5 + 0)
# 2nd monkey is testing 72 % 7 = 2 (10 * 7 + 2)
# Now applying supermodulo to item before each specific rule of each monkey
# 1st monkey: 55 % 35 = 20 (1 * 35 + 20)  ==> 20 % 5 = 0 (4 * 5 + 0)
# 2nd monkey: 72 % 35 = 2 (2 * 35 + 2)  ==> 2 % 7 = 2 (0 * 7 + 2)
# Same results!

supermodulo = 1

for i in range(len(tests)):
    supermodulo *= tests[i]

def Rounds(items, operations, tests, throw, monkeyInspect):
    for monkey in range(len(monkeyInspect)):
        for i in reversed(items[monkey]):
            monkeyInspect[monkey] += 1
            item = i
            new = 0

            if operations[monkey][1] == "+":
                if operations[monkey][2] == "old":
                    new = (item + item) % supermodulo
                else:
                    new = (item + int(operations[monkey][2])) % supermodulo
            elif operations[monkey][1] == "*":
                if operations[monkey][2] == "old":
                    new = (item * item) % supermodulo
                else:
                    new = (item * int(operations[monkey][2])) % supermodulo

            if new % int(tests[monkey]) == 0:
                items[int(throw[monkey][0])].append(new)
            else:
                items[int(throw[monkey][1])].append(new)

            items[monkey].remove(item)

    return items, operations, tests, throw, monkeyInspect

for i in range(10000):
    items, operations, tests, throw, monkeyInspect = Rounds(items, operations, tests, throw, monkeyInspect)

monkeyInspect.sort(reverse=True)
answer = monkeyInspect[0] * monkeyInspect[1]

print(f"answer is {answer}")