import random

def random_code():
    length = random.randint(5, 10)
    code = ""
    for i in range(length):
        code += chr(random.randint(65, 90))
    return code
