import pygame
import sys
from src.GameBox import *
from random import randint as Ri

width, height = 1040, 540
game = Game(width, height, "blue", resizable=True)
screen = game.get_screen()

cam = Cammera()

player = Player(pygame.Vector2(width / 2, height / 2), pygame.Vector2(50, 50), "red")
player.add_physics(0, 0, 0, pygame.Vector2(25, 25), pygame.Vector2(0.5, 0.5))

orbs = []
#fill in list
for _ in range(7) : # this will be the number of orbs
	pos = pygame.Vector2(Ri(0, width), Ri(0, height))
	size = Ri(25, 50)
	color = (Ri(0, 255), Ri(0, 255), Ri(0, 255))
	orbs.append(Rect(pos, pygame.Vector2(size, size), color, collision=False))

game.generate_bounds(width, height)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE: game.rescale(event)

    player.move.by_WSAD(4)

    game.update(events, fps=60)
