import pygame
import logging
import util.system
import util.player
import util.constants

logging.basicConfig(level=logging.INFO)
#log = logging.getLogger("game")

running = True
pygame.init()
screen = util.system.Screen()
bgmusic = util.system.Music()
Map = util.system.Map("home.json")

clock = pygame.time.Clock()

logging.info("start loading the map")
Map.load_map()
logging.info("Map loading is done")
Map.draw_map()


player = util.player.Player(Map.map)

while running:
    dt = clock.tick(20)  # 20 fps
    screen.draw(Map.surface, pygame.Rect(0, 0, util.constants.SCREEN_WIDTH, util.constants.SCREEN_HEIGHT))
    screen.draw(player.image, player.rect)

    if player.inventory.draw_surface():
        screen.draw(player.inventory.surface, player.inventory.surface.get_rect())

    screen.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.quit()
            bgmusic.quit()
            break

        player.check_for_movement_event(event)

logging.debug("Closing down the program")