import pygame
import numpy as np

from ..basics._net import Global
from ..basics.utils import clamp, moveTward, zeroOut

class _playerControler:
    def __init__(self, player: object, speed: float = 1.0, gravity: float = 0.0, jump: float = 0.0, maxV: float = 10.0, airRes: float = 0.2):
        self.speed = speed
        self.gravity = gravity
        self.jump = jump
        self.player = player
        self.maxV = maxV
        self.airRes = airRes

    def update(self):
        self.player.vx = clamp(self.player.vx, -self.maxV, self.maxV)
        #self.player.vy = clamp(self.player.vy, -self.maxV, self.maxV)

        self.player.vx = moveTward(self.player.vx, 0, self.airRes)
        self.player.vy = moveTward(self.player.vy, 0, self.airRes)

        self.player.vx = zeroOut(self.player.vx, 0.3)
        self.player.vy = zeroOut(self.player.vy, 0.3)

        if self.player.gravity and not self.player.onGround: self.player.vy += self.gravity




    def move(self, x, y):
        self.player.vx += x * self.speed
        self.player.vy += y * self.speed

    def top_down_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move(-1, 0)
        if keys[pygame.K_d]:
            self.move(1, 0)
        if keys[pygame.K_w]:
            self.move(0, -1)
        if keys[pygame.K_s]:
            self.move(0, 1)

    def platforming_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move(-1, 0)
        if keys[pygame.K_d]:
            self.move(1, 0)
        if keys[pygame.K_SPACE] and self.player.onGround:
            self.player.vy = -self.jump

