import pygame
from ..Net import Global

class Tree:
    def __init__(self, root, branches=[]):
        self.root = root
        try:
            self.rPos = root.pos.copy()
        except:
            Global.errors.raiseError("Root not found: " + f"{str(root)}: Type {type(root)}", "Tree")
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
                    if hasattr(branch, "pos"):
                        branch.pos += movement
                    elif type(branch) == Tree:
                        branch.root.pos += movement
                    else:
                        Global.errors.raiseError("Branch not found: " + f"{str(branch)}: Type {type(branch)}", "Tree")
            self.rPos = self.root.pos.copy()

    def _del_global_(self):
        Global.objs["0"].remove(self)

