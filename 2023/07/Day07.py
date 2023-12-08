#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Author: Maxime MICHEL
# https://github.com/MaximeMichelGD
#
# Date: 2023 12 07
# Purpose: Trying to be a better coder while participating at AOC 2023!
# Find all my solutions on my GitHub!
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

import os
import time

# Set realDataSet to True to test with real dataset
realDataSet = True
day = 7

print(f"* Day {day} *")

#---------------------------------------------------------------------------------------------------------------
# Reading Data
#---------------------------------------------------------------------------------------------------------------

startReading = time.time()
lst = ""
if realDataSet:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\data.txt", "r").read().strip()
else:
    lst = open(os.path.realpath(os.path.dirname(__file__)) + "\dataexemple.txt", "r").read().strip()

endReading = time.time()
readingTime = startReading - endReading
print(f"Time to read the file :  {readingTime}")

#---------------------------------------------------------------------------------------------------------------
# Part 1 !
#---------------------------------------------------------------------------------------------------------------
solutionStart = time.time()
lines = [x for x in lst.split('\n')]

result = 0

hands = {"five_kind": 0, "four_kind": 1, "full_house": 2, "three_kind": 3, "two_pair": 4, "one_pair": 5, "high_card": 6}
cards_rank = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

def determineTypeHand(cards):
    cardsUnique = set({})

    for card in cards:
        cardsUnique.add(card)
    
    if len(cardsUnique) == 5:
        return hands["high_card"]
    
    elif len(cardsUnique) == 4:
        return hands["one_pair"]
    
    elif len(cardsUnique) == 3:
        for card in cardsUnique:
            if cards.count(card) == 3:
                return hands["three_kind"]
            elif cards.count(card) == 2:
                return hands["two_pair"]
    
    elif len(cardsUnique) == 2:
        for card in cardsUnique:
            if cards.count(card) == 4:
                return hands["four_kind"]
            elif cards.count(card) == 3:
                return hands["full_house"]
    
    else:
        return hands["five_kind"]

hands_ranked = [[],[],[],[],[],[],[]]

for i in range(len(lines)):
    line = lines[i].strip().split()

    cards = line[0]

    # First step, determines what type the hand is
    typeHandIndex = determineTypeHand(cards)
    
    # Now we need to rank each current hand
    if hands_ranked[typeHandIndex] == []: # The hand is the first in its category, it goes first place without comparison
        hands_ranked[typeHandIndex].append(line)
    else: # The hand is not first in its category
        indexToPlace = -1
        hand_placed = False
        for hand in hands_ranked[typeHandIndex]:
            indexToPlace += 1

            # Check if current hand (line) is better than the hand in iteration

            for j in range(0,5):
                #print(f"checking {cards[i]} of {cards} > {hand[0][i]} of cards {hand[0]} ")
                if cards_rank[cards[j]] > cards_rank[hand[0][j]]: # The card is better, we place it before this hand
                    hands_ranked[typeHandIndex].insert(indexToPlace, line)
                    hand_placed = True
                    break # Hand was placed, no point to continue
                elif cards_rank[cards[j]] < cards_rank[hand[0][j]]: # The card is lower, we break to compare vs next hand
                    break
            
            # Need to break of this loop if hand was succesfully placed
            if hand_placed:
                break
        
        if hand_placed == False: # current hand wasn't better than any other hand, place it in last position
            hands_ranked[typeHandIndex].append(line)

final_hands = []

for i in range(len(hands_ranked)):
    for j in range(len(hands_ranked[i])):
        final_hands.append(hands_ranked[i][j])

for i in range(len(final_hands)):
    result += int(final_hands[i][1]) * range(1,len(final_hands)+1)[-i-1]


# Part 1 Time
print(f"Part 1 result : {result}")
solutionEnd = time.time()
partOneTime = solutionEnd - solutionStart
print(f"Part 1 Time : {partOneTime}")

#---------------------------------------------------------------------------------------------------------------
# Part 2 !
#---------------------------------------------------------------------------------------------------------------
solutionStart = time.time()

result = 0

cards_rank_two = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

