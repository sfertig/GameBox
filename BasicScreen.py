import pygame
import sys
from src.GameBox import *

width, height = 800, 600
game = Game(width, height, "blue", "BasicScreen")

cam = Camera()

test = Node2D((0, 0), 10)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game.quit()
            pygame.quit()
            sys.exit()

    game.update(events)