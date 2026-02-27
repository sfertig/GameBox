import pygame
from ..Net import Global
from ..Node2d.Node2D import Node2D

class Camera(Node2D):
    def __init__(self, scale: float = 1.0, smooth: float = 1.0):

        Global.cam = self

        super().__init__(pygame.Vector2(0, 0), 0)
        self._del_global_()
        self.smooth = smooth
        self.zoom = scale
        

        self.shakeinfo = [False, 0, 0, False]  # [active, duration, power, returnPos]

        #movement
        self.target = None
        self.offset = None

    def update(self):
        #addon
        addon = pygame.Vector2(0, 0)
        if self.shakeinfo[0]: 
            addon = pygame.Vector2(Ri(-1, 1), Ri(-1, 1)) * self.shakeinfo[2]
            self.shakeinfo[1]-=1
            if self.shakeinfo[1]<=0: 
                self.shakeinfo[0] = False
                if self.shakeinfo[3]: self.pos = pygame.Vector2(self.shakeinfo[3])

        if self.target and hasattr(self.target, "pos"):
            target_pos = self.target.pos
            self.pos = (self.pos + (target_pos + self.offset - self.pos) * self.smooth)

        self.pos+=addon

    def set_target(self, target):
        self.target = target
        self.offset = self.pos - target.pos

    def shake(self, dur, power, returnPos=False):
        self.shakeinfo = [True, dur, power, returnPos]
