import pygame
import numpy as np

from ._net import Global

from ..basics.utils import moveTward

class Cammera:
    def __init__(self, scale: float = 1.0):
        self.x = 0
        self.y = 0
        Global.game.objs.append(self)
        Global.cam = self
        self.follow = None
        self.diff = (0, 0)
        self.scale = scale

    def update(self):
        return
        if self.follow is not None:
            self.x = (self.follow.x - self.diff[0])
            self.y = (self.follow.y - self.diff[1])

    def set_follow_target(self, target: object):
        self.follow = target
        print(target)
        self.diff = (target.x - self.x, target.y - self.y)

    def set_scale(self, scale: float = 1.0):
        self.scale = scale
    def change_scale(self, scale: float = 1.0):
        self.scale += scale
