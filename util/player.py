import math

import pygame.sprite


class Player(pygame.sprite.Sprite):
    MAX_MAP_SIZE = 32

    def __init__(self):
        super().__init__(pygame.sprite.Group())

        self.walk_time = 20*0.9
        self.x = 12
        self.y = 13
        self.image = pygame.surface.Surface([16, 16])  # pygame.image.load("data\\texture\\player.png")
        self.image.fill((255, 0, 255))
        self.rect = pygame.Rect(self.x * 16, self.y * 16, 16, 16)

    def update_rect(self):
        self.rect = pygame.Rect(self.x * 16, self.y * 16, 16, 16)

    @staticmethod
    def lerp():
        return

    def moveTo(self, x, y):
        self.x, self.y = x, y
        self.update_rect()

    def move(self, x, y):
        if not (self.x + x >= self.MAX_MAP_SIZE or
                self.y + y >= self.MAX_MAP_SIZE or
                self.x + x < 0 or
                self.y + y < 0):
            self.x += x
            self.y += y
            self.update_rect()

    def check_for_movement_event(self, event):
        kb_state = pygame.key.get_pressed()
        self.walk_time -= 1
        if self.walk_time < 1:
            if kb_state[pygame.K_d]:
                self.move(1, 0)
            elif kb_state[pygame.K_a]:
                self.move(-1, 0)
            elif kb_state[pygame.K_w]:
                self.move(0, -1)
            elif kb_state[pygame.K_s]:
                self.move(0, 1)
