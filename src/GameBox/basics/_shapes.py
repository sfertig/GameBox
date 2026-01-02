import pygame
import numpy as np

from ..basics._net import Global

class Rect:
    def __init__(self, pos: tuple, size: tuple, color: tuple = (0, 0, 0), collision: bool = True):
        self.x, self.y = pos
        self.width, self.height = size
        self.color = color
        Global.game.objs.append(self)
        self.collision = collision

    def update(self):
        width = self.width * Global.cam.scale
        height = self.height * Global.cam.scale
        if (Global.cam.follow) != (self):
            x = self.x - Global.cam.x
            y = self.y - Global.cam.y
        elif (Global.cam.follow) == (self):
            x = self.x
            y = self.y

        rect = pygame.Rect(x, y, width ,height)
        if self.collision: Global.collisions.append(rect)
        pygame.draw.rect(Global.screen, self.color, rect)

    def move(self, x, y):
        if (Global.cam.follow) != (self):
            self.x += x
            self.y += y
        else:
            Global.cam.move(x, y)
