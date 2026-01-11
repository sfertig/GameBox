import pygame
import numpy as np

from ..basics._net import Global
from ..helpers._input import Keys

class _brushPencil():
    def __init__(self):
        self.selectedTile = 1
        self.mode = "paint"

    def update(self, tilemap):
        #get all mouse calculations
        x, y = Keys.mouse_x, Keys.mouse_y
        x += Global.cam.x
        y += Global.cam.y
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

            x -= Global.cam.x
            y -= Global.cam.y
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

