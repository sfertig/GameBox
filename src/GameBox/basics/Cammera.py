import pygame
import numpy as np

from .Net import Global


class Cammera:
    def __init__(self, scale: float = 1.0, smooth: float = 1.0):

        Global.cam = self

        self.pos = np.array([0.0, 0.0])
        self.smooth = smooth
        self.zoom = scale

        #movement
        self.target = None
        self.offset = None

    def update(self):
        if self.target and hasattr(self.target, "pos"):
            target_pos = self.target.pos
            if self.offset is None:
                self.offset = self.pos - target_pos
            self.pos = self.pos + (target_pos + self.offset - self.pos) * self.smooth

    def set_target(self, target):
        self.target = target
        self.offset = self.pos - target.pos
