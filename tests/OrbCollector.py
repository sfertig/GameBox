from src.GameBox import *
import pygame
from random import randint as Ri
import numpy as np

pygame.init()
Keys.init()

width, height = 1400, 800

game = Game(width, height)
screen = game.get_screen()
cam = Cammera(smooth=0.2)

#create world bounds
color = "blue"
top = Rect((0, -10), (width, 10), color)
left = Rect((-10, 0), (10, height), color)
right = Rect((width, 0), (10, height), color)
bottom = Rect((0, height), (width, 10), color)

player = Player((width/2, height/2), (50, 50), "green")
player.add_physics(0, 0, 0, (25, 25), (0.75, 0.75))

scoreText = Text((0, 0), "Score: 0", pygame.font.SysFont("Arial", 32), (255, 255, 255))
score = 0

cam.set_target(player)

orbs = [] 
for _ in range(100):
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

    player.move.by_WSAD(3.75)

    for orb in orbs[:]:
        if orb.collide(player):
            orb.delete()
            orbs.remove(orb)
            score+=1
            scoreText.change(f"Score: {score}")

    game.update(events, render=True, fps=60)


game.quit()
pygame.quit()
