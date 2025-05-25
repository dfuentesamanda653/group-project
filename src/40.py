import random

def split_data(data, ratio):
    """
    Split data into training and testing sets.
    
    Args:
        data (list): The dataset to be split.
        ratio (float): The proportion of the dataset used for training.
        
    Returns:
        tuple: A pair of lists containing the training set and test set.
    """
    train_set = random.sample(data, int(len(data) * ratio))
    return [train_set, data - train_set]

# Example usage
data_points = range(10)
split_ratio = 0.8
training_data, test_data = split_data(data_points, split_ratio)

for point in training_data:
    print(point)
