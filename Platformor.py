from src.GameBox import *
import pygame
import os

Keys.init()

width, height = 800, 600

game = Game(width, height)
G = game._fetch_global()
screen = game.get_screen()

cam = Cammera(smooth=0.2)

player = Player((width/2, height/2), (50, 50), "green")
player.add_physics(0, 0, 0, (20, 20))
cam.set_target(player)

map = Tilemap("tests/assets/levelTiles.png", (16, 16), 4.0)
map.load_from_json("tests/assets/map1.json")

r = Rect((width/2, 0), (75, 35), "blue", show=False)


running = True
while running:
    events = pygame.event.get()
    for event in events:    
        if event.type == pygame.QUIT:
            running = False

    if Keys.is_pressed(Keys.c):
        os.system("cls")
        
    player.move.by_WSAD(3.0)

    game.update(events)

game.quit()
pygame.quit()
os.system("cls")
