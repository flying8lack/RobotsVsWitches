import pygame.sprite


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(self)
        self.x = 12
        self.y = 13
        self.image = pygame.surface.Surface([16, 16])#pygame.image.load("data\\texture\\player.png")
        self.image.fill((255, 0, 255))
        self.rect = pygame.Rect(self.x, self.y, 16, 16)

