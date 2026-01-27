import pygame
import numpy as np

from ..basics.Net import Global
from ..helpers.Input import Keys
from ._collisionDefs import _tileCollisionDefs

class _brushPencil():
    def __init__(self):
        self.selectedTile = 1
        self.mode = "paint"

    def update(self, tilemap):
        #get all mouse calculations
        x, y = Keys.mouse_x, Keys.mouse_y
        x += Global.cam.pos[0]
        y += Global.cam.pos[1]
        mx = x // tilemap.tileDim[0] * tilemap.tileDim[0]
        my = y // tilemap.tileDim[1] * tilemap.tileDim[1]

        #get mode
        x, y = Keys.mouse_x, Keys.mouse_y
        if x > tilemap.tileset.get_size()[0] * tilemap.tilescale / 2 or y > tilemap.tileset.get_size()[1] * tilemap.tilescale / 2:
            self.mode = "paint"
        else:
            self.mode = "select"

        #--show tileset
        tile = tilemap.tiles[self.selectedTile]
        image = pygame.transform.scale_by(tilemap.tileset, tilemap.tilescale / 2)
        Global.screen.blit(image, (0, 0))
        #--show outlined sellected tile
        x, y = tilemap.tilePosInImage[self.selectedTile]
        x *= tilemap.tilescale / 2
        y *= tilemap.tilescale / 2
        width = tilemap.orginDim[0] * tilemap.tilescale / 2
        height = tilemap.orginDim[1] * tilemap.tilescale / 2
        outline = pygame.Rect(x, y, width, height)
        pygame.draw.rect(Global.screen, "white", outline, 2)
        #other stuff
        if self.mode == "paint":
            x = mx
            y = my

            x -= Global.cam.pos[0]
            y -= Global.cam.pos[1]
            Global.screen.blit(tile, (x, y))
            #set tile or erase
            if pygame.mouse.get_pressed()[0]:
                #check if mouse is on tilemap
                x, y = mx // tilemap.tileDim[0], my // tilemap.tileDim[1]
                if x >= 0 and x < tilemap.mapDim[0] and y >= 0 and y < tilemap.mapDim[1]:
                    tilemap.map[int(y)][int(x)] = self.selectedTile
            elif pygame.mouse.get_pressed()[2]:
                x, y = mx // tilemap.tileDim[0], my // tilemap.tileDim[1]
                if x >= 0 and x < tilemap.mapDim[0] and y >= 0 and y < tilemap.mapDim[1]:
                    tilemap.map[int(y)][int(x)] = 0
        elif self.mode == "select":
            #paint mouse hovered tile
            x, y = Keys.mouse_x, Keys.mouse_y
            x = (x // width)
            y = (y // height)
            outline = pygame.Rect(x * width, y * width, width, height)
            pygame.draw.rect(Global.screen, "black", outline, 2)
            if pygame.mouse.get_pressed()[0]:
                x *= tilemap.orginDim[0]
                y *= tilemap.orginDim[1]
                self.selectedTile = tilemap.posToTile[(int(x), int(y))]

        #move selection by arrow keys
        x, y = tilemap.tilePosInImage[self.selectedTile]

        width = 16
        height = 16

        if Keys.is_pressed(Keys.left): x -= width
        if Keys.is_pressed(Keys.right): x += width
        if Keys.is_pressed(Keys.up): y -= height
        if Keys.is_pressed(Keys.down): y += height

        if (int(x), int(y)) in tilemap.posToTile:
            self.selectedTile = tilemap.posToTile[(int(x), int(y))]

class _collisionsPencil():
    def __init__(self, tilemap):
        self.selectedTile = 0
        self.shapes = tilemap.collisionShapes.num
        self.mode = "paint"
        size = tilemap.tilescale / 2
        self.size = tilemap.orginDim[0] * size
        self.coll = _tileCollisionDefs((tilemap.orginDim[0] * size, tilemap.orginDim[1] * size))

    def update(self, tilemap):
        x, y = Keys.mouse_x, Keys.mouse_y
        #draw tilesets and background
        Global.screen.fill("darkgrey")
        image = pygame.transform.scale_by(tilemap.tileset, tilemap.tilescale / 2)
        Global.screen.blit(image, (0, 0))
        Global.screen.blit(image, (0, image.get_size()[1]+ 10))
        #draw all collision rects on top tileset
        for tile in range(tilemap.tilesetNum - 1):
            tile+=1
            if str(tile) not in tilemap.collisionDict: continue
            rectshape = tilemap.collisionDict[str(tile)]
            rect = getattr(self.coll, rectshape).copy()
            tx, ty = tilemap.tilePosInImage[int(tile)]
            tx = (tx // tilemap.orginDim[0]) * self.size
            ty = (ty // tilemap.orginDim[1]) * self.size
            rect.x += tx
            rect.y += ty
            pygame.draw.rect(Global.screen, "yellow", rect, 5)
            outline = pygame.Rect(tx, ty, self.size, self.size)
            pygame.draw.rect(Global.screen, "gray", outline, 2)
        #change mode
        if y > image.get_size()[1] * 2 + 50: self.mode = "select"
        else: self.mode = "paint"
        #draw collisions tiles at bottom
        tx, ty = 0, image.get_size()[1] * 2 + 50
        for tile in range(self.shapes-1):
            rect = getattr(self.coll, tilemap.collisionShapes.rects[tile]).copy()
            rect.x += tx
            rect.y += ty
            pygame.draw.rect(Global.screen, "yellow", rect, 5)
            outline = pygame.Rect(tx, ty, self.size, self.size)
            pygame.draw.rect(Global.screen, "gray", outline, 2)
            tx += self.size + self.size / 2
        #paint mode
        if self.mode == "paint":
            #draw tile around mouse
            rect = getattr(self.coll, tilemap.collisionShapes.rects[self.selectedTile]).copy()
            rect.x += x - self.size / 2
            rect.y += y - self.size / 2
            pygame.draw.rect(Global.screen, "yellow", rect, 5)
            outline = pygame.Rect(x, y, self.size, self.size)
            outline.center = (Keys.mouse_x, Keys.mouse_y)
            pygame.draw.rect(Global.screen, "gray", outline, 2)
            #paint collisions
            size = tilemap.orginDim[0]
            if pygame.mouse.get_pressed()[0]:
                x = (x - (x % self.size)) // self.size
                y = (y - (y % self.size)) // self.size
                px = x * size
                py = y * size
                if (int(px), int(py)) in tilemap.posToTile:
                    tilemap.collisionDict[str(tilemap.posToTile[(int(px), int(py))])] = self.coll.rects[self.selectedTile]
            #erase collisions
            if pygame.mouse.get_pressed()[2]:
                x = (x - (x % self.size)) // self.size
                y = (y - (y % self.size)) // self.size
                px = x * size
                py = y * size
                if (int(px), int(py)) in tilemap.posToTile:
                    tilemap.collisionDict[tilemap.posToTile[(int(px), int(py))]] = "none"

        elif self.mode == "select":
            #get tile at mouse
            x = int(x // (self.size + self.size / 2))
            #draw underline
            underline = pygame.Rect((0, 0), (self.size, 5))
            underline.center = (Keys.mouse_x, ty + self.size+5)
            pygame.draw.rect(Global.screen, "black", underline)
            #select tile
            if pygame.mouse.get_pressed()[0] and x < self.shapes-1 and x >= 0:
                self.selectedTile = int(x)
                
