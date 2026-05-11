try:
    entree = input("Entrez votre âge : ")
    if not entree.isdigit():
        raise ValueError("l'âge doit être un nombre entier.")
    
    age = int(entree)
    print(f"Vous avez {age} ans.")

except ValueError as e:
    print(f"Erreur : {e}")