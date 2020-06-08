import random
import json
import sys


def get_dice_num(dice):
    # Generate noun number
    dice_num = ''
    for x in range(dice):
        dice_num += str(random.randint(1, 6))
    return dice_num

# Open adjectives list
with open('./nlp-adjectives.json') as f1:
    adj_list = json.load(f1)
f1.close()

# Open noun list
with open('./nlp-nouns.json') as f2:
    noun_list = json.load(f2)
f2.close()

# Initialize 2 of each noun and adjectives
num = 2
if len(sys.argv) > 1:
    num = int(sys.argv[1])
arr = []
for x in range(num):
    arr.append(adj_list[get_dice_num(4)])
    arr.append(noun_list[get_dice_num(5)])

# Concatenate the words into a password
password = " ".join(arr)

# Print the password
print(password)
