import pygame


NAME = "GameBox"

class Error:
    def __init__(self, message, dest):
        self.message = message
        self.dest = dest
    def __repr__(self):
        return f"{NAME}: {self.dest}: {self.message}"

def raiseError(message, dest):
    raise Error(message, dest)

class Errors:
    def __init__(self):
        self.raiseError = raiseError
    
