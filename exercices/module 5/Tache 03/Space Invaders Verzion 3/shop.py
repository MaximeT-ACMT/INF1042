import pygame

class Shop:

    def __init__(self):

        self.font = pygame.font.SysFont(None, 32)

    def draw(self, screen, coins, player):

        screen.fill((0, 0, 0))

        title = self.font.render(
            "SHOP",
            True,
            (255, 255, 255)
        )

        coins_text = self.font.render(
            f"Coins: {coins}",
            True,
            (255, 255, 255)
        )

        gun_text = self.font.render(
            f"Current Gun: {player.gun}",
            True,
            (255, 255, 0)
        )

        options1 = self.font.render(
            "1 = +20 Health (50 Coins)",
            True,
            (255, 255, 255)
        )

        options2 = self.font.render(
            "2 = Shotgun (150 Coins)",
            True,
            (255, 255, 255)
        )

        options3 = self.font.render(
            "3 = Rapid Gun (250 Coins)",
            True,
            (255, 255, 255)
        )

        options4 = self.font.render(
            "ENTER = Start Level",
            True,
            (255, 255, 255)
        )

        screen.blit(title, (390, 120))
        screen.blit(coins_text, (380, 170))
        screen.blit(gun_text, (340, 220))

        screen.blit(options1, (270, 300))
        screen.blit(options2, (270, 350))
        screen.blit(options3, (270, 400))
        screen.blit(options4, (300, 470))