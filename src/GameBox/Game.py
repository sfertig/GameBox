import pygame
import numpy as np

from .basics.Net import Global

class Game:
    def __init__(self, width: int, height: int, bg_color = "black", title = "Game", resizable: bool = False):
        pygame.init()
        flags = pygame.RESIZABLE if resizable else 0
        self.screen = pygame.display.set_mode((width, height), flags)
        self.clock = pygame.time.Clock()
        self.running = True
        self.bg_color = bg_color
        self.title = title
        
        #set global
        Global.screen = self.screen
        Global.screenDim = np.array([width, height])
        Global.bg_color = bg_color
        Global.winTitle = title
        Global.clock = self.clock

    def update(self, events, render = True, fps=60):
        Global.collision = []
        #update cam
        Global.cam.update()

        self.screen.fill(Global.bg_color)
        Global.events = events
        Global.dt = self.clock.tick(fps)/1000.0
        
        #collect all collision rects first
        for key in range(5, -1, -1):
            for obj in Global.objs[str(key)]:
                if hasattr(obj, '_addCollision'):
                    obj._addCollision()
        
        #then update all objects
        for key in range(5, -1, -1):
            for obj in Global.objs[str(key)]:
                if hasattr(obj, 'update'):
                    obj.update()
        
        if render: pygame.display.update()

    def get_screen(self): return self.screen
    
    def quit(self):
        for tilemap in Global.tilemaps:
            tilemap._quit()

