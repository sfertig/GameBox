import pygame
import numpy as np

from..helpers._input import Keys
from ..basics._net import Global

class _tilemapEditor:
    def __init__(self, tilemap, activation):
        self.tilemap = tilemap
        self.activation = activation
        self.active = False

    def _update(self):
        if  self.active:
            pass
            #editor stuff

        print(self.active)
        #toggle
        if Keys.is_pressed(self.activation): self.active = not self.active


