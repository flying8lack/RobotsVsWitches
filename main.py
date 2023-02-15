import pygame
import logging
import util.system
import util.player

log = logging.Logger(__name__)
running = True
pygame.init()
screen = util.system.Screen()
bgmusic = util.system.Music()
Map = util.system.Map("")
player = util.player.Player()

log.debug("start loading the map")
Map.load_map()
log.debug("Map loading is done")


while running:
    screen.draw(Map.surface, pygame.Rect(0, 0, 600, 400))
    screen.draw(player.image, player.rect)
    screen.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.quit()
            bgmusic.quit()

        if event.type == pygame.KEYDOWN:
            if event.dict["key"] == pygame.K_d:

                player.move(1, 0)
