import pygame
import numpy as np

from ..basics._net import Global

class Sprite_2d:
    def __init__(self, pos: tuple, image, scale: float = 1.0):
        """
        Initialize a 2D sprite.
        
        Args:
            pos: Tuple (x, y) for the sprite position
            image: Either a file path (str) or pygame.Surface object
            scale: Scale factor for the sprite (default: 1.0)
        """
        #add to game
        Global.game.objs.append(self)

        self.pos = pos
        if type(image) == str:
            if image not in Global.images:
                self.image = pygame.transform.scale_by(pygame.image.load(image), scale)
            else:
                self.image = Global.images[image].copy()
        else:
            self.image = pygame.transform.scale_by(image, scale)
        
        #cache the image
        Global.images[image] = self.image

    def update(self):
        Global.screen.blit(self.image, self.pos)

    def move_by(self, x: int, y: int):
        self.pos = (self.pos[0] + x, self.pos[1] + y)

    def move_to(self, x: int, y: int):
        self.pos = (x, y)

    def get_pos(self):
        return self.pos

    def rescale(self, scale: float):
        self.image = pygame.transform.scale_by(self.image, scale)

    def __remove__(self):
        Global.game.objs.remove(self)

