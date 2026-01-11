import pygame
import numpy as np

from..helpers._input import Keys
from ..basics._net import Global
from ._collisionDef import _tileCollisionDefs

from._editorBrushes import _brushPencil, _collisionsPencil

class _tilemapEditor:
    def __init__(self, tilemap, activation):
        self.tilemap = tilemap
        self.activation = activation
        self.active = False

        self.mode = _brushPencil()

        self.changes = {
            "pencil": Keys.b,
            "collisions": Keys.c
            
        }

    def _update(self):
        if  self.active:
            self.change_mode()
            #editor stuff
            self.mode.update(self.tilemap)
        #toggle
        if Keys.is_pressed(self.activation): self.active = not self.active

    def change_mode(self):
        #key presses
        if Keys.is_pressed(self.changes["pencil"]): self.mode = _brushPencil()
        elif Keys.is_pressed(self.changes["collisions"]): self.mode = _collisionsPencil(self.tilemap)
    