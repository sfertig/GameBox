from src.GameBox import *
import pygame

pygame.init()
Keys.init()

width, height = 1400, 800

game = Game(width, height)
cam = Cammera()

shape = Rect((0, 0), (100, 100), (255, 255, 255))

player = Player((width/2, height/2), (50, 50), (255, 255, 255))
player.add_physics(0, 0, 0, (25, 25), (0.8, 0.8))

map = TileMap("tests/levelTiles.png", (16, 16), 5, (25, 25), 0)
map.load_map_from_json("tests/testMap.json")
map.activate_editor(Keys.tab)


cam.set_target(player)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    player.move.by_WSAD(2)

    game.update(events)

game.quit()
pygame.quit()
