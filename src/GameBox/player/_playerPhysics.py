import pygame

from ..basics.Net import Global
from ..basics.utils import clamp, zeroOut

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
        self.player.vel.x = clamp(self.player.vel.x, -self.maxV.x, self.maxV.x)
        self.player.vel.y = clamp(self.player.vel.y, -self.maxV.y, self.maxV.y)
        
        #apply gravity
        self.player.vel.y += self.gravity
        
        #apply friction
        self.player.vel.x *= self.friction.x
        self.player.vel.y *= self.friction.y
        
        #zero out very small velocities to prevent drift
        self.player.vel.x = zeroOut(self.player.vel.x, 0.01)
        self.player.vel.y = zeroOut(self.player.vel.y, 0.01)
        
        #update position
        self.player.pos, self.player.vel = CollisionLogic(self.player.vel, self.player.pos, self.player.dim, self.player.sampleSize)
               
