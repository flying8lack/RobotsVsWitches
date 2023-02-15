import pygame

import util.tiles


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Map:

    def __init__(self, map_name: str):
        self.map_name = map_name
        self.surface = pygame.surface.Surface((600, 400))
        self.surface.fill((255, 255, 255), self.surface.get_rect())

    def load_map(self):
        # file = json.loads("data/map/"+self.map_name)
        for x in range(75):
            for y in range(50):
                self.surface.blit(util.tiles.Tile("green.png", Vector(x, y), False).surface, (x * 8, y * 8, 8, 8))


class Music:

    def __init__(self):
        pygame.mixer.init()
        self.music_id = ""

    def load(self):
        pygame.mixer.music.load("data\\sounds\\music\\" + self.music_path)

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
        self.surface = pygame.display.set_mode((600, 400))
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
