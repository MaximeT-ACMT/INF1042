# Maxime Talbot
# Simulates random numbers between 1 and 4 and displays the percentage of each.

import random

iterations = int(input("How many values do you want to simulate? "))

count1 = count2 = count3 = count4 = 0

for _ in range(iterations):
    num = random.randint(1, 4)
    if (num == 1):
        count1 += 1
    elif (num == 2):
        count2 += 1
    elif (num == 3):
        count3 += 1
    elif (num == 4):
        count4 += 1

results = [count1, count2, count3, count4]
for i in range(4):
    percentage = (results[i] / iterations) * 100
    print(f"Value {i+1}: {results[i]} times ({percentage:.1f} %)")