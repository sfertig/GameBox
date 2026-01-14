import pygame
import numpy as np

from ..basics._net import Global
from ._Animations import Animation

class Sprite_2d:
    def __init__(self, pos: tuple, image, scale: float = 1.0, collision = True, dirrection: int = 1):
        """
        Initialize a 2D sprite.
        
        Args:
            pos: Tuple (x, y) for the sprite position
            image: Either a file path (str) or pygame.Surface object
            scale: Scale factor for the sprite (default: 1.0)
        """
        #add to game
        Global.game.objs.append(self)
        self.collision = collision
        self.__worldPos__ = True
        self.dir = dirrection

        self.pos = pos
        if type(image) == str:
            self.image = pygame.image.load(image)
        else:
            self.image = image
        
        #scale image
        print(self.image)
        self.image = pygame.transform.scale_by(self.image, scale)
        #flip image
        if self.dir == -1:
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        #world space
        x, y = self.pos
        if self.__worldPos__:
            x = x - Global.cam.x
            y = y - Global.cam.y
        Global.screen.blit(self.image, (x, y))
        if self.collision:
            rect = self.image.get_rect()
            rect.x = x
            rect.y = y
            Global.collisions.append(rect)

    def switch_dirrection(self):
        self.image = pygame.transform.flip(self.image, True, False)
        

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

def split_image(image, tileDim, startPos):
    if type(image) == str:
        image = pygame.image.load(image)
    else:
        image = image

    #return image split
    x = startPos[0] * tileDim[0]
    y = startPos[1] * tileDim[1]
    return image.subsurface((x, y, tileDim[0], tileDim[1]))
    