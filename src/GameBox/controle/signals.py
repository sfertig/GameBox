import pygame
from ..Net import Global

class Signal:
    def __init__(self, listners, connection, args):
        self.listners = listners
        self.connection = connection
        self.args = args
        Global.objs["Sig"].append(self)

    def update(self):
        if not self.connection:
            return
        for i in self.listners:
            if i:
                self.connection(*self.args)
                break
