import pygame.event

from NPC.Enemy.AbstractEnemy import AbstractEnemy
from battle.BattleScreen import BattleScreen
from util.player import Player

import random


class Battle:

    def __init__(self, player: Player, enemy: AbstractEnemy, screen):
        self.screen = BattleScreen(player, enemy)
        self.screen_handle = screen
        self.battle_ended = False

    def game_logic(self):

        if self.screen.choice_locked:
            self.screen.set_enemy_choice(random.randint(0, 2))
            if self.screen.block_p_x == self.screen.block_e_x:
                self.screen.enemy.get_stat().health -= 5
            elif self.screen.block_p_x != self.screen.block_e_x:
                self.screen.player.stat.health -= 2

            if self.screen.enemy.get_stat().health <= 0:
                self.battle_ended = True

            if self.screen.player.stat.health <= 0:
                quit()


        self.screen.choice_locked = False

    def draw_to_screen(self):
        if self.battle_ended:
            return
        self.screen.draw()
        self.screen_handle.draw(self.screen.final_surface, self.screen.final_surface.get_rect())

    def event_handle(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.screen.choice_locked = True
            self.screen.set_enemy_choice(2)
        elif event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            if x <= 128:
                self.screen.path_choice(0)
            elif 256 >= x > 128:
                self.screen.path_choice(1)
            elif 256 + 128 >= x > 256:
                self.screen.path_choice(2)
            elif x > 256 + 128:
                self.screen.path_choice(3)

        self.game_logic()
