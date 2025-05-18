import math
import random

def draw_random_polygon(sides: int) -> list[tuple[int, int]]:
    """
    Draw a random polygon with given number of sides.
    
    Args:
        sides (int): Number of sides for the polygon.
        
    Returns:
        list[tuple[int, int]]: A list of tuples representing the vertices of the polygon.
    """
    return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(sides)]

def draw_random_color_polygon(sides: int, colors: set) -> list[tuple[int, int]]:
    """
    Draw a random colored polygon with given number of sides and allowed colors.
    
    Args:
        sides (int): Number of sides for the polygon.
        colors (set): A set of valid colors for each side of the polygon.
        
    Returns:
        list[tuple[int, int]]: A list of tuples representing the vertices of the colored polygon.
    """
    return [random.choice(tuple(colors)) for _ in range(sides)]

def main():
    sides = random.randint(3, 8)  # Randomly choose number of sides
    colors = set([i % 10 for i in range(256)])  # Randomly generate allowed colors
    
    polygon = draw_random_polygon(sides)
    colored_polygon = draw_random_color_polygon(sides, colors)

    print(f"Polygon with {sides} sides: {polygon}")
    print(f"Colored polygon with {sides} sides and allowed colors: {colored_polygon}")

if __name__ == "__main__":
    main()
