import pygame

from .Net import Global

class shape:
    def __init__(self, pos, dim, color, show):
        self.pos = pygame.Vector2(pos)
        self.dim = pygame.Vector2(dim)
        self.color = color
        self.show = show

    def move_to(self, x, y):
        self.pos = pygame.Vector2(x, y)
    def move_by(self, x, y):
        self.pos += pygame.Vector2(x, y)
    
    def scale(self, factor):
        self.dim *= factor
    def set_dim(self, width, height):
        self.dim = pygame.Vector2(width, height)
    def change_dim(self, width, height):
        self.dim += pygame.Vector2(width, height)
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
    def __init__(self, pos, dim, color, show=True, collision=True, layer=3):
        super().__init__(pos, dim, color, show)
        self.collision = collision
        self.layer = layer

        Global.objs[str(layer)].append(self)

    def update(self):
        if self.show: self.draw()

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
    def __init__(self, pos, radius, color, show=True, layer=3):
        super().__init__(pos, pygame.Vector2(radius, radius), color)
        self.collision = False
        self.layer = layer
        Global.objs[str(layer)].append(self)

    def update(self):
        if self.show: self.draw()

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

