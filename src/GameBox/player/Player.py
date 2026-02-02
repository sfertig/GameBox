import pygame

from ..basics.Net import Global
from ._playerPhysics import playerPhysics
from ._playerControler import playerController


class Player:
    def __init__(self, pos, dim, color, show=True, layer=3):
        self.pos = pygame.Vector2(pos)
        self.dim = pygame.Vector2(dim)
        self.vel = pygame.Vector2(0, 0)
        self.color = color

        self.physics = None
        self.move = playerController(self)
        self.show = show

        self.sampleSize = 5
        self.layer = layer
        
        Global.objs[str(layer)].append(self)
        #Global.player = self

    def add_physics(self, speed: float = 7.0, gravity: float = 5.5, jumpForce: float = 10.0, maxV: tuple = (25, 25), friction: tuple = (0.8, 0.8)):
        self.physics = playerPhysics(self, speed, gravity, jumpForce, pygame.Vector2(maxV), pygame.Vector2(friction))
        
    def update(self):
        if self.physics: self.physics.update()
        if self.show: self.draw()

    #--debug func--
    def draw(self):
        sp = (self.pos - Global.cam.pos) * Global.cam.zoom
        ss = self.dim * Global.cam.zoom
        pygame.draw.rect(Global.screen, self.color, [sp, ss])

    def set_sample_size(self, size):
        self.sampleSize = size
