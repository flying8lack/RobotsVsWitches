import pygame.image

import util.constants
from util.player import Player


class BattleScreen:

    def __init__(self, player):
        if not isinstance(player, Player):
            raise TypeError()

        self.enemies = None
        self.player: Player = player

        self.background = pygame.image.load("battle_background.png")
        self.final_surface = pygame.Surface((util.constants.SCREEN_WIDTH, util.constants.SCREEN_HEIGHT))

    def draw(self):
        self.final_surface.blit(self.background, self.background.get_rect())
