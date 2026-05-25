# projectile

import pygame
from settings import Settings


class Projectile:

    def __init__(self, x, y):

        self.rect = pygame.Rect(
            x,
            y,
            Settings.BULLET_WIDTH,
            Settings.BULLET_HEIGHT
        )

    def update(self):

        self.rect.y -= Settings.BULLET_SPEED

    def draw(self, screen):

        pygame.draw.rect(screen, Settings.GREEN, self.rect)