"""
GameBox - A beginner-friendly Python 2D game development library.
--------------------------------------------------------------
GameBox makes it easy to build 2D games with graphics, sound, and UI in just a few lines of code.
"""


__version__ = "0.10.1"
__author__ = "Sam Fertig"

#____imports____
from .Game import Game
from .Node2d.Node2D import Node2D
from .basics.Camera import Camera
from .Node2d.Shapes import Rect, Circle
from .controle.input import Keys
from .controle.Tree import Tree
from .Node2d.Sprites import Sprite2D

__all__ = [
    "Game",
    "Node2D",
    "Camera",
    "Rect",
    "Circle",
    "Keys",
    "Tree",
    "Sprite2D"
    ]