import pygame
import math

class Enemy:

    def __init__(self, x, y, boss=False):

        self.boss = boss

        size = (80, 60) if boss else (40, 30)

        self.image = pygame.Surface(size)
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # slower than player
        self.speed = 1

        self.health = 50 if boss else 1

        self.damage = 10 if boss else 5

    def update(self, player):

        # MOVE TOWARD PLAYER
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y

        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance != 0:
            dx /= distance
            dy /= distance

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def create_enemies(level=1):

    enemies = []

    # BOSS LEVEL
    if level == 10:

        enemies.append(
            Enemy(400, 100, True)
        )

        return enemies

    rows = 1 + level
    cols = 3 + level

    for row in range(rows):
        for col in range(cols):

            enemies.append(
                Enemy(
                    80 + col * 80,
                    60 + row * 60
                )
            )

    return enemies