import pygame
from src.GameBox import *


width = 800
height = 600

game = Game(width, height)
screen = game.get_screen()

cam = Cammera()


player = Player((width / 2, height / 2), (50, 50), "green")
player.add_physics(0, 0, 0, (25, 25), (0.75, 0.75))

cam.set_target(player)

#create world bounds
color = "blue"
top = Rect((0, -10), (width, 10), color)
left = Rect((-10, 0), (10, height), color)
right = Rect((width, 0), (10, height), color)
bottom = Rect((0, height), (width, 10), color)


running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    player.move.by_WSAD(3.75)

    game.update(events, fps=60)

game.quit()
pygame.quit()
