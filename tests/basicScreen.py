from src.GameBox import *
import pygame

pygame.init()
Keys.init()

width, height = 800, 600

game = Game(width, height)
cam = Cammera()

player = Player((width/2, height/2), (50, 50), (255, 255, 255))

shape = Rect((0, 0), (100, 100), (255, 255, 255))

cam.set_target(shape)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False


    game.update(events)

game.quit()
pygame.quit()
