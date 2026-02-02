from src.GameBox import *
import pygame

width, height = 1000, 800

game = Game(width, height)
screen = game.get_screen()

cam = Cammera()

player = Player((width / 2, height / 2), (50, 50), "green")
player.add_physics(0, 0, 0, (25, 25), (0.75, 0.75))
cam.set_target(player)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    player.move.by_WSAD(3.8)

    game.update(events)

game.quit()
pygame.quit()
