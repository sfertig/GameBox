import pygame
import sys
from src.GameBox import *

width, height = 800, 600
game = Game(width, height, "blue", "BasicScreen")

cam = Camera()

rect = Rect((0, 0), (100, 100), "red", 0)
t = Tree(rect)
c = Circle((0, 0), 125, "green", 1)
t.add_branch(c)
c2 = Circle((0, 0), 110, "blue", 1)
t.add_branch(c2)

speed = 5

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game.quit()
            pygame.quit()
            sys.exit()

    if Keys.is_held(Keys.d): rect.pos.x += speed
    if Keys.is_held(Keys.a): rect.pos.x -= speed
    if Keys.is_held(Keys.w): rect.pos.y -= speed
    if Keys.is_held(Keys.s): rect.pos.y += speed
        

    game.update(events)