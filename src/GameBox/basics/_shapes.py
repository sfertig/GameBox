import pygame
import numpy as np

from ..basics._net import Global

class Rect:
    """
    A rectangle shape used for rendering and collision detection.

    Args:
        pos (tuple): The position of the rectangle.
        size (tuple): The size of the rectangle.
        color (tuple, optional): The color of the rectangle. Defaults to (0,0,0).
        collision (bool, optional): Whether the rectangle should be used for collision detection. Defaults to True.
    """

    def __init__(self, pos: tuple, size: tuple, color: tuple = (0, 0, 0), collision: bool = True):
        """
        Initialize the rectangle object.

        Args:
            pos (tuple): The position of the rectangle.
            size (tuple): The size of the rectangle.
            color (tuple, optional): The color of the rectangle. Defaults to (0,0,0).
            collision (bool, optional): Whether the rectangle should be used for collision detection. Defaults to True.
        """
        self.x, self.y = pos
        self.width, self.height = size
        self.color = color
        Global.game.objs.append(self)
        self.collision = collision

    def update(self):
        """
        Update the rectangle object.

        This method updates the position and size of the rectangle based on the camera's position and scale.
        It then renders the rectangle to the screen and adds it to the collision detection list if necessary.
        """
        width = self.width * Global.cam.scale
        height = self.height * Global.cam.scale
        if (Global.cam.follow) != (self):
            x = self.x - Global.cam.x
            y = self.y - Global.cam.y
        elif (Global.cam.follow) == (self):
            x = self.x
            y = self.y

        rect = pygame.Rect(x, y, width, height)
        if self.collision: Global.collisions.append(rect)
        pygame.draw.rect(Global.screen, self.color, rect)

    def move(self, x, y):
        """
        Move the rectangle object.

        Args:
            x (int): The x-coordinate to move the rectangle by.
            y (int): The y-coordinate to move the rectangle by.
        """
        if (Global.cam.follow) != (self):
            self.x += x
            self.y += y
        else:
            Global.cam._move(x, y)
            
    def move_to(self, x, y):
        """
        Move the rectangle object to a specific position.

        Args:
            x (int): The x-coordinate to move the rectangle to.
            y (int): The y-coordinate to move the rectangle to.
        """
        if (Global.cam.follow) != (self):
            self.x = x
            self.y = y
        else:
            Global.cam.x = x
            Global.cam.y = y

    def __remove__(self):
        """
        Remove the rectangle object from the game.

        This method removes the rectangle object from the game's object list.
        """
        Global.game.objs.remove(self)
