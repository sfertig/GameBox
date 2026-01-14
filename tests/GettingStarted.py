import pygame
from src.GameBox import *

width, height = 800, 600

game = Game(width, height, "blue", "First Game!")
screen = game.get_screen()

cam = Cammera()

Keys.init()

player = Player((width / 2, height / 2), (64, 64), "green", False)
player.add_physics(1.0, 3.0, 16, 7.0, 0.5)


rect = Rect((0, 0), (64, 64), "red", True)

print(player.x, player.y)

#cam.set_follow_target(player)
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
