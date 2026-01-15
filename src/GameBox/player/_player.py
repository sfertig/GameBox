import pygame
import numpy as np

from ..basics._net import Global

from ..player._playerPhysics import _playerPhysics
from ..player._playerSprite import _playerSprite

from ..GameLevel_ui._sprites import Sprite_2d

class Player:
    def __init__(self, pos: tuple, size: tuple, color: tuple = (0, 0, 0), gravity: bool = False):
        self.x, self.y = pos
        self.screenPos = pos
        self.dim = size
        self.color = color
        self.width, self.height = size

        self.gravity = gravity

        self.state = ""
        
        Global.game.objs.append(self)
        Global.player.pos = pos
        Global.player.player = self

        self.sprite = _playerSprite(self)


    def add_physics(self, speed: float = 1.0, gravity: float = 0.0, jump: float = 10.0, maxV: float = 10.0, airRes: float = 0.2):
        self.physics = _playerPhysics(self, speed, gravity, jump, maxV, airRes)

    def update(self):
        self.physics.update()
        #ui

        if (Global.cam.follow) != (self):
            x = self.x - Global.cam.x
            y = self.y - Global.cam.y
        elif (Global.cam.follow) == (self):
            x = self.x
            y = self.y
        velocity = (self.physics.vx, self.physics.vy)
        self.sprite.update(x, y, velocity)

    #movement
    def top_down_movement(self):
        self.physics.top_down_movement()

    def platforming_movement(self):
        self.physics.platforming_movement()

    def set_tilemap_sample(self, sample: int = 10):
        """
        Sets the sample size for player physics collisions. 
        Is the radius of tiles that will be used to get tilemap collisions around player. Note: 
        The larger the sample size the longer it may take to calculate collisions per frame.
        """
        self.physics.sample = sample


