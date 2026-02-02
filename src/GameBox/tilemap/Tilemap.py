import pygame
import numpy as np

from ..basics.Net import Global
from ..basics.ui import load_image

class Tilemap:
    def __init__(self, tilesetImage, tileDim, scale, mapDim, fill=0, layer=4, show=True):
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
        self.map = np.full(mapDim, fill)
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
        for y in range(self.mapDim[1]):
            for x in range(self.mapDim[0]):
                if self.map[y][x] == 0:
                    continue
                tile = self.tiles[self.map[y][x]]
                mx = ((x * self.scaleDim.x) - Global.cam.pos.x)
                my = ((y * self.scaleDim.y) - Global.cam.pos.y)
                if mx < -self.scaleDim.x or mx > Global.screenDim.x or my < -self.scaleDim.y or my > Global.screenDim.y: continue
                Global.screen.blit(tile, (mx, my))
            

