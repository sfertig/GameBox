import pygame
import numpy as np

from ..basics.Net import Global
from ..basics.ui import load_image

class Tilemap:
    def __init__(self, tilesetImage, tileDim, scale, mapDim, fill=0, layer=4, show=True):
        self.tilemap = load_image(tilesetImage)

        self.tileDim = tileDim
        self.scale = scale
        self.mapDim = mapDim

        self.fill = fill
        self.layer = layer
        self.show = show
        Global.objs[str(self.layer)].append(self)

        #load images and create basic tilemap 
        self.map = np.full(mapDim, fill)
        self.tiles: Dict[int, pygame.Surface] = {}
        tile = 1
        #split image into tiles
        for y in range(mapDim[1]):
            for x in range(mapDim[0]):
                self.tiles[tile] = self.tilemap.subsurface(pygame.Rect(x * tileDim[0], y * tileDim[1], tileDim[0], tileDim[1]))
                tile += 1

    def update(self):
        if self.show: self.draw()

    def draw(self):
        for y in range(self.mapDim[1]):
            for x in range(self.mapDim[0]):
                sx = x * self.tileDim[0] * self.scale
                sy = y * self.tileDim[1] * self.scale
                if sx > Global.screenDim[0] or sx < 0 or sy > Global.screenDim[1] or sy < 0: continue
                image = self.tiles[self.map[y][x]]
                Global.screen.blit(image, (sx, sy))
            

