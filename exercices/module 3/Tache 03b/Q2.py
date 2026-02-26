def entrée_age(age):
    return age >= 18
age = int(input("C'est quoi ton age? "))
if entrée_age(age):
    print("Bienvenue ")
else:
    print("Accès n'ais pas permis")