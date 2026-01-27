import pygame
import numpy as np


class _global_:
    def __init__(self):
        #screen info
        self.screen: pygame.Surface
        self.screenDim: np.array
        self.bg_color: np.array
        self.winTitle: str

        #time info
        self.clock: pygame.time.Clock
        self.dt: float

        #game info and data
        self.objs = []
        self.events = None
        
Global = _global_()

