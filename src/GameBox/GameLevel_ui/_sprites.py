import pygame
import numpy as np

from ..basics._net import Global
from ._Animations import Animation

class Sprite_2d:
    def __init__(self, pos: tuple, image, scale: float = 1.0, collision = True, dirrection: int = 1):
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
        self.dir = dirrection

        self.pos = pos
        if type(image) == str:
            self.image = pygame.image.load(image)
        else:
            self.image = image
        
        #scale image
        print(self.image)
        self.image = pygame.transform.scale_by(self.image, scale)
        #flip image
        if self.dir == -1:
            self.image = pygame.transform.flip(self.image, True, False)

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

    def switch_dirrection(self):
        self.image = pygame.transform.flip(self.image, True, False)
        

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

def split_image(image, tileDim, startPos):
    if type(image) == str:
        image = pygame.image.load(image)
    else:
        image = image

    #return image split
    x = startPos[0] * tileDim[0]
    y = startPos[1] * tileDim[1]
    return image.subsurface((x, y, tileDim[0], tileDim[1]))

class Animated_Sprite2D:
    """
    A class for animated 2D sprites.

    Args:
        pos (tuple): The position of the sprite in world space.
        image (str or pygame.Surface): The image of the sprite.
        imageDim (tuple): The dimensions of the image.
        tileDim (tuple): The dimensions of the tiles in the image.
        frames (int): The number of frames in the animation.
        speed (float): The speed of the animation.
        scale (float): The scale of the sprite.
        collision (bool): Whether the sprite has collision.
        dirrection (int): The direction of the sprite.

    Attributes:
        animation (Animation): The animation of the sprite.
        collision (bool): Whether the sprite has collision.
        dir (int): The direction of the sprite.
        pos (tuple): The position of the sprite in world space.
        scale (float): The scale of the sprite.
        image (pygame.Surface): The current frame of the animation.
        __worldPos__ (bool): Whether the sprite is in world space.

    Methods:
        update (None): Updates the sprite.
        __remove__ (None): Removes the sprite from the game.
        switch_dirrection (None): Switches the direction of the sprite.
        move_by (x, y): Moves the sprite by (x, y) in world space.
        move_to (x, y): Moves the sprite to (x, y) in world space.
        get_pos (None): Returns the position of the sprite in world space.
        rescale (scale): Rescales the sprite by the given scale.
    """

    def __init__(self, pos, image, imageDim, tileDim, frames, speed, scale = 1.0, collision = True, dirrection = 1):
        """
        
        """

        self.animation = Animation(image, tileDim, (0, 0), frames, speed)
        self.collision = collision
        self.dir = dirrection
        self.pos = pos

        self.scale = scale
        self.image = pygame.transform.scale_by(self.animation.getFrame(), scale)
        if self.dir == -1:
            self.image = pygame.transform.flip(self.image, True, False)

        self.__worldPos__ = True

        #add to game
        Global.game.objs.append(self)

    def update(self):
        self.animation.update(Global.dt)
        self.image = pygame.transform.scale_by(self.animation.getFrame(), self.scale)
        if self.dir == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        
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

    def __remove__(self):
        Global.game.objs.remove(self)

    def switch_dirrection(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def move_by(self, x: int, y: int):
        self.pos = (self.pos[0] + x, self.pos[1] + y)

    def move_to(self, x: int, y: int):
        self.pos = (x, y)

    def get_pos(self):
        return self.pos

    def rescale(self, scale: float):
        self.image = pygame.transform.scale_by(self.image, scale)

class AnimationPlayer2D:
    """
    Class for playing animations in a 2D game.

    Attributes:
        pos (tuple): Position of the AnimationPlayer2D.
        scale (float): Scale of the AnimationPlayer2D.
        anims (dict): Dictionary of animations that can be played, where the key is the name of the animation and the value is an instance of Animated_Sprite2D.
        currentAnim (str): The name of the currently playing animation.

    Methods:
        update (None): Updates the currently playing animation.
        add_animation (name, image, imageDim, tileDim, frames, speed, scale = 1.0, collision = True, dirrection = 1): Adds an animation to the AnimationPlayer2D.
        remove_animation (name: str): Removes an animation from the AnimationPlayer2D.
        set_worldPos (worldPos: bool): Sets the world position of all animations in the AnimationPlayer2D.
        __remove__ (None): Removes the AnimationPlayer2D from the game.
        set_scale (scale: float): Sets the scale of all animations in the AnimationPlayer2D.
        set_animation (anim: str): Sets the currently playing animation.
        move_by (x, y): Moves the AnimationPlayer2D by (x, y) in world space.
        move_to (x, y): Moves the AnimationPlayer2D to (x, y) in world space.
        get_pos (None): Returns the position of the AnimationPlayer2D in world space.
    """
    def __init__(self, pos, scale):
        self.pos = pos
        self.scale = scale
        self.anims = {}
        self.currentAnim = None

        self.__worldPos__ = True

        #add to game
        Global.game.objs.append(self)

    def update(self):
        if self.currentAnim is not None:
            self.anims[self.currentAnim].update()

    def add_animation(self, name, image, imageDim, tileDim, frames, speed, scale = 1.0, collision = True, dirrection = 1):
        self.anims[name] = Animated_Sprite2D(self.pos, image, imageDim, tileDim, frames, speed, scale, collision, dirrection)
        self.currentAnim = name
        self.anims[self.currentAnim].__remove__()

    def remove_animation(self, name: str):
        self.anims[name].__remove__()
        del self.anims[name]

    def set_worldPos(self, worldPos: bool):
        for anim in self.anims:
            self.anims[anim].__worldPos__ = worldPos

    def __remove__(self):
        if self in Global.game.objs:
            Global.game.objs.remove(self)

    def set_scale(self, scale: float):
        for anim in self.anims:
            self.anims[anim].rescale(scale)

    def set_animation(self, anim: str):
        self.currentAnim = anim

    def move_by(self, x: int, y: int):
        self.pos = (self.pos[0] + x, self.pos[1] + y)
        for anim in self.anims:
            self.anims[anim].move_by(x, y)

    def move_to(self, x: int, y: int):
        self.pos = (x, y)
        for anim in self.anims:
            self.anims[anim].move_to(x, y)

    def get_pos(self):
        return self.pos


