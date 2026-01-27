from src.GameBox import *
import pygame

pygame.init()
Keys.init()

width, height = 800, 600

game = Game(width, height)
cam = Cammera()

shape2 = Rect((100, 100), (100, 100), (255, 0, 0))

shape = Rect((0, 0), (100, 100), (255, 255, 255))
speed = 5

cam.set_target(shape)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    #move rect
    if Keys.is_held(Keys.a):
        shape.move_by(-speed, 0)
    if Keys.is_held(Keys.d):
        shape.move_by(speed, 0)
    if Keys.is_held(Keys.w):
        shape.move_by(0, -speed)
    if Keys.is_held(Keys.s):
        shape.move_by(0, speed)

    game.update(events)

game.quit()
pygame.quit()
