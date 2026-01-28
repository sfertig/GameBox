import pygame
import numpy as np

from ..basics.Net import Global
from ..basics.utils import clamp

from ..helpers._collisions import CollisionLogic

class playerPhysics:
    def __init__(self, player, speed, gravity, jumpForce, maxV, friction):
        self.player = player
        self.speed = speed
        self.gravity = gravity
        self.jumpForce = jumpForce
        self.maxV = maxV
        self.friction = friction
        
    def update(self):
        #clamp velocities
        self.player.vel[0] = clamp(self.player.vel[0], -self.maxV[0], self.maxV[0])
        self.player.vel[1] = clamp(self.player.vel[1], -self.maxV[1], self.maxV[1])
        
        #apply gravity
        self.player.vel[1] += self.gravity
        
        #apply friction
        self.player.vel *= self.friction
        
        #update position
        self.player.pos, self.player.vel = CollisionLogic(self.player.vel, self.player.pos, self.player.dim, self.player.sampleSize)
               
