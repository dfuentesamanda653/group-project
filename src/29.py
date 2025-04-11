import math
def is_perfect_square(x):
    if x < 0:
        return False
    sqrt_x = int(math.sqrt(x))
    return sqrt_x * sqrt_x == x

print(is_perfect_square(16)) # True
print(is_perfect_square(-4)) # False
