import pygame
import sys
from src.GameBox import *

width, height = 800, 600
game = Game(width, height, "blue", "BasicScreen")

cam = Camera()

test = Rect((0, 0), (100, 100), "red", 0, ui=True)
c = Circle((0, 0), 125, "green", 1)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game.quit()
            pygame.quit()
            sys.exit()
        

    game.update(events)