"""
GameBox - A beginner-friendly Python 2D game development library.
--------------------------------------------------------------
GameBox makes it easy to build 2D games with graphics, sound, and UI in just a few lines of code.
"""


__version__ = "0.0.3"
__author__ = "Sam Fertig"

#____imports____
from ._game import Game
from .basics.cammera import Cammera
from .basics._shapes import Rect
from .player._player import Player
from .basics.utils import clamp, moveTward, zeroOut
from .tilemap._tilemap import TileMap
from.helpers._input import Keys


__all__ = [
    "Game",
    "Cammera",
    "Rect",
    "Player",
    "clamp",
    "moveTward",
    "zeroOut",
    "TileMap",
    "Keys",
]

