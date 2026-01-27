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

__all__ = [
    "Game", 
    "Cammera"
    
    ]



