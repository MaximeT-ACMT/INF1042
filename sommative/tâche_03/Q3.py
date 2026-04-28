list_a = ["Drums", "Bass", "Piano", "Bass", "Guitar", "Drums"]
list_b = ["Piano", "Vocals", "Guitar", "Synth", "Piano"]

# Remove the duplicates by converting the lists to sets and printing the results
set_a = set(list_a)
set_b = set(list_b)

print("2. Unique songs in A:", set_a)
print("   Unique songs in B:", set_b)

# Items in both sets and then print the results
both = set_a.intersection(set_b)
print("3. Songs in both lists:", both)

# Items in only one of the sets and then print the results
only_one = set_a.symmetric_difference(set_b)
print("4. Songs in only one list:", only_one)

# Combining both sets to get all unique songs and then print the results
all_unique = set_a.union(set_b)
print("5. All unique songs combined:", all_unique)