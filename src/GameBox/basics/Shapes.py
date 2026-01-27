import pygame
import numpy as np

from .Net import Global

class shape:
    def __init__(self, pos, dim, color):
        self.pos = pos
        self.dim = dim
        self.color = color

    def move_to(self, x, y):
        self.pos = np.array([x, y])
    def move_by(self, x, y):
        self.pos += np.array([x, y])
    
    def scale(self, factor):
        self.dim *= factor
    def set_dim(self, width, height):
        self.dim = np.array([width, height])
    def change_dim(self, width, height):
        self.dim += np.array([width, height])
    def set_color(self, color):
        self.color = color

class Rect(shape):
    def __init__(self, pos, dim, color):
        super().__init__(np.array(pos), np.array(dim), color)

        Global.objs.append(self)

    def update(self):
        self.draw()

    def draw(self):
        sp = (self.pos - Global.cam.pos) * Global.cam.zoom
        ss = self.dim * Global.cam.zoom
        pygame.draw.rect(Global.screen, self.color, (sp, ss))

