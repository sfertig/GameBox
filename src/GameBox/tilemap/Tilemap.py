from tkinter import OFF
import pygame
import numpy as np
import json

from ..basics.Net import Global
from ..basics.ui import load_image
from ..basics.utils import show

from ._collisionDefs import _tileCollisionDefs

OFFSETS = [(0, 0), (1, 0), (0,1), (1,1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]

class Tilemap:
    def __init__(self, tilesetImage, tileDim, scale, layer=4, show=True):
        self.tilemap = load_image(tilesetImage)

        self.tileDim = pygame.Vector2(tileDim)
        self.scaleDim = pygame.Vector2(tileDim) * scale
        self.scale = scale

        self.layer = layer
        self.show = show
        Global.objs[str(self.layer)].append(self)
        Global.tilemaps.append(self)

        #load images and create basic tilemap 
        self.map = {}
        self.mapPath = None
        self.collisions = {}
        self.collisionDefs = _tileCollisionDefs(self.scaleDim)
        self.tiles: Dict[int, pygame.Surface] = {}
        self.images: Dict[int, pygame.Surface] = {}
        tile = 0
        #split image into tiles
        for y in range(int(self.tilemap.get_height() // self.tileDim.y)):
            for x in range(int(self.tilemap.get_width() // self.tileDim.x)):
                self.images[tile] = self.tilemap.subsurface(pygame.Rect(x * self.tileDim.x, y * self.tileDim.y, self.tileDim.x, self.tileDim.y))
                self.tiles[tile] = pygame.transform.scale_by(self.images[tile], self.scale)
                tile += 1

    def get_collisions_around(self, pos):
        collisions = []
        for i in OFFSETS:
            n = (int(pos.x+i[0]), int(pos.y+i[1]))
            if not f"{n[0]};{n[1]}" in self.map: continue
            tile = self.map[f"{n[0]};{n[1]}"]
            if str(tile['type']) in self.collisions:
                rect = getattr(self.collisionDefs, self.collisions[str(tile['type'])]).copy()
                rect.x *= self.scaleDim.x
                rect.y *= self.scaleDim.y
                collisions.append(rect)
        return collisions

    def load_from_dict(self, data):
        self._private_load(None, data['map'], data['collisions'])

    def load_from_json(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
        self._private_load(path, data['map'], data['collisions'])

    #private load func
    def _private_load(self, Path, data, collisions):
        self.map = data
        print(collisions)
        self.collisions = collisions
        self.mapPath = Path

    def update(self):
        if self.show: self.draw()

    def draw(self):
        for key in self.map:
            tile = self.map[key]
            image = self.tiles[tile['type']]
            pos = tile['pos']
            x = (pos[0] * self.scaleDim.x) - Global.cam.pos.x
            y = (pos[1] * self.scaleDim.y) - Global.cam.pos.y
            if not show(pygame.Vector2(x, y), self.scaleDim, Global.screenDim): continue
            Global.screen.blit(image, (x, y))
            if str(tile['type']) in self.collisions:
                shape = getattr(self.collisionDefs, self.collisions[str(tile['type'])]).copy()
                shape.x += x
                shape.y += y
                pygame.draw.rect(Global.screen, (255, 0, 0), shape, 1)
            
            

