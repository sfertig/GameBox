import pygame
import os
from src.GameBox import *

width, height = 800, 600

game = Game(width, height, "blue", "First Game!")
screen = game.get_screen()
game._set_debug(True)

cam = Cammera()

Keys.init()

player = Player((width / 2, height / 2), (64, 64), "green", False)
player.add_physics(1.0, 3.0, 16, 7.0, 0.5)

player.sprite.add_animation_player(2.0)
player.sprite.add_animation("Walk", "tests/Player.png", (5, 1), (32, 32), 5, 0.075, 2.0, 1)
player.sprite.add_animation("Idle", "tests/Player.png", (5, 1), (32, 32), 1, 0.075, 2.0, 1)

player.sprite.set_animation("Idle")


stateTree = {
    "Idle": {Conditions.velocity_any: "Walk"},
    "Walk": {Conditions.velocity_none: "Idle"}
}
player.sprite.set_states(stateTree, "Walk")

rect = Rect((width / 2, height / 4), (64, 64), "red", True)


cam.set_follow_target(player)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    
    player.top_down_movement()
    game.update(events, 60)

    #print player state
    os.system("cls")
    print(player.sprite.state)

    if Keys.is_pressed(pygame.K_i):
        game._set_debug(not game._get_debug_state())

    
game.quit()
pygame.quit()
os.system("cls")
