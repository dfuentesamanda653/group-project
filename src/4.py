
import random

def get_random_code():
    """Returns a randomly generated string of characters."""
    length = random.randint(10, 20)
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))