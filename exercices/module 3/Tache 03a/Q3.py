# Trouve la moyenne des 2 numéros
# Les 2 numéros
num1 = float(input("Écrire numéro 1: "))
num2 = float(input("Écrire numéro 2: "))
# Maintenant, calculer la moyenne
average = (num1 + num2) / 2
# Arrondir la réponse (si on a besoin)
average_arrondir = round(average,2)
# Imprimer le résultat 
print("La moyenne est: " + str(average_arrondir))