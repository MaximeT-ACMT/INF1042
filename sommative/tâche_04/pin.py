import pygame
import math
from settings import *

class Pin(pygame.sprite.Sprite):
    def __init__(self, x, y, value, pin_id):
        super().__init__()
        self.value = value  
        self.pin_id = pin_id # Track exact position index (0 to 4)
        self.radius = PIN_RADIUS
        
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pin_color = GOLD if self.value == 5 else (WHITE if self.value == 3 else GREY)
        pygame.draw.circle(self.image, pin_color, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, RED, (self.radius, self.radius), self.radius, 2)
        
        self.rect = self.image.get_rect()
        self.x = float(x)
        self.y = float(y)
        self.rect.center = (int(self.x), int(self.y))
        
        self.vx = 0.0
        self.vy = 0.0
        self.is_down = False

    def update(self):
        if self.vx != 0 or self.vy != 0:
            self.x += self.vx
            self.y += self.vy
            self.vx *= FRICTION
            self.vy *= FRICTION
            self.rect.center = (int(self.x), int(self.y))
            
            if math.hypot(self.vx, self.vy) < 0.05:
                self.vx = 0.0
                self.vy = 0.0