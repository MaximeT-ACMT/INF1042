mots = ["chat", "chien", "chat", "oiseau", "chien", "chat"]
count = {}

for mot in mots:
    if mot in count:
        count[mot] = count[mot] + 1
    else:
        count[mot] = 1

print(count)