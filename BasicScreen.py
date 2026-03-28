import pygame
import sys
import os
from src.GameBox import *

width, height = 800, 600
game = Game(width, height, "blue", "BasicScreen")
g = game._get_global_()

cam = Camera()


shape = Area2D((0, 0), col)

shape2 = CollisionShape_Rect((width/2, height/2), (50, 50))
rect = Rect((width/2, height/2), (50, 50), "red")


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

    if shape.areaEntered: print("area entered")
    if shape.areaExited: print("area exited")
        

    game.update(events, fps=60)