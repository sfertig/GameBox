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
        """
        Move the image by (x, y) in world space.
        
        Args:
            x: int, the x component of the movement
            y: int, the y component of the movement
        """
        self.image.move_by(x, y)

    def move_to(self, x: int, y: int):
        """
        Move the image to (x, y) in world space.
        
        Args:
            x: int, the x component of the position
            y: int, the y component of the position
        """
        self.image.move_to(x, y)
    
    def get_pos(self):
        """
        Get the position of the image in world space.
        
        Returns:
            tuple: (x, y) the position of the image
        """
        return self.image.get_pos()

    def rescale(self, scale: float):
        """
        Rescale the image by the given scale.
        
        Args:
            scale: float, the scale factor
        """
        self.image.rescale(scale)

    def update(self):
        """
        Update the image by drawing it on the screen.
        """
        Global.screen.blit(self.image.image, self.image.pos)
