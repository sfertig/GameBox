import pygame

from ..Net import Global

class Node2D:
    def __init__(self, pos, layer, ui=False, show=True):
        self.pos = pygame.Vector2(pos)
        self.layer = layer
        self.ui = ui
        self.show = show

        try:
            Global.objs[str(layer)].append(self)
        except:
            Global.errors.raiseError("Layer not found: " + str(layer), "Node2D")

    def _del_global_(self):
        try:
            Global.objs[str(self.layer)].remove(self)
        except:
            Global.errors.raiseError("Layer not found: " + str(self.layer), "Node2D")
