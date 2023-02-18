from abc import ABC

import pygame

import Items.baseItem


class GunItem(Items.baseItem.BaseItem):

    def saveData(self):
        pass

    def readData(self):
        pass

    def use(self):
        pass

    def get_texture_location(self):
        return ""

    def get_rect(self):
        return self.surface.get_rect()

    def get_surface(self):
        return self.surface

    def __init__(self):
        super().__init__()
        #self.surface = pygame.image.load(self.get_texture_location())
        pass
