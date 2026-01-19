import pygame
import numpy as np

from ..basics._net import Global

from ..GameLevel_ui._sprites import Sprite_2d

class Image:
    def __init__(self, pos: tuple, image, scale: float = 1.0):
        """
        Initialize an Image UI element.
        
        Args:
            pos: Tuple (x, y) for the image position
            image: Either a file path (str) or pygame.Surface object
            scale: Scale factor for the image (default: 1.0)
        """
        #add to game
        self.image = Sprite_2d(pos, image, scale)
        self.image.__remove__()
        Global.game.ui_objs.append(self)

    def move_by(self, x: int, y: int):
        self.image.move_by(x, y)

    def move_to(self, x: int, y: int):
        self.image.move_to(x, y)
    
    def get_pos(self):
        return self.image.get_pos()

    def rescale(self, scale: float):
        self.image.rescale(scale)

    def update(self):
        Global.screen.blit(self.image.image, self.image.pos)
