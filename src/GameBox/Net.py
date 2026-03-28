import pygame
import numpy as np
from .basics.Errors import Errors

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
        #objs in layers 1-5
        self.objs = {"0":[], "1":[], "2":[], "3":[], "4":[], "5":[], "Sig": []}
        self.events = None
        self.cam = None

        self.collision_shapes = {}

        #errors
        self.errors = Errors()   

        #assets
        self.assets = {}     

Global = _global_()
