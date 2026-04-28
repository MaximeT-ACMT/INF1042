notes = [78, 85, 92, 67, 85, 74]

# Display the list
print("1. Full list:", notes)

# Print the first and last notes in the list
print("2. First grade:", notes[0], "| Last grade:", notes[-1])

# Adding 88 (Like my average in school lol)
notes.append(88)

# Remove 85
notes.remove(85)

print("5. Updated list:", notes)

# Calculate total, average, highest, and lowest notes
total = sum(notes)
average = total / len(notes)
highest = max(notes)
lowest = min(notes)

# print the results
print(f"6. Total: {total}, Average: {average:.2f}, High: {highest}, Low: {lowest}")