import pygame

import util.system

pygame.init()
screen = util.system.Screen()
bgmusic = util.system.Music()

running = True
screen.draw()
screen.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.quit()
            bgmusic.quit()
