import pygame
import numpy as np

from .Net import Global

class shape:
    def __init__(self, pos, dim, color):
        self.pos = np.array(pos)
        self.dim = np.array(dim)
        self.color = color

    def move_to(self, x, y):
        self.pos = np.array([x, y])
    def move_by(self, x, y):
        self.pos += np.array([x, y])
    
    def scale(self, factor):
        self.dim *= factor
    def set_dim(self, width, height):
        self.dim = np.array([width, height])
    def change_dim(self, width, height):
        self.dim += np.array([width, height])
    def set_color(self, color):
        self.color = color

    def collide(self, obj):
        rect = pygame.Rect(self.pos, self.dim)
        if hasattr(obj, 'pos') and hasattr(obj, 'dim'):
            obj_rect = pygame.Rect(obj.pos, obj.dim)
            return rect.colliderect(obj_rect)
        print(f"<GameBox> Error: Object {obj} does not have pos and dim attributes and can't be collided with")
        return False

class Rect(shape):
    def __init__(self, pos, dim, color, collision=True, layer=3):
        super().__init__(np.array(pos), np.array(dim), color)
        self.collision = collision
        self.layer = layer

        Global.objs[str(layer)].append(self)

    def update(self):
        self.draw()

    def _addCollision(self):
        if self.collision:
            rect = pygame.Rect(self.pos, self.dim)
            Global.collision.append(rect)

    def draw(self):
        sp = (self.pos - Global.cam.pos) * Global.cam.zoom
        ss = self.dim * Global.cam.zoom
        pygame.draw.rect(Global.screen, self.color, (sp, ss))

    def delete(self):
        Global.objs[str(self.layer)].remove(self)

class Circle(shape):
    def __init__(self, pos, radius, color, layer=3):
        super().__init__(np.array(pos), np.array([radius, radius]), color)
        self.collision = False
        self.layer = layer
        Global.objs[str(layer)].append(self)

    def update(self):
        self.draw()

    def _addCollision(self):
        if self.collision:
            rect = pygame.Rect(self.pos, self.dim)
            Global.collision.append(rect)

    def draw(self):
        sp = (self.pos - Global.cam.pos) * Global.cam.zoom
        ss = self.dim * Global.cam.zoom
        pygame.draw.circle(Global.screen, self.color, (sp), ss[0]//2)

    def delete(self):
        Global.objs[str(self.layer)].remove(self)

