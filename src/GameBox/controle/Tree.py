import pygame
from ..Net import Global

class Tree:
    def __init__(self, root, branches=[]):
        self.root = root
        self.rPos = root.pos.copy()
        self.branches = [*branches]
        Global.objs["0"].append(self)

    def add_branch(self, branch):
        self.branches.append(branch)
    def remove_branch(self, branch):
        self.branches.remove(branch)

    def update(self):
        "will move branches if root is moving"
        if hasattr(self.root, "pos"):
            if self.root.pos != self.rPos:
                movement = self.root.pos - self.rPos
                for branch in self.branches:
                    branch.pos += movement
            self.rPos = self.root.pos.copy()

    def _del_global_(self):
        Global.objs["0"].remove(self)

