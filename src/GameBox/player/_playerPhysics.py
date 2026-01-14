import pygame
import numpy as np

from ..basics._net import Global
from ..basics.utils import clamp, moveTward, zeroOut
from ..helpers._collisions import CheckCollisions

class _playerPhysics:
    def __init__(self, player, speed: float = 1.0, gravity: float = 0.0, jump: float = 0.0, maxV: float = 10.0, airRes: float = 0.2):
        self.player = player
        self.rect = pygame.Rect(self.player.x, self.player.y, self.player.dim[0], self.player.dim[1])
        
        self.speed = speed
        self.gravity = gravity
        self.jump = jump
        self.player = player
        self.maxV = maxV
        self.airRes = airRes
        self.onGround = False
        self.canJump = False

        self.sample = 10

        self.vx, self.vy = 0, 0

    def update(self):
        self.ckeck_is_on_ground()
        x, y, self.vx, self.vy = CheckCollisions(self.player.x, self.player.y, 
                               self.vx, self.vy, self.player.dim, 
                               self.sample,self.player)
        if (Global.cam.follow) != (self.player):
            self.player.x = x
            self.player.y = y
        elif (Global.cam.follow) == (self.player):
            dx = -(self.player.x - x)
            dy = -(self.player.y - y)
            Global.cam._move(self.vx, self.vy)



    
    def ckeck_is_on_ground(self):
        self.canJump = False
        rect = pygame.Rect(self.player.x, self.player.y + self.player.dim[1], self.player.dim[0], 10)
        for collision in Global.collisions:
            if collision.colliderect(rect):
                self.canJump = True


    def move(self, x, y):
        self.vx += x * self.speed
        self.vy += y * self.speed

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
        #limit velocity
        self.vx = clamp(self.vx, -self.maxV, self.maxV)
        self.vy = clamp(self.vy, -self.maxV, self.maxV)
        self.vx = moveTward(self.vx, 0, self.airRes)
        self.vy = moveTward(self.vy, 0, self.airRes)
        self.vx = zeroOut(self.vx, 0.3)
        self.vy = zeroOut(self.vy, 0.3)

    def platforming_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move(-1, 0)
        if keys[pygame.K_d]:
            self.move(1, 0)
        if keys[pygame.K_w] and self.canJump:
            self.vy -= self.jump
        #limit velocity
        self.vx = clamp(self.vx, -self.maxV, self.maxV)
        self.vx = moveTward(self.vx, 0, self.airRes)
        self.vx = zeroOut(self.vx, 0.3)
        if self.player.gravity and not self.onGround: self.vy += self.gravity
