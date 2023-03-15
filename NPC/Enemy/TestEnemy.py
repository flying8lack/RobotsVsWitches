import pygame

from NPC.Enemy.AbstractEnemy import AbstractEnemy
from battle.Stats import Stat


class TestEnemy(AbstractEnemy):

    def __init__(self):
        self.surface = pygame.Surface([16, 16])
        self.surface.fill((240, 98, 20))
        self.stat = Stat(12)

    def get_stat(self) -> Stat:
        return self.stat

    def get_name(self) -> str:
        return "TEST"

    def get_surface(self):
        return self.surface

    def get_battle_surface(self):
        return self.surface

    def get_battle_rect(self):
        return self.surface.get_rect()

    def get_rect(self):
        return self.surface.get_rect()
