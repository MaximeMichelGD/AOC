#/!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\

#This version is manual. At the time I am writing this comment, I really want to optimize that and make it automatic with any given data
#So check if there is a Day11_Partx_Automatized to check out my automatized solution if it exists!
#2023-06-20

#/!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\

import os
import string


monkey0 = [79,98]
monkey1 = [54,65,75,74]
monkey2 = [79,60,97]
monkey3 = [74]

monkey0_inspect = 0
monkey1_inspect = 0
monkey2_inspect = 0
monkey3_inspect = 0

supermodulo = 23 * 19 * 13 * 17

def Main(monkey0, monkey1, monkey2, monkey3, monkey0_inspect, monkey1_inspect, monkey2_inspect, monkey3_inspect):
    for item in reversed(monkey0):
        monkey0_inspect += 1

        new = 0
        new = (item * 19) % supermodulo
        #new = new // 3

        if new % 23 == 0:
            monkey2.append(new)
        else:
            monkey3.append(new)

        monkey0.remove(item)

    for item in reversed(monkey1):
        monkey1_inspect += 1

        new = 0
        new = (item + 6) % supermodulo
        #new = new // 3

        if new % 19 == 0:
            monkey2.append(new)
        else:
            monkey0.append(new)

        monkey1.remove(item)

    for item in reversed(monkey2):
        monkey2_inspect += 1

        new = 0
        new = (item * item) % supermodulo
        #new = new // 3

        if new % 13 == 0:
            monkey1.append(new)
        else:
            monkey3.append(new)

        monkey2.remove(item)
    
    for item in reversed(monkey3):
        monkey3_inspect += 1

        new = 0
        new = (item + 3) % supermodulo
        #new = new // 3

        if new % 17 == 0:
            monkey0.append(new)
        else:
            monkey1.append(new)

        monkey3.remove(item)


    return monkey0, monkey1, monkey2, monkey3, monkey0_inspect, monkey1_inspect, monkey2_inspect, monkey3_inspect
    

for i in range(10000):
    print(f"round {i+1}")

    monkey0, monkey1, monkey2, monkey3, monkey0_inspect, monkey1_inspect, monkey2_inspect, monkey3_inspect = Main(monkey0, monkey1, monkey2, monkey3, monkey0_inspect, monkey1_inspect, monkey2_inspect, monkey3_inspect)

    # print(f"After round {i+1}, monkeys are holding:")
    # print(f"Monkey 0: {monkey0}")
    # print(f"Monkey 1: {monkey1}")
    # print(f"Monkey 2: {monkey2}")
    # print(f"Monkey 3: {monkey3}")
    # print("-"*30)

print(f"monkey0 inspected {monkey0_inspect} items")
print(f"monkey1 inspected {monkey1_inspect} items")
print(f"monkey2 inspected {monkey2_inspect} items")
print(f"monkey3 inspected {monkey3_inspect} items")
print("-"*30)

print("\n")

inspected = []
inspected.append(monkey0_inspect)
inspected.append(monkey1_inspect)
inspected.append(monkey2_inspect)
inspected.append(monkey3_inspect)

inspected.sort(reverse=True)

answer = inspected[0] * inspected[1]

print(f"answer is {answer}")