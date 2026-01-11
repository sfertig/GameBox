import pygame
import numpy as np

from ..basics._net import Global
from ..helpers._input import Keys

class _brushPencil():
    def __init__(self):
        self.selectedTile = 1

    def update(self, tilemap):
        #get all mouse calculations
        x, y = Keys.mouse_x, Keys.mouse_y
        x += Global.cam.x
        y += Global.cam.y
        x = x // tilemap.tileDim[0] * tilemap.tileDim[0]
        y = y // tilemap.tileDim[1] * tilemap.tileDim[1]

