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
        return "data\\texture\\items\\gun.png"

    def get_rect(self):
        return self.surface.get_rect()

    def get_surface(self):
        return self.surface

    def __init__(self):
        self.surface = pygame.image.load(self.get_texture_location())

