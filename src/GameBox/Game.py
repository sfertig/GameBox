import pygame

from .Net import Global

class Game:
    def __init__(self, width: int, height: int, bg_color = "black", title = "Game", resizable: bool = False):
        pygame.init()
        flags = pygame.RESIZABLE if resizable else 0
        self.flags = flags
        self.screen = pygame.Surface((width, height))
        self.width, self.height = width, height
        self.display = pygame.display.set_mode((width, height), flags)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.bg_color = bg_color
        self.title = title
        
        #set global
        Global.screen = self.screen
        Global.screenDim = pygame.Vector2(width, height)
        Global.bg_color = bg_color
        Global.winTitle = title
        Global.clock = self.clock

    def update(self, events, render = True, fps=60):
        Global.collision = []
        #update cam
        if not Global.cam: Global.errors.raiseError("Camera not found", "Game")
        Global.cam.update()

        self.screen.fill(Global.bg_color)
        Global.events = events
        Global.dt = self.clock.tick(fps)/1000.0
        
        if render: 
            self.display.blit(pygame.transform.scale(self.screen, (self.width, self.height)), (0, 0))
            pygame.display.update()

    def get_screen(self): return self.screen


    def rescale(self, event):
        self.width = event.w
        self.height = event.h
        self.display = pygame.display.set_mode((self.width, self.height), self.flags)
    
    def quit(self):
        return
