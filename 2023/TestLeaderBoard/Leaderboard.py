import os
import string
import json
from collections import deque

lst = open(os.path.realpath(os.path.dirname(__file__)) + "\JSON.txt", "r").read().strip()

lines = [x for x in lst.split('\n')]

json_dicti = json.loads(lst)

print(json_dicti["members"])

for user_id, user_data in json_dicti["members"].items():
    print(f"User ID: {user_id}")
    
    # Itération à travers les données de chaque utilisateur
    for key, value in user_data.items():
        if key == 'completion_day_level':
            print(f"  {key}:")
            
            # Itération à travers le niveau 'completion_day_level'
            for day, day_data in value.items():
                print(f"    Day {day}:")
                
                # Itération à travers les données spécifiques à chaque jour
                for part, part_data in day_data.items():
                    print(f"      Part {part}: {part_data}")
        else:
            print(f"  {key}: {value}")
    
    print("\n")
