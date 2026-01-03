import pygame
import numpy as np
import json

from ..basics._net import Global

class TileMap:
    def __init__(self, tileSet: str, tileDim: tuple, tileScale: float, mapDim: tuple, mapFill: int, offset: tuple):
        self.tilesetFile = tileSet
        self.tileDim = (tileDim[0] * tileScale, tileDim[1] * tileScale)
        self.mapDim = mapDim
        self.offset = offset
        self.tilescale = tileScale
        self.orginDim = tileDim

        Global.game.objs.append(self)

        #map, tile splitting, ect
        #--create map
        self.map = np.full(self.mapDim, mapFill)
        #--split map into tiles
        self.tiles = {}
        tileset = pygame.image.load(tileSet).convert_alpha()
        tile_w, tile_h = tileDim
        tile_id = 0
        tileset_w, tileset_h = tileset.get_size()

        for y in range(0, tileset_h, tile_h):
            for x in range(0, tileset_w, tile_w):
                tile = pygame.Surface(tileDim, pygame.SRCALPHA)
                tile.blit(tileset, (0, 0), (x, y, tile_w, tile_h))
                self.tiles[tile_id] = pygame.transform.scale(tile, self.tileDim)
                tile_id += 1

        print(f"tiles: {self.tiles}")

    def load_map_from_json(self, filePath: str):
        with open(filePath, "r") as f:
            data = json.load(f)
        self.__private_loadMap(np.array(data))

    def __private_loadMap(self, map: np.array):
        self.map = map

    def update(self):
        self.draw_tiles()

    def draw_tiles(self):
        for y in range(self.mapDim[1]):
            for x in range(self.mapDim[0]):
                tile = self.tiles[self.map[y][x]]
                mx = (x * self.tileDim[0] + self.offset[0]) - Global.cam.x
                my = (y * self.tileDim[1] + self.offset[1]) - Global.cam.y
                Global.screen.blit(tile, (mx, my))
