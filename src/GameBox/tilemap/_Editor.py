import pygame
import numpy as np

from..helpers._input import Keys
from ..basics._net import Global

class _tilemapEditor:
    def __init__(self, tilemap, activation):
        self.tilemap = tilemap
        self.activation = activation
        self.active = False

        self.selectedTile = 10
        self.mx, self.my = Keys.mouse_x, Keys.mouse_y

        self.mode = "paint"

    def _update(self):
        if  self.active:
            #update mouse pos
            self.mx, self.my = Keys.mouse_x, Keys.mouse_y
            self.mx += Global.cam.x
            self.my += Global.cam.y
            self.mx = self.mx // self.tilemap.tileDim[0] * self.tilemap.tileDim[0]
            self.my = self.my // self.tilemap.tileDim[1] * self.tilemap.tileDim[1]
            self.mx -= self.tilemap.offset[0]
            self.my -= self.tilemap.offset[1]

            

            self._mode_()
            self.ui()

        #toggle
        if Keys.is_pressed(self.activation): self.active = not self.active

    def _mode_(self):
        x, y = Keys.mouse_x, Keys.mouse_y
        if x > self.tilemap.tileset.get_size()[0] * self.tilemap.tilescale / 2 or y > self.tilemap.tileset.get_size()[1] * self.tilemap.tilescale / 2:
            self.mode = "paint"
            #more parrimeters will be placed as needed
        else:
            self.mode = "select"

    def ui(self):
        tile = self.tilemap.tiles[self.selectedTile]
        image = pygame.transform.scale_by(self.tilemap.tileset, self.tilemap.tilescale / 2)
        Global.screen.blit(image, (0, 0))
        #show outlined sellected tile
        x, y = self.tilemap.tilePosInImage[self.selectedTile]
        x *= self.tilemap.tilescale / 2
        y *= self.tilemap.tilescale / 2
        width = self.tilemap.orginDim[0] * self.tilemap.tilescale / 2
        height = self.tilemap.orginDim[1] * self.tilemap.tilescale / 2
        print(x, y, width, height)
        outline = pygame.Rect(x, y, width, height)
        pygame.draw.rect(Global.screen, "white", outline, 2)
        #other stuff
        if self.mode == "paint":
            #show selected tile
            #--outline on tileset
            #--show beside mouse
            x = self.mx
            y = self.my
            x -= self.tilemap.offset[0]
            y -= self.tilemap.offset[1]
            x -= Global.cam.x
            y -= Global.cam.y
            Global.screen.blit(tile, (x, y))
        elif self.mode == "select":
            pass
            #paint outline of sellected tile



