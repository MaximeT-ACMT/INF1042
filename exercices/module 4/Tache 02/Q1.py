import random
import os

os.makedirs("exemples/module4", exist_ok=True)

file_path = "exemples/module4/valeurs.txt"

with open(file_path, "w") as f:
    for _ in range(1000):
        value = random.randint(0, 100000)
        f.write(f"{value}\n")

print(f"File successfully created: {file_path}")