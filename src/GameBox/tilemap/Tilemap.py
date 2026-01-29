import pygame
import numpy as np
import json

from ..basics.Net import Global

from ._collisionDefs import _tileCollisionDefs
from ._editor import _tilemapEditor

class TileMap:
    def __init__(self, tileSet: str, tileDim: tuple, tileScale: float, mapDim: tuple, mapFill: int, saveFile = None, layer=4):
        self.tilesetFile = tileSet
        self.mapFile = saveFile
        self.tileDim = (tileDim[0] * tileScale, tileDim[1] * tileScale)
        self.mapDim = mapDim
        self.tilescale = tileScale
        self.orginDim = tileDim
        self.layer = layer

        self.tilesetNum = 0

        self.editor = None

        Global.objs[str(layer)].append(self)

        self.collisionShapes = _tileCollisionDefs(self.tileDim)

        self.collisionDict = {}

        self.tilePosInImage = {}
        self.posToTile = {}

        #map, tile splitting, ect
        #--create map
        self.map = np.full(self.mapDim, mapFill)
        #--split map into tiles
        self.tiles = {}
        tileset = pygame.image.load(tileSet).convert_alpha()
        self.tileset = tileset
        tile_w, tile_h = tileDim
        tile_id = 1
        tileset_w, tileset_h = tileset.get_size()

        for y in range(0, tileset_h, tile_h):
            for x in range(0, tileset_w, tile_w):
                tile = pygame.Surface(tileDim, pygame.SRCALPHA)
                tile.blit(tileset, (0, 0), (x, y, tile_w, tile_h))
                self.tiles[tile_id] = pygame.transform.scale(tile, self.tileDim)
                self.tilePosInImage[tile_id] = (x, y)
                self.posToTile[(x, y)] = tile_id
                self.tilesetNum += 1
                tile_id += 1

        Global.tilemaps.append(self)

    def load_map_from_json(self, filePath: str):
        with open(filePath, "r") as f:
            data = json.load(f)
        self.__private_loadData(filePath, data)

    def __private_loadData(self, path: str, data: dict):
        self.map = np.array(data["map"])
        self.mapFile = path
        self.collisionDict = data["collisions"]

    def activate_editor(self, activation):
        print(f"editor activated. press {activation} to toggle")
        self.editor = _tilemapEditor(self, activation)

    def update(self):
        self.draw_tiles()
        if self.editor is not None: self.editor._update()
            

    def draw_tiles(self):
        for y in range(self.mapDim[1]):
            for x in range(self.mapDim[0]):
                if self.map[y][x] == 0:
                    continue
                tile = self.tiles[self.map[y][x]]
                mx = ((x * self.tileDim[0]) - Global.cam.pos[0]) * Global.cam.zoom
                my = ((y * self.tileDim[1]) - Global.cam.pos[1]) * Global.cam.zoom
                if mx < -self.tileDim[0] or mx > Global.screenDim[0] or my < -self.tileDim[1] or my > Global.screenDim[1]: continue
                screenTile = pygame.transform.scale(tile, (int(self.tileDim[0] * Global.cam.zoom), int(self.tileDim[1] * Global.cam.zoom)))
                Global.screen.blit(screenTile, (mx, my))

    def _quit(self):
        #save map
        if self.mapFile is not None:
            print('tilemap saved')
            with open(self.mapFile, "w") as f:
                data = {}
                data["map"] = self.map.tolist()
                data["collisions"] = self.collisionDict
                json.dump(data, f)