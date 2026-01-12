import pygame
import numpy as np

from ..basics._net import Global

from ..player._playerPhysics import _playerPhysics
from ..GameLevel_ui._sprites import Sprite_2d, AnimatedSprite_2d, AnimationPlayer

class Player:
    def __init__(self, pos: tuple, size: tuple, color: tuple = (0, 0, 0), gravity: bool = False):
        self.x, self.y = pos
        self.screenPos = pos
        self.dim = size
        self.color = color

        self.gravity = gravity
        
        Global.game.objs.append(self)
        Global.player.pos = pos
        Global.player.player = self

        self.sprite = None


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
        if self.sprite is not None:
            self.sprite.update()

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

    def add_sprit2D(self, image, scale: float = 1.0):
        """
        Adds a 2D sprite to the player.
        """
        self.sprite = Sprite_2d(self.screenPos,image, scale, False)
        self.sprite.__remove__()
        self.sprite.__worldPos__ = False

    def add_animated_sprit2D(self, image, tileDim, startPos, frames, dur):
        """
        Adds an animated 2D sprite to the player.
        """
        self.sprite = AnimatedSprite_2d(self.screenPos,image, tileDim, startPos, frames, dur, False)
        self.sprite.__remove__()
        self.sprite.__worldPos__ = False

    def remove_sprite(self):
        """
        Removes the sprite from the player.
        """
        self.sprite = None

    def add_animation_player(self):
        """
        Adds an animation player to the player.
        """
        self.sprite = AnimationPlayer(self.screenPos)
        self.sprite.__remove__()
        self.sprite.__worldPos__ = False

    def add_animation(self, name: str, animation: AnimationPlayer):
        """
        Adds an animation to the animation player.
        """
        self.sprite.add_animation(name, animation)

    def set_dim_as_sprite(self):
        if self.sprite is not None:
            dim = self.sprite.image.get_size()
            self.dim = dim
            self.width, self.height = dim


