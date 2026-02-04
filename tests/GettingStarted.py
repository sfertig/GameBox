import pygame
from random import randint as Ri
from src.GameBox import *


width, height = 1040, 540


game = Game(width, height, resizable=True)
screen = game.get_screen()

cam = Cammera()
cam.pos += pygame.Vector2(width/2, height/2)

player = Player(pygame.Vector2(width, height), pygame.Vector2(50, 50), "blue")
player.add_physics(0, 0, 0, pygame.Vector2(100, 100), pygame.Vector2(0.5, 0.5))


score = 0
scoreUI = Text(pygame.Vector2(0, 0), 'player1: 0', pygame.font.SysFont("Arial", 32), "white")

game.generate_bounds(width*2, height*2, "blue", True)

orbs = []
#fill in list
for _ in range(25) : # this will be the number of orbs
	pos = pygame.Vector2(Ri(0, width), Ri(0, height))
	size = Ri(25, 50)
	color = (Ri(0, 255), Ri(0, 255), Ri(0, 255))
	orbs.append(Rect(pos, pygame.Vector2(size, size), color, collision=False))

cam.set_target(player)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE: game.rescale(event)

    for orb in orbs[:]:
        if orb.collide(player):
            orb.delete()
            orbs.remove(orb)
            score += 1
            scoreUI.change(f"player1: {score}")
            cam.shake(3, 2, (0, 0))

    player.move.by_WSAD(7.25) 
    game.update(events, fps=60)

game.quit()
pygame.quit()
