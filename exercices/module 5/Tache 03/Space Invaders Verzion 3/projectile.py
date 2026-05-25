import pygame

class Projectile:
    def __init__(self, x, y, gun="pistol"):
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        if gun == "pistol":
            self.speed = 10
            self.damage = 1

        elif gun == "rapid":
            self.speed = 14
            self.damage = 1

        elif gun == "shotgun":
            self.speed = 8
            self.damage = 3

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)