import pygame.sprite


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(pygame.sprite.Group())
        self.x = 12
        self.y = 13
        self.image = pygame.surface.Surface([16, 16])  # pygame.image.load("data\\texture\\player.png")
        self.image.fill((255, 0, 255))
        self.rect = pygame.Rect(self.x * 16, self.y * 16, 16, 16)

    def update_rect(self):
        self.rect = pygame.Rect(self.x * 16, self.y * 16, 16, 16)

    def moveTo(self, x, y):
        self.x, self.y = x, y
        self.update_rect()

    def move(self, x, y):
        self.x += x
        self.y += y
        self.update_rect()
