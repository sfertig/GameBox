from src.GameBox import *
import pygame

pygame.init()
Keys.init()

width, height = 800, 600

game = Game(width, height)
cam = Cammera()

shape = Rect((0, 0), (100, 100), (255, 255, 255))

player = Player((width/2, height/2), (50, 50), (255, 255, 255))
player.add_physics(0, 0, 0, (25, 25), (0.8, 0.8))


cam.set_target(player)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    player.move.by_WSAD(5)

    game.update(events)

game.quit()
pygame.quit()
