import random

def play_dice():
    result = random.randint(1, 6)
    return str(result)

print(play_dice())
