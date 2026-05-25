# player

import pygame
from settings import Settings


class Player:

    def __init__(self):

        self.rect = pygame.Rect(
            Settings.WIDTH // 2 - Settings.PLAYER_WIDTH // 2,
            Settings.HEIGHT - 70,
            Settings.PLAYER_WIDTH,
            Settings.PLAYER_HEIGHT
        )

    def move(self, keys):

        if keys[pygame.K_a]:
            self.rect.x -= Settings.PLAYER_SPEED

        if keys[pygame.K_d]:
            self.rect.x += Settings.PLAYER_SPEED

        if keys[pygame.K_w]:
            self.rect.y -= Settings.PLAYER_SPEED

        if keys[pygame.K_s]:
            self.rect.y += Settings.PLAYER_SPEED

        # Keep inside screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > Settings.WIDTH:
            self.rect.right = Settings.WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > Settings.HEIGHT:
            self.rect.bottom = Settings.HEIGHT

    def draw(self, screen):

        pygame.draw.rect(screen, Settings.BLUE, self.rect)