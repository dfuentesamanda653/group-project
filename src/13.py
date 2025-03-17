import random

def get_random_code():
    # Define a list of all possible characters for the code
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Define the length of the code
    length = 10
    # Create an empty string to store the generated code
    code = ""
    # Loop through the length of the code and add a random character from the list of possible characters to the string
    for i in range(length):
        code += random.choice(chars)
    return code