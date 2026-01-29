import pygame
import numpy as np

from .Net import Global

class _image:
    def __init__(self, pos, image, scale):
        self.pos = np.array(pos)
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.scale = scale

    def move_to(self, pos):
        self.pos = np.array(pos)
    def move_by(self, x, y):
        self.pos[0]+=x
        self.pos[1]+=y

    def change_scale(self, amount):
        self.scale += amount
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale)))

class Image(_image):
    def __init__(self, pos, image, scale, layer=0):
        super().__init__(pos, image, scale)
        self.layer = layer
        Global.objs[self.layer].append(self)

    def update(self):
        self.draw()
        
    def draw(self):
        if Global.cam.zoom != 0:
            image = pygame.transform.scale(self.image, (int(self.image.get_width() * Global.cam.zoom), int(self.image.get_height() * Global.cam.zoom)))
            Global.screen.blit(image, self.pos - Global.cam.pos)
        else:
            Global.screen.blit(self.image, self.pos)
