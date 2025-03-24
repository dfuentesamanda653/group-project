import numpy as np
from scipy.stats import norm

def calculate_z_score(data):
    mean = data.mean()
    std_dev = data.std()
    z_score = (data - mean) / std_dev
    return z_score

# Example usage:
data_points = [1, 2, 3, 4, 5]
z_scores = calculate_z_score(data_points)
print(z_scores)
