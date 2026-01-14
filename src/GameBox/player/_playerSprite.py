import pygame
import numpy as np

from ..basics._net import Global

from ..GameLevel_ui._sprites import Sprite_2d, Animated_Sprite2D

class _playerSprite:
    def __init__(self, player):
        self.player = player

        self.sprite = None

    def update(self, x, y):
        #any changes to follow target
        if Global.cam.follow == self.player and self.sprite is not None:
            self.sprite.__worldPos__ = False
            self.sprite.move_to(self.player.screenPos[0], self.player.screenPos[1])
        elif Global.cam.follow != self.player and self.sprite is not None:
            self.sprite.__worldPos__ = True
            self.sprite.move_to(self.player.x, self.player.y)
        
        if self.sprite is None:
            #rect (x, y) is top left corner
            rect = pygame.Rect((x, y), self.player.dim)
            pygame.draw.rect(Global.screen, self.player.color, rect)
        if type(self.sprite) == Sprite_2d:
            self.sprite.update()
        elif type(self.sprite) == Animated_Sprite2D:
            self.sprite.update()

    def add_sprite_2d(self, image, scale=1.0, dirrection=1):
        self.sprite = Sprite_2d((self.player.x, self.player.y), image, scale, False, dirrection)
        if Global.cam.follow == self.player:
            self.sprite.__worldPos__ = False
        self.sprite.__remove__()

    def add_animated_sprite_2d(self, image, imageDim, tileDim, frames, speed, scale = 1.0, collision = True, dirrection = 1):
        self.sprite = Animated_Sprite2D((self.player.x, self.player.y), image, imageDim, tileDim, frames, speed, scale, collision, dirrection)
        if Global.cam.follow == self.player:
            self.sprite.__worldPos__ = False
        self.sprite.__remove__()

    def remove_sprite(self):
        if self.sprite is not None:
            self.sprite = None
        


