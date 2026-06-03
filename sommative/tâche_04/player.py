import pygame
import math
import random
from settings import *

class BowlingBall(pygame.sprite.Sprite):
    def __init__(self, ball_profile=None):
        super().__init__()
        if ball_profile is None:
            ball_profile = {"name": "Standard", "color": (80, 20, 100), "style": "solid"}
            
        self.profile = ball_profile
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        self.generate_texture()
        
        self.rect = self.image.get_rect()
        self.vx = 0.0
        self.vy = 0.0
        self.x = 0.0
        self.y = 0.0
        self.state = 'aiming'
        self.reset()

    def generate_texture(self):
        base_c = self.profile["color"]
        style = self.profile["style"]
        center = (BALL_RADIUS, BALL_RADIUS)
        
        pygame.draw.circle(self.image, base_c, center, BALL_RADIUS)
        
        if style == "stripe":
            pygame.draw.line(self.image, WHITE, (0, BALL_RADIUS), (BALL_RADIUS*2, BALL_RADIUS), 3)
        elif style == "speckle":
            for _ in range(12):
                rx = random.randint(4, BALL_RADIUS*2 - 4)
                ry = random.randint(4, BALL_RADIUS*2 - 4)
                pygame.draw.circle(self.image, WHITE, (rx, ry), 1)
        elif style == "swirl":
            pygame.draw.circle(self.image, GOLD, (BALL_RADIUS-4, BALL_RADIUS-4), 5, 1)
            pygame.draw.circle(self.image, WHITE, (BALL_RADIUS+3, BALL_RADIUS+3), 4, 1)
        elif style == "spiral":
            pygame.draw.circle(self.image, RED, center, 8, 1)
            pygame.draw.circle(self.image, WHITE, center, 4, 1)
        elif style == "glitter":
            for _ in range(25):
                rx = random.randint(2, BALL_RADIUS*2 - 2)
                ry = random.randint(2, BALL_RADIUS*2 - 2)
                self.image.set_at((rx, ry), (255, 255, 255))
        elif style == "star":
            pygame.draw.polygon(self.image, WHITE, [
                (BALL_RADIUS, 4), (BALL_RADIUS+3, BALL_RADIUS-2),
                (BALL_RADIUS*2-4, BALL_RADIUS), (BALL_RADIUS+3, BALL_RADIUS+2),
                (BALL_RADIUS, BALL_RADIUS*2-4), (BALL_RADIUS-3, BALL_RADIUS+2),
                (4, BALL_RADIUS), (BALL_RADIUS-3, BALL_RADIUS-2)
            ])
        elif style == "marble":
            pygame.draw.ellipse(self.image, (40, 10, 0), (2, 4, 20, 10), 1)
            pygame.draw.ellipse(self.image, WHITE, (6, 2, 12, 22), 1)

        pygame.draw.circle(self.image, (255, 255, 255, 90), (BALL_RADIUS-4, BALL_RADIUS-4), 3)

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.rect.center = (int(self.x), int(self.y))
        self.vx = 0.0
        self.vy = 0.0
        self.state = 'aiming'
        self.angle = 0.0
        self.angle_direction = 1.1  
        self.power = 0.0
        self.power_direction = 2.0  

    def update(self):
        if self.state == 'aiming':
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.x > 270:
                self.x -= 4
            if keys[pygame.K_RIGHT] and self.x < 630:
                self.x += 4
            self.rect.centerx = int(self.x)

            self.angle += self.angle_direction
            if abs(self.angle) > 35:
                self.angle_direction *= -1

        elif self.state == 'power':
            self.power += self.power_direction
            if self.power >= 100:
                self.power = 100
                self.power_direction = -2.0  
            elif self.power <= 0:
                self.power = 0
                self.power_direction = 2.0   

        elif self.state == 'launched':
            self.x += self.vx
            self.y += self.vy
            self.vx *= FRICTION
            self.vy *= FRICTION
            self.rect.center = (int(self.x), int(self.y))

            if self.x < 250 or self.x > 650:
                self.vx = 0  
                if self.vy < -1: self.vy = -4 

            if self.y < -50 or (abs(self.vx) < 0.05 and abs(self.vy) < 0.05):
                self.state = 'done'

    def handle_input(self, event):
        is_trigger = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_trigger = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            is_trigger = True

        if is_trigger:
            if self.state == 'aiming':
                self.state = 'power'
            elif self.state == 'power':
                max_speed = 15.0
                speed = (self.power / 100.0) * max_speed + 3.5  
                rad = math.radians(self.angle - 90)
                self.vx = speed * math.cos(rad)
                self.vy = speed * math.sin(rad)
                self.state = 'launched'

    def draw_overlays(self, surface):
        if self.state == 'aiming':
            rad = math.radians(self.angle - 90)
            end_x = self.x + 70 * math.cos(rad)
            end_y = self.y + 70 * math.sin(rad)
            pygame.draw.line(surface, RED, self.rect.center, (end_x, end_y), 3)

        elif self.state == 'power':
            meter_x, meter_y = 40, 450
            pygame.draw.rect(surface, BLACK, (meter_x, meter_y, 30, 150), 2)
            fill_height = int((self.power / 100.0) * 146)
            color = (int((self.power/100)*255), int((1 - self.power/100)*255), 0)
            pygame.draw.rect(surface, color, (meter_x + 2, meter_y + 148 - fill_height, 26, fill_height))