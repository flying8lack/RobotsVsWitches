import json

import pygame

import util.tiles
import util.constants


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Map:

    def __init__(self, map_name: str):
        self.map_name = map_name
        self.surface = pygame.surface.Surface(pygame.Vector2(util.constants.SCREEN_WIDTH,
                                                             util.constants.SCREEN_HEIGHT))
        self.surface.fill((255, 255, 255), self.surface.get_rect())

    def load_map(self):

        with open("data\\map\\"+self.map_name, "r") as f:
            file = json.loads(f.read())

            for x in range(int(util.constants.SCREEN_WIDTH/util.constants.TILE_SIZE)):
                for y in range(int(util.constants.SCREEN_HEIGHT/util.constants.TILE_SIZE)):
                    self.surface.blit(
                        util.tiles.Tile(file["build"]["background"], Vector(x, y), False).surface,
                        (x * util.constants.TILE_SIZE, y * util.constants.TILE_SIZE,
                         util.constants.TILE_SIZE, util.constants.TILE_SIZE))


class Music:

    def __init__(self):
        pygame.mixer.init()
        self.music_id = ""

    def load(self):
        pygame.mixer.music.load("data\\sounds\\music\\" + self.music_id)

    @staticmethod
    def play():
        pygame.mixer.music.play(1)  # loops

    @staticmethod
    def stop():
        pygame.mixer.music.stop()

    def quit(self):
        self.stop()
        pygame.mixer.quit()


class Screen:

    def __init__(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode((util.constants.SCREEN_WIDTH, util.constants.SCREEN_HEIGHT))
        self.characters = pygame.sprite.Group()

    def draw(self, surface, dest):
        self.surface.blit(surface, dest)

    def draw_character(self):
        self.characters.draw(self.surface)

    @staticmethod
    def quit():
        pygame.display.quit()

    @staticmethod
    def update():
        pygame.display.flip()
