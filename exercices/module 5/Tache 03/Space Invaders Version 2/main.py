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

font = pygame.font.SysFont(None, 32)

player = Player()

enemies = create_enemies()

bullets = []

score = 0

# TIMER
start_time = pygame.time.get_ticks()

# RESPAWN TIMER
last_respawn = pygame.time.get_ticks()

running = True

while running:

    clock.tick(Settings.FPS)

    current_time = pygame.time.get_ticks()

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

    # PLAYER MOVEMENT
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

    # RESPAWN ENEMIES EVERY 10 SECONDS
    if current_time - last_respawn >= Settings.RESPAWN_TIME:

        enemies = create_enemies()

        last_respawn = current_time

    # GAME TIMER
    elapsed_seconds = (current_time - start_time) // 1000

    time_left = Settings.GAME_TIME - elapsed_seconds

    if time_left <= 0:
        running = False

    # DRAW
    screen.fill(Settings.BLACK)

    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    # SCORE
    score_text = font.render(
        f"Score: {score}",
        True,
        Settings.WHITE
    )

    screen.blit(score_text, (20, 20))

    # TIMER
    timer_text = font.render(
        f"Time Left: {time_left}",
        True,
        Settings.WHITE
    )

    screen.blit(timer_text, (600, 20))

    # CONTROLS
    controls_text = font.render(
        "WASD = Move   SPACE = Shoot",
        True,
        Settings.WHITE
    )

    screen.blit(controls_text, (180, 20))

    pygame.display.flip()

# GAME OVER SCREEN
screen.fill(Settings.BLACK)

game_over_text = font.render(
    f"Time's Up! Final Score: {score}",
    True,
    Settings.WHITE
)

screen.blit(game_over_text, (220, 300))

pygame.display.flip()

pygame.time.delay(5000)

pygame.quit()
sys.exit()