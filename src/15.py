import random 
def random_code(): 
    return "".join([str(random.randint(0,9)) for i in range(4)]) 