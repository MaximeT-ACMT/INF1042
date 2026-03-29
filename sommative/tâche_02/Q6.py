# [Your Name]
# Calculates parking fees based on duration, hourly rates, and electric vehicle discounts.

hours = float(input("Number of hours parked: "))
is_electric = input("Is the car electric? (yes/no): ").lower() == "yes"

if (hours <= 1):
    cost = 4
else:
    cost = 4 + (hours - 1) * 3

if (hours > 5):
    cost += 10

if (is_electric):
    cost = cost * 0.80

print(f"Total parking cost: ${cost:.2f}")