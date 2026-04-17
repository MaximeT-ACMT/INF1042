import random

set_a = {random.randint(1, 20) for _ in range(10)}
set_b = {random.randint(1, 20) for _ in range(10)}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union :", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference :", set_a - set_b)