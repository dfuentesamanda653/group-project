import random

def generate_random_number():
    number = random.randint(1, 100)
    return number

random_number = generate_random_number()
print(random_number)
