import math

class Forme:
    def __init__(self, longueur):
        self.longueur = longueur

    def aire(self):
        pass

    def perimetre(self):
        pass

class Cercle(Forme):
    def aire(self):
        return math.pi * (self.longueur ** 2)
    
    def perimetre(self):
        return 2 * math.pi * self.longueur

class Triangle(Forme):
    def aire(self):
        return (math.sqrt(3) / 4) * (self.longueur ** 2)
    
    def perimetre(self):
        return 3 * self.longueur

class Rectangle(Forme):
    def aire(self):
        return self.longueur ** 2
    
    def perimetre(self):
        return 4 * self.longueur

class Pentagone(Forme):
    def aire(self):
        return (5 * self.longueur**2) / (4 * math.tan(math.pi / 5))
    
    def perimetre(self):
        return 5 * self.longueur

class Hexagone(Forme):
    def aire(self):
        return (3 * math.sqrt(3) / 2) * (self.longueur ** 2)
    
    def perimetre(self):
        return 6 * self.longueur

class Heptagone(Forme):
    def aire(self):
        return (7 * self.longueur**2) / (4 * math.tan(math.pi / 7))
    
    def perimetre(self):
        return 7 * self.longueur

class Octogone(Forme):
    def aire(self):
        return 2 * (1 + math.sqrt(2)) * (self.longueur ** 2)
    
    def perimetre(self):
        return 8 * self.longueur