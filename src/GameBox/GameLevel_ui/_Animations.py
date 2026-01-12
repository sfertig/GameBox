import pygame
import numpy as np

from ..basics._net import Global

class Animation:
    def __init__(self, image, tileDim, startPos, frames, dur):
        if type(image) == str:
            if image not in Global.images:
                image = pygame.transform.scale_by(pygame.image.load(image), scale)
            else:
                image = Global.images[image].copy()
        else:
            image = pygame.transform.scale_by(image, scale)
        
        #cache the image
        Global.images[image] = image

        #others
        self.dur = dur
        self.currentFrame = 0
        self.currentDur = 0

        #get frames from image
        self.frames = []
        x, y = startPos
        x *= tileDim[0]
        y *= tileDim[1]
        for i in range(frames):
            self.frames.append(image.subsurface(x, y, tileDim[0], tileDim[1]))
            x += tileDim[0]
            if x >= image.get_width():
                x = 0
                y += tileDim[1]

    def update(self, dt):
        self.currentDur += dt
        if self.currentDur >= self.dur:
            self.currentDur = 0
            self.currentFrame += 1
            if self.currentFrame >= len(self.frames):
                self.currentFrame = 0

    def getFrame(self):
        return self.frames[self.currentFrame]


