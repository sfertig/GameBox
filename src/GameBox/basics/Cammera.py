import pygame
import numpy as np
from random import randint as Ri

from .Net import Global


class Cammera:
    def __init__(self, scale: float = 1.0, smooth: float = 1.0):

        Global.cam = self

        self.pos = np.array([0.0, 0.0])
        self.smooth = smooth
        self.zoom = scale

        self.shakeinfo = np.array([False, 0, 0])

        #movement
        self.target = None
        self.offset = None

    def update(self):
        #addon
        addon = np.array([0, 0])
        if self.shakeinfo[0]: 
            addon = ((Ri(-1, 1), Ri(-1, 1))) * np.array([self.shakeinfo[2], self.shakeinfo[2]])
            self.shakeinfo[1]-=1
            if self.shakeinfo[1]<=0: 
                self.shakeinfo[0] = False
                if self.shakeinfo[3]: self.pos = np.array(self.shakeinfo[3])

        if self.target and hasattr(self.target, "pos"):
            target_pos = self.target.pos
            self.pos = (self.pos + (target_pos + self.offset - self.pos) * self.smooth)

        self.pos+=addon

    def set_target(self, target):
        self.target = target
        self.offset = self.pos - target.pos

    def shake(self, dur, power, returnPos=False):
        self.shakeinfo = [True, dur, power, returnPos]
