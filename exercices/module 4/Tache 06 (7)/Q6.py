import random  

students = { "Maksym Bicz", "Léonidas Charron", "Hayden Cornelsen", "Angel Mekontchou Zeulefack", "Ibrahim", "Josh Paiement", "Grant Philippe-Daniel", "Maxime Talbot", "David Toussaint" }

print("--- Random Name Generator for INF1042 Students ---")

while len(students) > 0:
    
    picked_name = students.pop()
    
    print("Le nom choisi est : " + picked_name)
    
    print("There is " + str(len(students)) + " Name left to be picked.")
    print("--------------------")

print(" All Names have been picked! ")