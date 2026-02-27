import pygame

NAME = "GameBox"

class Error(Exception):  # ← inherit from Exception
    def __init__(self, message, dest):
        super().__init__(message)
        self.message = message
        self.dest = dest

    def __repr__(self):
        return f"{NAME}: {self.dest}: {self.message}"

    def __str__(self):  # optional but recommended
        return f"{NAME}: {self.dest}: {self.message}"

def raiseError(message, dest):
    raise Error(message, dest)

def ValueError(message, dest):
    print(f"{NAME}: {dest}: {message}")

class Errors:
    def __init__(self):
        self.raiseError = raiseError
        self.ValueError = ValueError