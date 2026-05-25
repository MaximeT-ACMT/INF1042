# main

import pygame
import sys

from settings import Settings
from player import Player
from projectile import Projectile
from enemy import Enemy, create_enemies


pygame.init()

screen = pygame.display.set_mode(
    (Settings.WIDTH, Settings.HEIGHT)
)

pygame.display.set_caption(Settings.TITLE)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

player = Player()

enemies = create_enemies()

bullets = []

score = 0

running = True

while running:

    clock.tick(Settings.FPS)

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bullet = Projectile(
                    player.rect.centerx,
                    player.rect.top
                )

                bullets.append(bullet)

    # MOVEMENT
    keys = pygame.key.get_pressed()

    player.move(keys)

    # UPDATE BULLETS
    for bullet in bullets[:]:

        bullet.update()

        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    # UPDATE ENEMIES
    edge_hit = False

    for enemy in enemies:

        enemy.update()

        if enemy.rect.right >= Settings.WIDTH:
            edge_hit = True

        if enemy.rect.left <= 0:
            edge_hit = True

    if edge_hit:

        Enemy.direction *= -1

        for enemy in enemies:
            enemy.rect.y += Settings.ENEMY_DROP

    # COLLISIONS
    for bullet in bullets[:]:

        for enemy in enemies[:]:

            if bullet.rect.colliderect(enemy.rect):

                if bullet in bullets:
                    bullets.remove(bullet)

                if enemy in enemies:
                    enemies.remove(enemy)

                score += 10

                break

    # DRAW
    screen.fill(Settings.BLACK)

    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    score_text = font.render(
        f"Score: {score}",
        True,
        Settings.WHITE
    )

    screen.blit(score_text, (20, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()