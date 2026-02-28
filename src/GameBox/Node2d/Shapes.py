import pygame
from .Node2D import Node2D
from ..Net import Global
from ..basics.utils import on_screen

#region Rect
class Rect(Node2D):
    def __init__(self, pos, size, color, layer, show=True, ui=False):
        super().__init__(pos, layer, ui, show)
        self._del_global_()
        try:
            Global.objs[str(layer)].append(self)
        except:
            Global.errors.raiseError("Layer not found: " + str(layer), "Rect")

        self.size = pygame.Vector2(size)
        self.color = color

    def update(self):
        if self.show: self.render()

    def render(self):
        if not self.ui: sp = self.pos - Global.cam.pos
        else: sp = self.pos
        if on_screen(sp):
            pygame.draw.rect(Global.screen, self.color, ((sp-self.size/2), self.size))
#endregion

#region Circle
class Circle(Node2D):
    def __init__(self, pos, radius, color, layer, show=True, ui=False):
        super().__init__(pos, layer, ui, show)
        self._del_global_()
        try:
            Global.objs[str(layer)].append(self)
        except:
            Global.errors.raiseError("Layer not found: " + str(layer), "Rect")

        self.radius = radius
        self.color = color

    def update(self):
        if self.show: self.render()

    def render(self):
        if not self.ui: sp = self.pos - Global.cam.pos
        else: sp = self.pos
        if on_screen(sp):
            pygame.draw.circle(Global.screen, self.color, sp, self.radius)
#endregion
