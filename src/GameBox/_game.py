import pygame
import numpy as np

from .basics._net import Global
from .player._player import Player

class Game:
    def __init__(self, width, height, bg_color, WinTitle="GameBox"):
        """
        Initialize the Game object.

        Parameters:
        width (int): The width of the game window.
        height (int): The height of the game window.
        bg_color (tuple): The background color of the game window.
        WinTitle (str): The title of the game window.

        Returns:
        None
        """
        Global.screenDim = (width, height)
        Global.screen = pygame.display.set_mode(Global.screenDim)
        pygame.display.set_caption(WinTitle)
        Global.bgColor = bg_color
        Global.clock = pygame.time.Clock()
        Global.game = self
        self.objs = []


    def update(self, frame_rate=60):
        Global.collisions.clear()
        Global.dt = Global.clock.tick(frame_rate) / 1000.0
        Global.screen.fill(Global.bgColor)
        player = None
        for obj in self.objs:
            if type(obj) == Player: player = obj
            else: obj.update()
        if player != None: player.update()
        pygame.display.update()

    def get_screen(self):
        return Global.screen
    
    def quit(self):
        #will save files later
        for obj in self.objs:
            if hasattr(obj, "_quit") and callable(obj._quit):
                obj._quit()


