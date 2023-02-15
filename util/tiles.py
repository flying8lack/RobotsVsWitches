import pygame

import util.system


class Tile:

    def __init__(self, path: str, pos: util.system.Vector, solid: bool):
        self.surface = pygame.image.load(path)
        self.solid = solid
        self.Rect = pygame.Rect(pos.x, pos.y, 8, 8)

    def collide(self, pos: util.system.Vector) -> bool:
        if self.solid:
            return self.Rect.collidepoint(pos.x, pos.y)
        else:
            return False
