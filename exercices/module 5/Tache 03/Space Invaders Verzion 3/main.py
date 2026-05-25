import pygame
import sys

from settings import Settings
from player import Player
from enemy import create_enemies
from projectile import Projectile
from shop import Shop
from save import load_save, save_game

pygame.init()

screen = pygame.display.set_mode(
    (Settings.WIDTH, Settings.HEIGHT)
)

pygame.display.set_caption(
    "ALIEN SHOOTER V3"
)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 28)

# =========================
# SAVE DATA
# =========================
save_data = load_save()

# =========================
# GAME OBJECTS
# =========================
player = Player()

shop = Shop()

level = 1
coins = 100
score = 0

enemies = create_enemies(level)

bullets = []

game_state = "SHOP"

# ROW MOVEMENT TIMER
current_row = 0
last_row_switch = pygame.time.get_ticks()

# LEVEL COMPLETE TIMER
level_complete_time = 0

running = True

# =========================
# GAME LOOP
# =========================
while running:

    clock.tick(Settings.FPS)

    current_time = pygame.time.get_ticks()

    # =========================
    # EVENTS
    # =========================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # ================= SHOP =================
        if game_state == "SHOP":

            if event.type == pygame.KEYDOWN:

                # BUY HEALTH
                if event.key == pygame.K_1 and coins >= 50:

                    player.health += 20

                    if player.health > player.max_health:
                        player.health = player.max_health

                    coins -= 50

                # BUY SHOTGUN
                if event.key == pygame.K_2 and coins >= 150:

                    player.gun = "shotgun"

                    coins -= 150

                # BUY RAPID
                if event.key == pygame.K_3 and coins >= 250:

                    player.gun = "rapid"

                    coins -= 250

                # START LEVEL
                if event.key == pygame.K_RETURN:

                    game_state = "PLAY"

        # ================= PLAY =================
        elif game_state == "PLAY":

            if event.type == pygame.KEYDOWN:

                # SHOOT
                if event.key == pygame.K_SPACE:

                    # SHOTGUN
                    if player.gun == "shotgun":

                        bullets.append(
                            Projectile(
                                player.rect.centerx - 15,
                                player.rect.top,
                                "shotgun"
                            )
                        )

                        bullets.append(
                            Projectile(
                                player.rect.centerx,
                                player.rect.top,
                                "shotgun"
                            )
                        )

                        bullets.append(
                            Projectile(
                                player.rect.centerx + 15,
                                player.rect.top,
                                "shotgun"
                            )
                        )

                    else:

                        bullets.append(
                            Projectile(
                                player.rect.centerx,
                                player.rect.top,
                                player.gun
                            )
                        )

        # ================= GAME OVER =================
        elif game_state == "GAMEOVER":

            if event.type == pygame.KEYDOWN:

                # RESTART
                if event.key == pygame.K_r:

                    player = Player()

                    level = 1
                    coins = 100
                    score = 0

                    enemies = create_enemies(level)

                    bullets = []

                    current_row = 0

                    game_state = "SHOP"

                # QUIT
                if event.key == pygame.K_q:

                    running = False

    # =========================
    # SHOP
    # =========================
    if game_state == "SHOP":

        shop.draw(
            screen,
            coins,
            player
        )

    # =========================
    # PLAY
    # =========================
    elif game_state == "PLAY":

        # PLAYER
        keys = pygame.key.get_pressed()

        player.move(keys)

        # ================= BULLETS =================
        for bullet in bullets[:]:

            bullet.update()

            if bullet.rect.bottom < 0:

                bullets.remove(bullet)

        # ================= CHANGE MOVING ROW EVERY 3 SECONDS =================
        if current_time - last_row_switch >= 3000:

            current_row += 1

            last_row_switch = current_time

            if current_row > 20:
                current_row = 0

        # ================= ENEMIES =================
        for enemy in enemies:

            enemy_row = enemy.rect.y // 60

            # ONLY ONE ROW MOVES
            if enemy_row == current_row:

                enemy.speed = 1 + (level * 0.1)

                enemy.update(player)

        # ================= BULLET COLLISION =================
        for bullet in bullets[:]:

            for enemy in enemies[:]:

                if bullet.rect.colliderect(enemy.rect):

                    enemy.health -= bullet.damage

                    if bullet in bullets:
                        bullets.remove(bullet)

                    # ENEMY DEAD
                    if enemy.health <= 0:

                        if enemy in enemies:
                            enemies.remove(enemy)

                        score += 10

                    break

        # ================= ENEMY TOUCH PLAYER =================
        for enemy in enemies[:]:

            if enemy.rect.colliderect(player.rect):

                player.health -= enemy.damage

                enemies.remove(enemy)

                if player.health <= 0:

                    game_state = "GAMEOVER"

        # ================= LEVEL COMPLETE =================
        if len(enemies) == 0:

            level_complete_time = current_time

            game_state = "LEVEL_COMPLETE"

        # ================= DRAW =================
        screen.fill(Settings.BLACK)

        # PLAYER
        player.draw(screen)

        # BULLETS
        for bullet in bullets:

            bullet.draw(screen)

        # ENEMIES
        for enemy in enemies:

            enemy.draw(screen)

        # ================= BOSS HEALTH BAR =================
        for enemy in enemies:

            if enemy.boss:

                pygame.draw.rect(
                    screen,
                    Settings.RED,
                    (250, 20, 400, 25)
                )

                pygame.draw.rect(
                    screen,
                    Settings.GREEN,
                    (
                        250,
                        20,
                        400 * (enemy.health / 50),
                        25
                    )
                )

        # ================= UI =================
        ui = font.render(
            f"Score: {score}   Coins: {coins}   Level: {level}   Health: {player.health}",
            True,
            Settings.WHITE
        )

        screen.blit(ui, (20, 20))

    # =========================
    # LEVEL COMPLETE SCREEN
    # =========================
    elif game_state == "LEVEL_COMPLETE":

        screen.fill(Settings.BLACK)

        complete_text = font.render(
            f"LEVEL {level} COMPLETED!",
            True,
            Settings.WHITE
        )

        next_text = font.render(
            "Next level starting...",
            True,
            Settings.WHITE
        )

        screen.blit(complete_text, (280, 250))
        screen.blit(next_text, (300, 320))

        # WAIT 3 SECONDS
        if current_time - level_complete_time >= 3000:

            coins += 100

            level += 1

            # GAME FINISHED
            if level > 10:

                game_state = "GAMEOVER"

                if score > save_data["best_score"]:

                    save_data["best_score"] = score

                    save_game(save_data)

            else:

                enemies = create_enemies(level)

                bullets = []

                current_row = 0

                game_state = "SHOP"

    # =========================
    # GAME OVER
    # =========================
    elif game_state == "GAMEOVER":

        screen.fill(Settings.BLACK)

        title = font.render(
            "GAME OVER",
            True,
            Settings.WHITE
        )

        score_text = font.render(
            f"Final Score: {score}",
            True,
            Settings.WHITE
        )

        best_text = font.render(
            f"Best Score: {save_data['best_score']}",
            True,
            Settings.WHITE
        )

        restart_text = font.render(
            "Press R to Restart",
            True,
            Settings.WHITE
        )

        quit_text = font.render(
            "Press Q to Quit",
            True,
            Settings.WHITE
        )

        screen.blit(title, (350, 180))
        screen.blit(score_text, (320, 250))
        screen.blit(best_text, (320, 300))
        screen.blit(restart_text, (280, 380))
        screen.blit(quit_text, (310, 430))

    pygame.display.flip()

pygame.quit()
sys.exit()