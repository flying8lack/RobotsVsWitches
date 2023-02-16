import pygame


class Tile(pygame.sprite.Sprite):

    def __init__(self, path: str, pos, solid: bool, *groups):
        super().__init__(*groups)
        self.surface = pygame.image.load("data\\tiles\\" + path)
        self.solid = solid
        self.Rect = self.surface.get_rect()#pygame.Rect(pos.x * 16, pos.y * 16, 16, 16)

    def collide(self, rect) -> bool:
        if self.solid:
            return self.Rect.colliderect(rect)
        else:
            return False
