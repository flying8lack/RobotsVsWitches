import pygame


class Vector:
    x: int
    y: int

class Map:

    def __init__(self):
        pass

    def 

class Music:

    def __init__(self):
        pygame.mixer.init()
        self.music_path = ""

    def load(self):
        pygame.mixer.music.load(self.music_path)

    def play(self):
        pygame.mixer.music.play(1)  # loops

    def stop(self):
        pygame.mixer.music.stop()

    def quit(self):
        self.stop()
        pygame.mixer.quit()


class Screen:

    def __init__(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode((600, 400))

    def draw(self, surface, dest, area):
        self.surface.blit(surface, dest, area)

    def quit(self):
        pygame.display.quit()

    def update(self):
        pygame.display.flip()
