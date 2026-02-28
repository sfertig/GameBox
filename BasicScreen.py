import pygame
import sys
import os
from src.GameBox import *

width, height = 800, 600
game = Game(width, height, "blue", "BasicScreen")

cam = Camera()

image = Sprite2D((0, 0), "tests/assets/coin.png")
back = Circle((0, 0), 100, "red", 4)
image.rescale(2.0)
t = Tree(image, [back, Circle((0, 0), 125, "green", 5)])


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
    if Keys.is_pressed(Keys.r): image.rescale(image.scale*2.0)
    if Keys.is_pressed(Keys.e): image.rescale(image.scale/2.0)
        

    game.update(events)