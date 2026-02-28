import pygame
import sys

NAME = "GameBox"

class Error:  # ← inherit from Exception
    def __init__(self, message, dest):
        self.message = message
        self.dest = dest

    def __repr__(self):
        return f"{NAME}: {self.dest}: {self.message}"

    def __str__(self):  # optional but recommended
        return f"{NAME}: {self.dest}: {self.message}"

def raiseError(message, dest):
    print(Error(message, dest))
    sys.exit()

def ValueError(message, dest):
    print(Error(message, dest))
    sys.exit()

def Message(message, dest):
    print(Error(message, dest)) 

class Errors:
    def __init__(self):
        self.raiseError = raiseError
        self.ValueError = ValueError
        self.Message = Message