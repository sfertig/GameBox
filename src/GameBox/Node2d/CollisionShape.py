import pygame
from ..Net import Global
from .Node2D import Node2D
from ..basics.utils import on_screen
from ..controle.Tree import Tree

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
        Global.collision_shapes[self] = ""
        Global.objs[str(0)].append(self)

    def get_rect(self):
        return pygame.Rect(self.pos-self.dim/2, self.dim)

    def update(self):
        if self.show:
            sp = self.pos - Global.cam.pos
            if on_screen(sp):
                pygame.draw.rect(Global.screen, self.color, ((sp-self.dim/2), self.dim))

    def delete(self):
        Global.objs[str(0)].remove(self)
        del Global.collision_shapes[self]
#endregion

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
        if type(collisionShape) not in SHAPES:
            Global.errors.raiseError("Shape not found: " + f"{str(collisionShape)}: Type {type(collisionShape)}", "Area2D")
        self.shape = collisionShape
        self.tree = Tree(self, [self.shape])

        #properties
        self.overlapping = False


    def update(self):
        self.check_collision()

    def check_collision(self):
        for shape in Global.collision_shapes:
            if shape != self.shape and type(shape) == CollisionShape_Rect:
                if self.shape.get_rect().colliderect(shape.get_rect()):
                    self.overlapping = True
                    break
                else:
                    self.overlapping = False

    def delete(self):
        Global.objs[str(self.layer)].remove(self)
        del self.tree

#endregion

