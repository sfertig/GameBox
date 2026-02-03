import pygame
import numpy as np

from ..basics.Net import Global
from ..basics.ui import load_image

class Tilemap:
    def __init__(self, tilesetImage, tileDim, scale, layer=4, show=True):
        self.tilemap = load_image(tilesetImage)

        self.tileDim = pygame.Vector2(tileDim)
        self.scaleDim = pygame.Vector2(tileDim) * scale
        self.scale = scale
        self.mapDim = mapDim

        self.fill = fill
        self.layer = layer
        self.show = show
        Global.objs[str(self.layer)].append(self)

        #load images and create basic tilemap 
        self.map = {}
        self.tiles: Dict[int, pygame.Surface] = {}
        self.images: Dict[int, pygame.Surface] = {}
        tile = 1
        #split image into tiles
        for y in range(mapDim[1]):
            for x in range(mapDim[0]):
                try:
                    self.images[tile] = self.tilemap.subsurface(pygame.Rect(x * self.tileDim.x, y * self.tileDim.y, self.tileDim.x, self.tileDim.y))
                    self.tiles[tile] = pygame.transform.scale_by(self.images[tile], self.scale)
                except:
                    pass
                tile += 1

    def update(self):
        if self.show: self.draw()

    def draw(self):
        for key in self.map:
            tile = self.map[key]
            image = self.tiles[tile['type']]
            pos = tile['pos']
            
            

