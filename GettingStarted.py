import pygame
from random import randint as Ri
from src.GameBox import *


width = 800
height = 600

game = Game(width, height)
screen = game.get_screen()

cam = Cammera()

player = Player(pygame.Vector2(width / 2, height / 2), pygame.Vector2(50, 50), "green")
player.add_physics(0, 0, 0, pygame.Vector2(25, 25), pygame.Vector2(0.75, 0.75))

score = 0
scoreUI = Text(pygame.Vector2(0, 0), 'Score: 0', pygame.font.SysFont("Arial", 32), "white")

#create world bounds
color = "blue"
top = Rect(pygame.Vector2(0, -10), pygame.Vector2(width, 10), color, False)
left = Rect(pygame.Vector2(-10, 0), pygame.Vector2(10, height), color, False)
right = Rect(pygame.Vector2(width, 0), pygame.Vector2(10, height), color, False)
bottom = Rect(pygame.Vector2(0, height), pygame.Vector2(width, 10), color, False)

orbs = []
#fill in list
for _ in range(45) : # this will be the number of orbs
	pos = pygame.Vector2(Ri(0, width), Ri(0, height))
	size = Ri(25, 50)
	color = (Ri(0, 255), Ri(0, 255), Ri(0, 255))
	orbs.append(Rect(pos, pygame.Vector2(size, size), color, collision=False))

#cam.set_target(player)

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
            cam.shake(3, 2, (0, 0))

    player.move.by_WSAD(3.75)
 
    game.update(events, fps=60)

game.quit()
pygame.quit()
