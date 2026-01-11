import pygame
import numpy as np

from ..basics._net import Global

class Image:
    def __init__(self, pos: tuple, image, scale: float = 1.0):
        #add to game
        Global.game.ui_objs.append(self)

        self.pos = pos
        if type(image) == str:
            self.image = pygame.transform.scale_by(pygame.image.load(image), scale)
        else:
            self.image = pygame.transform.scale_by(image, scale)

    def update(self):
        Global.screen.blit(self.image, self.pos)
