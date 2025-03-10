
import random

def get_random_python_code():
    """Generate a random Python code"""
    # Generate a random number of lines
    num_lines = random.randint(1, 10)

    # Generate a random number of statements per line
    num_statements_per_line = random.randint(1, 5)

    code = ""
    for i in range(num_lines):
        # Generate a random number of statements
        for j in range(num_statements_per_line):
            # Generate a random statement
            statement = "".join([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(random.randint(1, 20))])
            code += f"{statement}\n"

    return code