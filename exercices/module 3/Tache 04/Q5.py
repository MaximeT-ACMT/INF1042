code = input("Écrire le code postal(ex: L8P 1A1): ")

if len(code) == 7 and code[3] == " ":
    print(True)
else:
    print(False)
    # Pour être honnête j'ai fait des recherches pour cette question