def determineTypeHandPartTwo(cardsReceived):
    cardsUnique = set({})

    for card in cardsReceived:
        cardsUnique.add(card)
    
    if len(cardsUnique) == 5:
        if cardsReceived.count("J") == 0:
            return hands["high_card"]
        else:
            return hands["one_pair"]

    elif len(cardsUnique) == 4:
        if cardsReceived.count("J") == 0:
            return hands["one_pair"]
        else:
            return hands["three_kind"]

    
    elif len(cardsUnique) == 3:
        if cardsReceived.count("J") == 0:
            for card in cardsUnique:
                if cardsReceived.count(card) == 3:
                    return hands["three_kind"]
                elif cardsReceived.count(card) == 2:
                    return hands["two_pair"]
        else:
            if cardsReceived.count("J") >= 2:
                return hands["four_kind"]
            for card in cardsUnique:
                if (cardsReceived.count(card) == 1 or cardsReceived.count(card) == 3) and card != "J":
                    #print(f"Hands {cardsReceived} was ruled a four_kind because {card} of {cardsUnique} was counted {cardsReceived.count(card)}")
                    return hands["four_kind"]
                elif cardsReceived.count(card) == 2:
                    #print(f"Hands {cardsReceived} was ruled a full_house because {card} of {cardsUnique} was counted {cardsReceived.count(card)}")
                    return hands["full_house"]
    
    elif len(cardsUnique) == 2:
        if cardsReceived.count("J") == 0:
            for card in cardsUnique:
                if cardsReceived.count(card) == 4:
                    return hands["four_kind"]
                elif cardsReceived.count(card) == 3:
                    return hands["full_house"]
        else:
            #print(f"Hands {cards} was ruled a five_kind")
            return hands["five_kind"]
    
    else:
        return hands["five_kind"]

hands_ranked = [[],[],[],[],[],[],[]]

for i in range(len(lines)):
    line = lines[i].strip().split()

    cards = line[0]

    # First step, determines what type the hand is
    typeHandIndex = determineTypeHandPartTwo(cards)

    line.append(typeHandIndex)
    
    # Now we need to rank each current hand
    if hands_ranked[typeHandIndex] == []: # The hand is the first in its category, it goes first place without comparison
        hands_ranked[typeHandIndex].append(line)
    else: # The hand is not first in its category
        indexToPlace = -1
        hand_placed = False
        for hand in hands_ranked[typeHandIndex]:
            indexToPlace += 1

            # Check if current hand (line) is better than the hand in iteration

            for j in range(5):
                #print(f"checking {cards[i]} of {cards} > {hand[0][i]} of cards {hand[0]} ")
                if cards_rank_two[cards[j]] > cards_rank_two[hand[0][j]]: # The card is better, we place it before this hand
                    hands_ranked[typeHandIndex].insert(indexToPlace, line)
                    hand_placed = True
                    break # Hand was placed, no point to continue
                elif cards_rank_two[cards[j]] < cards_rank_two[hand[0][j]]: # The card is lower
                    break
            
            # Need to break of this loop if hand was succesfully placed
            if hand_placed:
                break
        
        if hand_placed == False: # current hand wasn't better than any other hand, place it in last position
            hands_ranked[typeHandIndex].append(line)

final_hands = []

for l in range(len(hands_ranked)):
    for m in range(len(hands_ranked[l])):
        final_hands.append(hands_ranked[l][m])
        #print(hands_ranked[l][m])
        #print(f"placing {hands_ranked[l][m]}, result {final_hands[-1]} => {hands_ranked[l][m] == final_hands[-1]}")

for i in range(len(final_hands)):
    result += int(final_hands[i][1]) * range(1,len(final_hands)+1)[-i-1]

# Part 2 Time
print(f"Part 2 result : {result}")
solutionEnd = time.time()
partTwoTime = solutionEnd - solutionStart
print(f"Part 2 Time : {partTwoTime}")

#---------------------------------------------------------------------------------------------------------------
# Time !
#---------------------------------------------------------------------------------------------------------------

totalTime = partOneTime + partTwoTime
print(f"Total Time: {totalTime}")