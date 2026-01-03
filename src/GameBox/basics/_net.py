import pygame
import numpy as np

class _global_:
    def __init__(self):
        #screen info and win data
        self.screen: pygame.Surface = None
        self.dt: float = 0
        self.screenDim: tuple = None
        self.bgColor: tuple = None
        self.clock: pygame.time.Clock = None

        #basics
        #--game and cam
        self.game: object = None
        self.cam: object = None
        #-collisions
        self.collisions: list[pygame.Rect] = []

        #objects
        self.player = self._player()
        self.tilemap: object = None

    class _player:
        def __init__(self):
            self.pos: tuple = None
            self.player: object = None



Global = _global_()