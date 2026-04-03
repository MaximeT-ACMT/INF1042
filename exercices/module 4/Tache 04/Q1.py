notes = [12, 15, 9, 18, 15, 12]

moyenne = sum(notes) / len(notes)
print(moyenne)

plus_frequent = notes[0]
max_occurrences = 0

for n in notes:
    count = 0
    for x in notes:
        if x == n:
            count += 1
    
    if count > max_occurrences:
        max_occurrences = count
        plus_frequent = n

print(plus_frequent)