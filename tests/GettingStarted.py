import pygame
from src.GameBox import *

width, height = 800, 600

game = Game(width, height, "blue", "First Game!")
screen = game.get_screen()

cam = Cammera()

Keys.init()

player = Player((width / 2, height / 2), (64, 64), "green", False)
player.add_physics(1.0, 3.0, 16, 7.0, 0.5)

image = split_image("tests/Player.png", (32, 32), (0, 0))
print(image)
player.sprite.add_animated_sprite_2d("tests/Player.png", (5, 1), (32, 32), 5, 0.075, 2.0, True, 1)
player.sprite.sprite.switch_dirrection()

rect = Rect((width / 2, height / 4), (64, 64), "red", True)


#cam.set_follow_target(player)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    
    player.top_down_movement()
    game.update(events, 60)
    
game.quit()
pygame.quit()
