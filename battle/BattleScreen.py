import pygame.image

import util.constants
from NPC.Enemy.AbstractEnemy import AbstractEnemy
from util.player import Player


class BattleScreen:

    def __init__(self, player, enemy):
        if not isinstance(player, Player):
            raise TypeError("player parameter must be a Player object")

        if not isinstance(player, Player):
            raise TypeError("enemy parameter must be an AbstractEnemy object")

        self.enemies: AbstractEnemy = enemy
        self.player: Player = player

        self.background = pygame.Surface((512, 512))
        self.background.fill((32, 32, 32))
        self.final_surface = pygame.Surface((util.constants.SCREEN_WIDTH, util.constants.SCREEN_HEIGHT))

    def draw(self):
        self.final_surface.blit(self.background, self.background.get_rect())
        self.final_surface.blit(self.player.battle_image, self.player.battle_rect)
        self.draw_gui()

    def draw_gui(self):
        font = pygame.font.SysFont(None, 20)

        self.final_surface.blit(font.render("Player's Health: " + str(self.player.stat.health), True, (255, 255, 255)),
                                (40 + 512 / 2, 512 - 128, 10, 10))
        self.final_surface.blit(
            font.render(f"{self.enemies.get_name()}'s Health: {self.enemies.get_stat().health}", True, (255, 255, 255)),
            ((512 / 2) + 40, 128, 10, 10))
