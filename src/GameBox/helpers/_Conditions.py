import pygame
import numpy as np

from ..basics._net import Global

class _Conditions:
    def __init__(self):
        #conditions start with 'C' and then command ('v' for velocity), and dir (^ up, _ down, < left, > right, # none, ~ any)
        self.velocity_up = 'CV^'
        self.velocity_down = 'CV_'
        self.velocity_left = 'CV<'
        self.velocity_right = 'CV>'
        self.velocity_none = 'CV#'
        self.velocity_any = 'CV~'

Conditions = _Conditions()
Global.cond = Conditions

class Condition_check:
    def __init__(self, stateTree: Dict[str, Dict[_Conditions, str]], currentState: str):
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
        dir = cond[2]
        #resolve in order up, down, left, right, none, any
        if dir == "^" and vy < 0: return True
        if dir == "_" and vy > 0: return True
        if dir == "<" and vx < 0: return True
        if dir == ">" and vx > 0: return True
        if dir == "#" and vx == 0 and vy == 0: return True
        if dir == "~": return True
        return False
            

