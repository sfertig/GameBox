import pygame
import numpy as np

from ..helpers.Input import Keys

class playerController:
    def __init__(self, player):
        self.p = player

    def by_WSAD(self, speed):
        if Keys.is_held(Keys.w): self.p.vel[1] -= speed
        if Keys.is_held(Keys.s): self.p.vel[1] += speed
        if Keys.is_held(Keys.a): self.p.vel[0] -= speed
        if Keys.is_held(Keys.d): self.p.vel[0] += speed

    def by_arrows(self, speed):
        if Keys.is_held(Keys.up): self.p.vel[1] -= speed
        if Keys.is_held(Keys.down): self.p.vel[1] += speed
        if Keys.is_held(Keys.left): self.p.vel[0] -= speed
        if Keys.is_held(Keys.right): self.p.vel[0] += speed

    def platformor_by_WSAD(self, speed):
        if Keys.is_pressed(Keys.w): self.p.vel[1] -= speed
        if Keys.is_held(Keys.a): self.p.vel[0] -= speed
        if Keys.is_held(Keys.d): self.p.vel[0] += speed

    def platformor_by_arrows(self, speed):
        if Keys.is_pressed(Keys.up): self.p.vel[1] -= speed
        if Keys.is_held(Keys.left): self.p.vel[0] -= speed
        if Keys.is_held(Keys.right): self.p.vel[0] += speed
