import pygame
from ..Net import Global
from .Node2D import Node2D

def load_image(path):
    if isinstance(path, str):
        if path in Global.assets:
            return Global.assets[path]
        else:
            try:
                Global.assets[path] = pygame.image.load(path)
                return Global.assets[path]
            except:
                raise ValueError("Image not found: " + path)
    elif isinstance(path, pygame.Surface):
        return path
    else:
        raise ValueError("Image must be a string or a pygame.Surface")

#region Sprite2D
class Sprite2D(Node2D):
    def __init__(self, pos, image, layer=3, scale=1.0, ui=False, show=True):
        super().__init__(pos, layer, ui, show)
        self._del_global_()

        self.image = load_image(image)
        self.scale = scale
        if scale != 1.0:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale)).copy()
        Global.objs[str(layer)].append(self)

    def update(self):
        if self.show: self.render()

    def render(self):
        if not self.ui: sp = self.pos - Global.cam.pos
        else: sp = self.pos
        Global.screen.blit(self.image, sp-pygame.Vector2(self.image.get_size())/2)

    def rescale(self, scale):
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
#endregion
