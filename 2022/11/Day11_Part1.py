#/!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\

#This version is manual. At the time I am writing this comment, I really want to optimize that and make it automatic with any given data
#So check if there is a Day11_Part1_Optimized to check out my automatized solution if it exists!
#2023-06-20

#/!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\

import os
import string


monkey0 = [74,73,57,77,74]
monkey1 = [99,77,79]
monkey2 = [64,67,50,96,89,82,82]
monkey3 = [88]
monkey4 = [80,66,98,83,70,63,57,66]
monkey5 = [81,93,90,61,62,64]
monkey6 = [69,97,88,93]
monkey7 = [59,80]

monkey0_inspect = 0
monkey1_inspect = 0
monkey2_inspect = 0
monkey3_inspect = 0
monkey4_inspect = 0
monkey5_inspect = 0
monkey6_inspect = 0
monkey7_inspect = 0

def Main(monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7, monkey0_inspect, monkey1_inspect, monkey2_inspect, monkey3_inspect, monkey4_inspect, monkey5_inspect, monkey6_inspect, monkey7_inspect):
    for item in reversed(monkey0):
        monkey0_inspect += 1

        new = 0
        new = item * 11
        new = new // 3

        if new % 19 == 0:
            monkey6.append(new)
        else:
            monkey7.append(new)

        monkey0.remove(item)

    for item in reversed(monkey1):
        monkey1_inspect += 1

        new = 0
        new = item + 8
        new = new // 3

        if new % 2 == 0:
            monkey6.append(new)
        else:
            monkey0.append(new)

        monkey1.remove(item)

    for item in reversed(monkey2):
        monkey2_inspect += 1

        new = 0
        new = item + 1
        new = new // 3

        if new % 3 == 0:
            monkey5.append(new)
        else:
            monkey3.append(new)

        monkey2.remove(item)
    
    for item in reversed(monkey3):
        monkey3_inspect += 1

        new = 0
        new = item * 7
        new = new // 3

        if new % 17 == 0:
            monkey5.append(new)
        else:
            monkey4.append(new)

        monkey3.remove(item)

    for item in reversed(monkey4):
        monkey4_inspect += 1

        new = 0
        new = item + 4
        new = new // 3

        if new % 13 == 0:
            monkey0.append(new)
        else:
            monkey1.append(new)

        monkey4.remove(item)

    for item in reversed(monkey5):
        monkey5_inspect += 1

        new = 0
        new = item + 7
        new = new // 3

        if new % 7 == 0:
            monkey1.append(new)
        else:
            monkey4.append(new)

        monkey5.remove(item)
    
    for item in reversed(monkey6):
        monkey6_inspect += 1

        new = 0
        new = item * item
        new = new // 3

        if new % 5 == 0:
            monkey7.append(new)
        else:
            monkey2.append(new)

        monkey6.remove(item)

    for item in reversed(monkey7):
        monkey7_inspect += 1

        new = 0
        new = item + 6
        new = new // 3

        if new % 11 == 0:
            monkey2.append(new)
        else:
            monkey3.append(new)

        monkey7.remove(item)
    
    return monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7, monkey0_inspect, monkey1_inspect, monkey2_inspect, monkey3_inspect, monkey4_inspect, monkey5_inspect, monkey6_inspect, monkey7_inspect
    

for i in range(20):
    monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7, monkey0_inspect, monkey1_inspect, monkey2_inspect, monkey3_inspect, monkey4_inspect, monkey5_inspect, monkey6_inspect, monkey7_inspect = Main(monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7, monkey0_inspect, monkey1_inspect, monkey2_inspect, monkey3_inspect, monkey4_inspect, monkey5_inspect, monkey6_inspect, monkey7_inspect)

    print(f"After round {i+1}, monkeys are holding:")
    print(f"Monkey 0: {monkey0}")
    print(f"Monkey 1: {monkey1}")
    print(f"Monkey 2: {monkey2}")
    print(f"Monkey 3: {monkey3}")
    print(f"Monkey 4: {monkey4}")
    print(f"Monkey 5: {monkey5}")
    print(f"Monkey 6: {monkey6}")
    print(f"Monkey 7: {monkey7}")
    print("-"*30)

print(f"monkey0 inspected {monkey0_inspect} items")
print(f"monkey1 inspected {monkey1_inspect} items")
print(f"monkey2 inspected {monkey2_inspect} items")
print(f"monkey3 inspected {monkey3_inspect} items")
print(f"monkey4 inspected {monkey4_inspect} items")
print(f"monkey5 inspected {monkey5_inspect} items")
print(f"monkey6 inspected {monkey6_inspect} items")
print(f"monkey7 inspected {monkey7_inspect} items")
print("-"*30)

print("\n")

inspected = []
inspected.append(monkey0_inspect)
inspected.append(monkey1_inspect)
inspected.append(monkey2_inspect)
inspected.append(monkey3_inspect)
inspected.append(monkey4_inspect)
inspected.append(monkey5_inspect)
inspected.append(monkey6_inspect)
inspected.append(monkey7_inspect)

inspected.sort(reverse=True)

answer = inspected[0] * inspected[1]

print(f"answer is {answer}")