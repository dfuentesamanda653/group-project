import numpy as np

def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    average = np.mean(numbers)
    return round(average, 2)

# Example usage:
numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print(f"The average of the provided numbers is: {result}")
