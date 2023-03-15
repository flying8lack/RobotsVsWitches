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

        self.choice_locked = False
        self.execute_turn = False

        self.enemy: AbstractEnemy = enemy
        self.player: Player = player

        self.background = pygame.Surface((512, 512))
        self.background.fill((32, 32, 32))
        self.final_surface = pygame.Surface((util.constants.SCREEN_WIDTH, util.constants.SCREEN_HEIGHT))

        self.block_e = pygame.Surface((16, 16))
        self.block_e.fill((255, 255, 240))
        self.block_e_x: int = 256
        self.block_e_y: int = int(512 / 2) - 32
        self.block_e_rect = (self.block_e_x, self.block_e_y)

        self.block_p = pygame.Surface((16, 16))
        self.block_p.fill((255, 255, 240))
        self.block_p_x: int = 256
        self.block_p_y: int = int(512 / 2)
        self.block_p_rect = (self.block_p_x, self.block_p_y)


    def set_enemy_choice(self, choice: int):
        if choice >= 2:
            choice = 2

        elif choice <= 0:
            choice = 0
        self.block_e_x = 64 + choice * (128 + 64)
        self.block_e_rect = (self.block_e_x, self.block_e_y)

    def path_choice(self, choice: int):
        if self.choice_locked:
            return
        if choice >= 2:
            choice = 2
        elif choice <= 0:
            choice = 0
        self.block_p_x = 64 + choice * (128 + 64)
        self.block_p_rect = (self.block_p_x, self.block_p_y)

    def draw(self):
        self.block_p_rect = pygame.Rect(self.block_p_x, self.block_p_y, 16, 16)
        self.block_e_rect = pygame.Rect(self.block_e_x, self.block_e_y, 16, 16)

        self.final_surface.blit(self.background, self.background.get_rect())
        pygame.draw.line(self.final_surface, (255, 255, 255), (64 + 32, 256 - 64), (64 + 32, 256 + 64))
        pygame.draw.line(self.final_surface, (255, 255, 255), (64 + (128 + 64) + 32, 256 - 64), (64 + 32 + (128 + 64), 256 + 64))
        pygame.draw.line(self.final_surface, (255, 255, 255), (64 + 32 + 2*(128 + 64), 256 - 64), (64 + 32 + 2*(128 + 64), 256 + 64))
        self.final_surface.blit(self.player.battle_image, self.player.battle_rect)
        self.final_surface.blit(self.block_p, self.block_p_rect)
        self.final_surface.blit(self.block_e, self.block_e_rect)

        self.draw_gui()

    def draw_gui(self):
        font = pygame.font.SysFont(None, 20)

        self.final_surface.blit(font.render("Player's Health: " + str(self.player.stat.health), True, (255, 255, 255)),
                                (40 + 512 / 2, 512 - 128, 10, 10))
        self.final_surface.blit(
            font.render(f"{self.enemy.get_name()}'s Health: {self.enemy.get_stat().health}", True, (255, 255, 255)),
            ((512 / 2) + 40, 128, 10, 10))
        if self.choice_locked:
            self.final_surface.blit(font.render("CHOICE LOCKED!", True, (255, 40, 40)), ((512 / 2) - 40, 256, 10, 10))
