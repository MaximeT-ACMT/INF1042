Côté1 = float(input("Côté 1: "))
Côté2 = float(input("Côté 2: "))
Côté3 = float(input("Côté 3: "))

triangle = (Côté1 + Côté2 > Côté3 and Côté1 + Côté3 > Côté2 and Côté2 + Côté3 > Côté1)

print(triangle)