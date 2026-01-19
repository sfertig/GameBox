import pygame
import numpy as np

from ..basics.utils import zeroOut
from ..basics._net import Global

class _Conditions:
    """
    Class containing the predefined conditions for the game.
    Conditions are in the format of 'C' followed by the command ('v' for velocity), and dir (^ up, _ down, < left, > right, # none, ~ any)
    """

    def __init__(self):
        """
        Initialize the conditions.
        """
        # conditions start with 'C' and then command ('v' for velocity), and dir (^ up, _ down, < left, > right, # none, ~ any)
        self.velocity_up = 'CV^'  # velocity up
        self.velocity_down = 'CV_'  # velocity down
        self.velocity_left = 'CV<'  # velocity left
        self.velocity_right = 'CV>'  # velocity right
        self.velocity_none = 'CV#'  # velocity none
        self.velocity_any = 'CV~'  # velocity any

Conditions = _Conditions()
Global.cond = Conditions

class Condition_check:
    def __init__(self, stateTree: dict[str, dict[_Conditions, str]], currentState: str):
        self.stateTree = stateTree
        self.currentState = currentState
        
    def check(self, velocity: tuple, pos: tuple):
        state = self.stateTree[self.currentState]
        for cond, next in state.items():
            #velocities
            if cond[1] == 'V':
                if self._resolve_velocities(velocity, cond):
                    self.currentState = next
                    return next
        return self.currentState
                

    def _resolve_velocities(self, velocities, cond):
        vx, vy = velocities
        Max = 0.3
        vx = zeroOut(vx, Max)
        vy = zeroOut(vy, Max)
        dir = cond[2]
        print(vx, vy, dir)
        #resolve in order up, down, left, right, none, any
        if dir == "^" and vy < 0: return True
        if dir == "_" and vy > 0: return True
        if dir == "<" and vx < 0: return True
        if dir == ">" and vx > 0: return True
        if dir == "#" and vx == 0 and vy == 0: return True
        if dir == "~" and (vx != 0 or vy != 0): return True
        return False

    def updateState(self, state: str):
        self.currentState = state
    def updateStateTree(self, stateTree: dict[str, dict[_Conditions, str]]):
        self.stateTree = stateTree
            

