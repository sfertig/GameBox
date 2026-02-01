import pygame
from random import randint as Ri
from src.GameBox import *


width = 800
height = 600

game = Game(width, height)
screen = game.get_screen()

cam = Cammera()

player = Player((width / 2, height / 2), (50, 50), "green")
player.add_physics(0, 0, 0, (25, 25), (0.75, 0.75))

score = 0
scoreUI = Text((0, 0), 'Score: 0', pygame.font.SysFont("Arial", 32), "white")

#create world bounds
color = "blue"
top = Rect((0, -10), (width, 10), color)
left = Rect((-10, 0), (10, height), color)
right = Rect((width, 0), (10, height), color)
bottom = Rect((0, height), (width, 10), color)

orbs = []
#fill in list
for _ in range(45) : # this will be the number of orbs
	pos = (Ri(0, width), Ri(0, height))
	size = Ri(25, 50)
	color = (Ri(0, 255), Ri(0, 255), Ri(0, 255))
	orbs.append(Rect(pos, (size, size), color, False))


running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    for orb in orbs[:]:
        if orb.collide(player):
            orb.delete()
            orbs.remove(orb)
            score += 1
            scoreUI.change(f"Score: {score}")
            cam.shake(5, 10)

    player.move.by_WSAD(3.75)

    game.update(events, fps=60)

game.quit()
pygame.quit()
