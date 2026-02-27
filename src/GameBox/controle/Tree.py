import pygame
from ..Net import Global

class Tree:
    def __init__(self, root):
        self.root = root
        self.branches = []
        Global.objs["-1"].append(self)

    def add_branch(self, branch):
        self.branches.append(branch)
    def remove_branch(self, branch):
        self.branches.remove(branch)

    def update(self):
        "will move branches if root is moving"
        if hasattr(self.root, "pos"):
            for branch in self.branches:
                branch.pos = self.root.pos + branch.pos

    def _del_global_(self):
        Global.objs["-1"].remove(self)
