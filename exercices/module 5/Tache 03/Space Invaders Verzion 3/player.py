import pygame

class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.centerx = 450
        self.rect.bottom = 580

        self.speed = 6

        self.max_health = 100
        self.health = 100

        self.gun = "pistol"

    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        self.rect.x = max(0, min(self.rect.x, 850))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # health bar
        pygame.draw.rect(screen, (255, 0, 0), (20, 550, 200, 20))
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (20, 550, 200 * (self.health / self.max_health), 20)
        )