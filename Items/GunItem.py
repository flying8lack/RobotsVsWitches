from abc import ABC

import pygame

import baseItem


class GunItem(baseItem.BaseItem):

    def get_texture_location(self):
        return ""

    def get_rect(self):
        return self.surface.get_rect()

    def get_surface(self):
        return self.surface

    def __init__(self):
        self.surface = pygame.image.load(self.get_texture_location())
