# enemy

import pygame
from settings import Settings


class Enemy:

    direction = 1

    def __init__(self, x, y):

        self.rect = pygame.Rect(
            x,
            y,
            Settings.ENEMY_WIDTH,
            Settings.ENEMY_HEIGHT
        )

    def update(self):

        self.rect.x += Settings.ENEMY_SPEED * Enemy.direction

    def draw(self, screen):

        pygame.draw.rect(screen, Settings.RED, self.rect)


def create_enemies():

    enemies = []

    rows = 3
    cols = 8

    for row in range(rows):

        for col in range(cols):

            x = 80 + col * 80
            y = 50 + row * 60

            enemies.append(Enemy(x, y))

    return enemies