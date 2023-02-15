import pygame
import logging
import util.system

log = logging.Logger(__name__)
running = True
pygame.init()
screen = util.system.Screen()
bgmusic = util.system.Music()
Map = util.system.Map("")
player = util.player

log.debug("start loading the map")
Map.load_map()
log.debug("Map loading is done")

screen.draw(Map.surface, pygame.Rect(0,0,600,400))
screen.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.quit()
            bgmusic.quit()
