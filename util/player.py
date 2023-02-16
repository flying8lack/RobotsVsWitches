import logging
import math

import pygame.sprite

import util.system


class Player(pygame.sprite.Sprite):
    MAX_MAP_SIZE = 32

    def __init__(self, map_obj: util.system.Map):
        super().__init__(pygame.sprite.Group())

        self.map_obj = map_obj

        self.walk_time = 20
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
        if not (self.x + x >= self.MAX_MAP_SIZE or
                self.y + y >= self.MAX_MAP_SIZE or
                self.x + x < 0 or
                self.y + y < 0):
            self.x += x
            self.y += y
            self.update_rect()

    def check_for_movement_event(self, event: pygame.event.Event):
        logging.debug("checking for player movement event")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:

                if not self.map_obj[self.x + 1][self.y].collide(self.image.get_rect()):
                    self.move(1, 0)


            elif event.key == pygame.K_a:
                if not self.map_obj[self.x - 1][self.y].collide(self.image.get_rect()):
                    self.move(-1, 0)

            elif event.key == pygame.K_w:
                if not self.map_obj[self.x][self.y - 1].collide(self.image.get_rect()):
                    self.move(0, -1)
            elif event.key == pygame.K_s:
                if not self.map_obj[self.x][self.y + 1].collide(self.image.get_rect()):
                    self.move(0, 1)
