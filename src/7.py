import random 
def get_random_code(): 
return ''.join(random.choice('0123456789abcdef') for _ in range(8)) 