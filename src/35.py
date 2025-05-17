import sys

def calculate_area(radius):
    area = 3.14 * radius ** 2
    print(f"The area of the circle with radius {radius} is {area}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a radius.")
    else:
        radius = float(sys.argv[1])
        calculate_area(radius)
