import pygame
from ..Net import Global
from ..Node2d.Node2D import Node2D

class Camera(Node2D):
    def __init__(self, smooth: float = 1.0):

        Global.cam = self

        super().__init__(pygame.Vector2(0, 0), 0)
        self._del_global_()
        self.smooth = smooth
        
        #movement
        self.target = None
        self.offset = None

    def update(self):
        if self.target and hasattr(self.target, "pos"):
            target_pos = self.target.pos
            self.pos = (self.pos + (target_pos + self.offset - self.pos) * self.smooth)

    def set_target(self, target):
        self.target = target
        self.offset = self.pos - target.pos

