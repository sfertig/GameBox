"""
GameBox - A beginner-friendly Python 2D game development library.
--------------------------------------------------------------
GameBox makes it easy to build 2D games with graphics, sound, and UI in just a few lines of code.
"""


__version__ = "0.10.0"
__author__ = "Sam Fertig"

#____imports____
from .Game import Game
from .basics.Cammera import Cammera
from .basics.Shapes import Rect, Circle
from .helpers.Input import Keys
from .player.Player import Player
from .tilemap.Tilemap import TileMap
from .basics.utils import clamp
from .basics.ui import Image

__all__ = [
    "Game", 
    "Cammera",
    "Rect",
    "Circle",
    "Keys",
    "Player",
    "TileMap",
    "clamp",
    "Image"
    
    ]



