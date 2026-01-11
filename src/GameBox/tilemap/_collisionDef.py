import pygame

class _tileCollisionDefs:
    def __init__(self, tileDim):
        width, height = tileDim


        self.rects = ["full", "halfLeft", "halfRight", "halfTop", "halfBottom", "topRight", 
                      "topLeft", "bottomRight", "bottomLeft", "center", "none", "dot"]
        
        self.num = len(self.rects) + 1

        self.full = pygame.Rect(0, 0, width, height)

        self.halfLeft = pygame.Rect(0, 0, width / 2, height)
        self.halfRight = pygame.Rect(width / 2, 0, width / 2, height)
        self.halfTop = pygame.Rect(0, 0, width, height / 2)
        self.halfBottom = pygame.Rect(0, height / 2, width, height / 2)

        self.topRight = pygame.Rect(width / 2, 0, width / 2, height / 2)
        self.topLeft = pygame.Rect(0, 0, width / 2, height / 2)
        self.bottomRight = pygame.Rect(width / 2, height / 2, width / 2, height / 2)
        self.bottomLeft = pygame.Rect(0, height / 2, width / 2, height / 2)

        self.dot = pygame.Rect(0, 0, 3, 3)

        self.center = pygame.Rect(width / 2, height / 2, width / 2, height / 2)

        self.none = pygame.Rect(0, 0, 0, 0)

    def regenerate(self, tileDim):
        width, height = tileDim
        self.full = pygame.Rect(0, 0, width, height)

        self.halfLeft = pygame.Rect(0, 0, width / 2, height)
        self.halfRight = pygame.Rect(width / 2, 0, width / 2, height)
        self.halfTop = pygame.Rect(0, 0, width, height / 2)
        self.halfBottom = pygame.Rect(0, height / 2, width, height / 2)

        self.center = pygame.Rect(width / 2, height / 2, width / 2, height / 2)

