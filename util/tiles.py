import pygame




class Tile:

    def __init__(self, path: str, pos, solid: bool):
        self.surface = pygame.image.load("data\\tiles\\"+path)
        self.solid = solid
        self.Rect = pygame.Rect(pos.x, pos.y, 8, 8)

    def collide(self, pos) -> bool:
        if self.solid:
            return self.Rect.collidepoint(pos.x, pos.y)
        else:
            return False
