import pygame
from ..Net import Global
from .Node2D import Node2D
from ..basics.utils import on_screen
from ..controle.Tree import Tree

SHAPES = {CollisionShape_Rect}

#region Area2D
class Area2D(Node2D):
    def __init__(self, pos, collisionShape, layer=3):
        super().__init__(pos, layer, False, False)
        self._del_global_()
        try:
            Global.objs[str(layer)].append(self)
        except:
            Global.errors.raiseError("Layer not found: " + str(layer), "Area2D")
        if collisionShape not in SHAPES:
            Global.errors.raiseError("Shape not found: " + f"{str(collisionShape)}: Type {type(collisionShape)}", "Area2D")
        self.shape = collisionShape
        self.tree = Tree(self, [self.shape])

    def update(self):
        pass

    def delete(self):
        Global.objs[str(self.layer)].remove(self)
        del self.tree

#endregion

#region CollisionShape
class CollisionShape(Node2D):
    def __init__(self, pos, dim, show=False):
        super().__init__(pos, 0, False, show)
        self._del_global_()
        self.color = "yellow"
        self.dim = dim
#endregion

#region Rect
class CollisionShape_Rect(CollisionShape):
    def __init__(self, pos, dim, show=False):
        super().__init__(pos, pygame.Vector2(dim), show)
        Global.collision_shapes[self] = "rect"
        Global.objs[str(0)].append(self)

    def update(self):
        if self.show:
            sp = self.pos - Global.cam.pos
            if on_screen(sp):
                pygame.draw.rect(Global.screen, self.color, ((sp-self.dim/2), self.dim))

    def delete(self):
        Global.objs[str(0)].remove(self)
        del Global.collision_shapes[self]
#endregion

