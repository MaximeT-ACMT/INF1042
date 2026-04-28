# Creating a dictionary 
inventory = {
    "stylo": 24,
    "cahiers": 15,
    "gommes": 10
}

print("2. Quantity of cahiers:", inventory["cahiers"])

# adding markers and modifying pens
inventory["marqueurs"] = 18
inventory["stylo"] = 30

# Removing erasers
del inventory["gommes"]

print("6. Current inventory:")
# what item and the amount of that item
for item, qty in inventory.items():
    print(f"- {item}: {qty}")


total_items = sum(inventory.values())
print("7. Total items in stock:", total_items)