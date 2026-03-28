import pygame
from ..Net import Global

class Signal:
    def __init__(self, listners, connection, args):
        self.listners = listners
        self.connection = connection
        self.args = args
        Global.objs["0"].append(self)

    def connect(self, connection, args=[]):
        self.connection = connection
        if args is not False:
            self.args = args

    def add_args(self, args):
        self.args.append(args)

    def update(self):
        if not self.connection:
            return
        for i in self.listners:
            if i:
                self.connection(*self.args)
                break
