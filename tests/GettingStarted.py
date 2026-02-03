import pygame
from random import randint as Ri
from src.GameBox import *


width = 800
height = 600

game = Game(width, height, resizable=False)
screen = game.get_screen()

cam = Cammera()

player1 = Player(pygame.Vector2(width / 2, height / 2), pygame.Vector2(50, 50), "blue")
player1.add_physics(0, 0, 0, pygame.Vector2(100, 100), pygame.Vector2(0.5, 0.5))

player2 = player1.copy()
player2.color = 'red'

score1 = 0
score2 = 0
scoreUI = Text(pygame.Vector2(0, 0), 'player1: 0  |  player2: 0', pygame.font.SysFont("Arial", 32), "white")

game.generate_bounds(width, height)

orbs = []
#fill in list
for _ in range(200) : # this will be the number of orbs
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
        #if event.type == pygame.VIDEORESIZE: game.rescale(event)

    for orb in orbs[:]:
        if orb.collide(player1):
            orb.delete()
            orbs.remove(orb)
            score1 += 1
            scoreUI.change(f"player1: {score1}  |  player2: {score2}")
            #cam.shake(3, 2, (0, 0))
        elif orb.collide(player2):
            orb.delete()
            orbs.remove(orb)
            score2 += 1
            scoreUI.change(f"player1: {score1}  |  player2: {score2}")
            #cam.shake(3, 2, (0, 0))

    player1.move.by_WSAD(3.75)
    player2.move.by_arrows(3.75)
 
    game.update(events, fps=60)

game.quit()
pygame.quit()
