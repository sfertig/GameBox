import pygame
import numpy as np

from ..basics._net import Global

class TileMap:
    def __init__(self, tileSet: str, tileDim: tuple, mapDim: tuple, mapFill: int, offset: tuple):
        self.tilesetFile = tileSet
        self.tileDim = tileDim
        self.mapDim = mapDim
        self.offset = offset

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
                self.tiles[tile_id] = tile
                tile_id += 1

        print(f"tiles: {self.tiles}")

    def update(self):
        pass
