from src.GameBox import *
import pygame

width, height = 800, 600
game = Game(width, height, "blue", "First Game!")
win = game.get_screen()

cam = Cammera()

player = Player((width / 2, 375), (50, 50), "green", False)
player.add_physics(1.0, 3.0, 16, 7.0, 0.5)

map = TileMap("tests/levelTiles.png", (16, 16), (25, 25), 0, (0, 0))


cam.set_follow_target(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.top_down_movement()

    game.update(60)

pygame.quit()