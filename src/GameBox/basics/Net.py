import pygame
import numpy as np


class _global_:
    def __init__(self):
        #screen info
        self.screen: pygame.Surface
        self.screenDim: np.array
        self.bg_color: np.array
        self.winTitle: str

        self.player = None

        #time info
        self.clock: pygame.time.Clock
        self.dt: float

        #game info and data
        self.objs = []
        self.collision = []
        self.events = None
        self.cam = None

        #tilemaps
        self.tilemaps = []
        
Global = _global_()

