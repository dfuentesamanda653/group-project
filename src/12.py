import random

def generate_random_code(length):
    """Generate a random string of letters and digits"""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(letters) for _ in range(length))