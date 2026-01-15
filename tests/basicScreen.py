from src.GameBox import *
import pygame
import os

width, height = 1400, 900
game = Game(width, height, "blue", "First Game!")
win = game.get_screen()

Keys.init()

cam = Cammera()

player = Player((width / 2, height / 4), (50, 50), "green", False)  
player.add_physics(1.0, 3.0, 16, 7.0, 0.5)

map = TileMap("tests/levelTiles.png", (16, 16), 5, (25, 25), 0)
map.load_map_from_json("tests/testMap.json")
map.activate_editor(Keys.tab)

player.sprite.add_animated_sprite_2d("tests/Player.png", (5, 1), (32, 32), 5, 0.075, 2.0, True, 1)

#player.set_dim_as_sprite()

cam.set_follow_target(player)
#cam.move(-50, -50)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    player.top_down_movement()


    game.update(events, 60)


game.quit()
pygame.quit()
os.system("cls")