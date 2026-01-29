from src.GameBox import *
import pygame
from random import randint as Ri
import numpy as np

pygame.init()
Keys.init()

width, height = 1400, 800

game = Game(width, height)
cam = Cammera(smooth=0.2)

player = Player((width/2, height/2), (50, 50), (255, 255, 255))
player.add_physics(0, 0, 0, (25, 25), (0.7, 0.7))


cam.set_target(player)

orbs = [] 
for _ in range(15):
    pos = (Ri(0, width), Ri(0, height))
    radius = Ri(10, 50)
    color = (Ri(0, 255), Ri(0, 255), Ri(0, 255))
    orbs.append(Circle(pos, radius, color))

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    player.move.by_WSAD(3.5)

    for orb in orbs:
        if orb.collide(player):
            orb.delete()
            orbs.remove(orb)

    game.update(events, render=True, fps=60)


game.quit()
pygame.quit()
