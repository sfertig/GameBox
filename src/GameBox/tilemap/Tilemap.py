import pygame
import numpy as np
import json

from ..basics.Net import Global
from ..basics.ui import load_image

class Tilemap:
    def __init__(self, tilesetImage, tileDim, scale, layer=4, show=True):
        self.tilemap = load_image(tilesetImage)

        self.tileDim = pygame.Vector2(tileDim)
        self.scaleDim = pygame.Vector2(tileDim) * scale
        self.scale = scale

        self.layer = layer
        self.show = show
        Global.objs[str(self.layer)].append(self)

        #load images and create basic tilemap 
        self.map = {}
        self.mapPath = None
        self.tiles: Dict[int, pygame.Surface] = {}
        self.images: Dict[int, pygame.Surface] = {}
        tile = 1
        #split image into tiles
        for y in range(int(self.tilemap.get_height() // self.tileDim.y)):
            for x in range(int(self.tilemap.get_width() // self.tileDim.x)):
                try:
                    self.images[tile] = self.tilemap.subsurface(pygame.Rect(x * self.tileDim.x, y * self.tileDim.y, self.tileDim.x, self.tileDim.y))
                    self.tiles[tile] = pygame.transform.scale_by(self.images[tile], self.scale)
                except:
                    pass
                tile += 1

    def load_from_dict(self, data):
        self._private_load(None, data)

    def load_from_json(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
        self._private_load(path, data)

    #private load func
    def _private_load(self, Path, data):
        self.map = data
        self.mapPath = Path

    def update(self):
        if self.show: self.draw()

    def draw(self):
        for key in self.map:
            tile = self.map[key]
            image = self.tiles[tile['type']]
            pos = tile['pos']
            x = (pos[0] * self.scaleDim.x) + Global.cam.pos.x
            y = (pos[1] * self.scaleDim.y) + Global.cam.pos.y
            if x < Global.cam.pos.x - Global.screenDim.x or x > Global.cam.pos.x + Global.screenDim.x or y < Global.cam.pos.y - Global.screenDim.y or y > Global.cam.pos.y + Global.screenDim.y: continue
            Global.screen.blit(image, (x, y))
            
            

