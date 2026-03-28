import pygame
import sys
import os
from src.GameBox import *

width, height = 800, 600
game = Game(width, height, "blue", "BasicScreen")
g = game._get_global_()

cam = Camera()

def entered(): print("entered")
def exited(): print("exited")


image = Area2D((0, 0), CollisionShape_Rect((0, 0), (100, 100)))
image_texture = Rect((0, 0), (100, 100), "red")
t = Tree(image, [image_texture])

image.areaEnteredSignal.connect(entered)
image.areaExitedSignal.connect(exited)

shape2 = Area2D((width/2, height/2), CollisionShape_Rect((0, 0), (50, 50)))
rect = Rect((width/2, height/2), (50, 50), "red")


speed = 5

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            print("sys exit")
            game.quit()
            pygame.quit()
            sys.exit()

    if Keys.is_held(Keys.d): image.pos.x += speed
    if Keys.is_held(Keys.a): image.pos.x -= speed
    if Keys.is_held(Keys.w): image.pos.y -= speed
    if Keys.is_held(Keys.s): image.pos.y += speed
        

    game.update(events, fps=60)