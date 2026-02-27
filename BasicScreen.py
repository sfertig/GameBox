import pygame
import sys
from src.GameBox import *

width, height = 800, 600
game = Game(width, height, "blue", "BasicScreen")

cam = Camera()

image = Sprite2D((0, 0), "tests/assets/coin.png")
back = Circle((0, 0), 100, "red", 5)
t = Tree(image, [back])


speed = 5

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game.quit()
            pygame.quit()
            sys.exit()

    if Keys.is_held(Keys.d): image.pos.x += speed
    if Keys.is_held(Keys.a): image.pos.x -= speed
    if Keys.is_held(Keys.w): image.pos.y -= speed
    if Keys.is_held(Keys.s): image.pos.y += speed
        

    game.update(events)