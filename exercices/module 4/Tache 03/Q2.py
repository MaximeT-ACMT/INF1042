import math

def get_distance(coordinates):
    x, y = coordinates
    return math.sqrt(x*2 + y*2)

point = (3, 4)
answer = get_distance(point)
print(f"The distance from {point} to (0,0) is: {answer}")