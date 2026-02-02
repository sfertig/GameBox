import pygame

from .Net import Global

class _image:
    def __init__(self, pos, image, scale, show):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.scale = scale
        self.show=show

    def move_to(self, pos):
        self.pos = pygame.Vector2(pos)
    def move_by(self, x, y):
        self.pos.x += x
        self.pos.y += y

    def change_scale(self, amount):
        self.scale += amount
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale)))

def load_image(image) -> pygame.Surface:
    if type(image) == str:
        return pygame.image.load(image)
    return image

class Image(_image):
    def __init__(self, pos, image, scale, show=True, layer=0):
        super().__init__(pos, load_image(image), scale, show)
        self.layer = layer
        Global.objs[str(self.layer)].append(self)

    def update(self):
        if self.show: self.draw()

    def draw(self):
        if Global.cam.zoom != 0:
            image = pygame.transform.scale(self.image, (int(self.image.get_width() * Global.cam.zoom), int(self.image.get_height() * Global.cam.zoom)))
            Global.screen.blit(image, self.pos - Global.cam.pos)
        else:
            Global.screen.blit(self.image, self.pos)

class Text:
    def __init__(self, pos, text, font, color, show=True, ui=True, layer=0):
        self.pos = pygame.Vector2(pos)
        self.text = text
        self.font = font
        self.color = color
        self.layer = layer
        self.ui = ui
        Global.objs[str(self.layer)].append(self)
        self.show = show

    def change(self, text):
        self.text = text

    def update(self):
        if self.show: self.draw()

    def draw(self):
        text = self.font.render(self.text, True, self.color)
        #scale if needed
        if Global.cam.zoom != 1.0: text = pygame.transform.scale_by(text, Global.cam.zoom)

        if self.ui: Global.screen.blit(text, self.pos)
        else:
            sp = self.pos - Global.cam.pos
            Global.screen.blit(text, sp)
        
        
