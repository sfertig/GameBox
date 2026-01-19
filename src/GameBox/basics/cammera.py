import pygame
import numpy as np

from ._net import Global

from ..basics.utils import moveTward

class Cammera:
    """
    A class for the camera object.
    """

    def __init__(self, scale: float = 1.0):
        """
        Initialize the camera object.

        Args:
            scale (float): The scale of the camera (default: 1.0)
        """
        self.x = 0
        self.y = 0
        Global.game.objs.append(self)
        Global.cam = self
        self.follow = None
        self.diff = (0, 0)
        self.scale = scale

    def _move(self, x: int, y: int):
        """
        Move the camera by (x, y).

        Args:
            x (int): The x component of the movement
            y (int): The y component of the movement
        """
        self.x += x
        self.y += y

    def update(self):
        """
        Update the camera position based on the follow target.
        """
        return
        if self.follow is not None:
            self.x = (self.follow.x - self.diff[0])
            self.y = (self.follow.y - self.diff[1])

    def set_follow_target(self, target: object):
        """
        Set the follow target for the camera.

        Args:
            target (object): The object to follow
        """
        self.follow = target
        print(target)
        self.diff = (target.x - self.x, target.y - self.y)

    def set_scale(self, scale: float = 1.0):
        """
        Set the scale of the camera.

        Args:
            scale (float): The scale of the camera (default: 1.0)
        """
        self.scale = scale

    def change_scale(self, scale: float = 1.0):
        """
        Change the scale of the camera by the given amount.

        Args:
            scale (float): The amount to change the scale by (default: 1.0)
        """
        self.scale += scale
