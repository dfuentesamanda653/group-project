import random
def get_random_number(n):
    return random.randint(0, n)

def get_random_string(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        result += random.choice(alphabet)
    return result
