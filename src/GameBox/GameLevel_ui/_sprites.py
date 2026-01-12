import pygame
import numpy as np

from ..basics._net import Global
from ._Animations import Animation

class Sprite_2d:
    def __init__(self, pos: tuple, image, scale: float = 1.0, collision = True):
        """
        Initialize a 2D sprite.
        
        Args:
            pos: Tuple (x, y) for the sprite position
            image: Either a file path (str) or pygame.Surface object
            scale: Scale factor for the sprite (default: 1.0)
        """
        #add to game
        Global.game.objs.append(self)
        self.collision = collision
        self.__worldPos__ = True

        self.pos = pos
        if type(image) == str:
            if image not in Global.images:
                self.image = pygame.transform.scale_by(pygame.image.load(image), scale)
            else:
                self.image = Global.images[image].copy()
        else:
            self.image = pygame.transform.scale_by(image, scale)
        
        #cache the image
        Global.images[image] = self.image

    def update(self):
        #world space
        x, y = self.pos
        if self.__worldPos__:
            x = x - Global.cam.x
            y = y - Global.cam.y
        Global.screen.blit(self.image, (x, y))
        if self.collision:
            rect = self.image.get_rect()
            rect.x = x
            rect.y = y
            Global.collisions.append(rect)

    def move_by(self, x: int, y: int):
        self.pos = (self.pos[0] + x, self.pos[1] + y)

    def move_to(self, x: int, y: int):
        self.pos = (x, y)

    def get_pos(self):
        return self.pos

    def rescale(self, scale: float):
        self.image = pygame.transform.scale_by(self.image, scale)

    def __remove__(self):
        Global.game.objs.remove(self)

class AnimatedSprite_2d(Sprite_2d):
    def __init__(self, pos: tuple, image, tileDim, startPos, frames, dur, collision = True):
        super().__init__(pos, image, collision=collision)
        self.animation = Animation(image, tileDim, startPos, frames, dur)
    
    def update(self):
        self.animation.update(Global.dt)
        #change to world space
        x, y = self.pos
        if self.__worldPos__:
            x = x - Global.cam.x
            y = y - Global.cam.y
        image = pygame.transform.scale_by(self.animation.getFrame(), 5.0)
        Global.screen.blit(image, (x, y))
        if self.collision:
            rect = image.get_rect()
            rect.x = x
            rect.y = y
            Global.collisions.append(rect)

class AnimationPlayer:
    def __init__(self, pos: tuple):
        self.pos = pos
        self.animations = {}
        self.current_animation = None

        Global.game.objs.append(self)

    def update(self):
        if self.current_animation is not None:
            self.animations[self.current_animation].update()
    
    def add_animation(self, name: str, animation: Animation):
        self.animations[name] = animation
        self.animations[name].__remove__()

    def play(self, name):
        """
        Play an animation by name
        """
        self.current_animation = name

    def __remove__(self):
        Global.game.objs.remove(self)
        