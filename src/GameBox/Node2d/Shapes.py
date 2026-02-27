import pygame
from .Node2D import Node2D
from ..Net import Global

class Rect(Node2D):
    def __init__(self, pos, size, color, layer, show=True, ui=False):
        super().__init__(pos, layer, ui, show)
        self._del_global_()
        try:
            Global.objs[str(layer)].append(self)
        except:
            Global.errors.raiseError("Layer not found: " + str(layer), "Rect")

        self.size = size
        self.color = color
        self.rect = pygame.Rect(pos, size)

    def update(self):
        if self.show: self.render()

    def render(self):
        sp = self.pos - Global.cam.pos
        pygame.draw.rect(Global.screen, self.color, (sp, self.size))
