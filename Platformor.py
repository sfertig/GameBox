from src.GameBox import *
import pygame

width, height = 800, 600

game = Game(width, height)
G = game._fetch_global()
screen = game.get_screen()

cam = Cammera(smooth=0.2)

player = Player((width/2, height/2), (50, 50), "green")
player.add_physics(0, 0, 0)
cam.set_target(player)

map = Tilemap("tests/assets/levelTiles.png", (16, 16), 4.0)
map.load_from_json("tests/assets/map1.json")


running = True
while running:
    events = pygame.event.get()
    for event in events:    
        if event.type == pygame.QUIT:
            running = False

    player.move.by_WSAD(3.80)

    game.update(events)

game.quit()
pygame.quit()
