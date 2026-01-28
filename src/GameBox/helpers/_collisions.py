import pygame
import numpy as np

from ..basics.Net import Global


def CollisionLogic(vel, pos, dim, sample):
    x, y = pos
    vx, vy = vel

    x, y, vx, vy = _Collisions(x, y, vx, vy, dim, Global.collision)
    #x, y, vx, vy = _tilemapCollisions(x, y, vx, vy, dim, sample)

    pos = np.array([x, y])
    vel = np.array([vx, vy])
    return pos, vel


def _Collisions(x, y, vx, vy, dim, shapes):
    # -----------------
    # X-axis movement
    # -----------------
    x += vx
    rect = pygame.Rect((x, y), dim)

    for collision in shapes:
        if rect.colliderect(collision):
            if vx > 0:
                x = collision.left - dim[0]
            elif vx < 0:
                x = collision.right
            vx = 0
            rect.x = x

    # -----------------
    # Y-axis movement
    # -----------------
    y += vy
    rect = pygame.Rect((x, y), dim)

    for collision in shapes:
        if rect.colliderect(collision):
            if vy > 0:  # falling
                y = collision.top - dim[1]
            elif vy < 0:  # jumping
                y = collision.bottom
            vy = 0
            rect.y = y

    # Debug draw (optional)
    pygame.draw.rect(Global.screen, "yellow", rect, 1)

    return x, y, vx, vy

def _tilemapCollisions(x, y, vx, vy, dim, sampleSize):
    for map in Global.tilemaps:
        #get player tilemap pos
        tx = x//map.tileDim[0]
        ty = y//map.tileDim[1]
        #get tiles around player
        collisions = []
        for yIndex in range(-sampleSize, sampleSize):
            for xIndex in range(-sampleSize, sampleSize):
                #if point not on map, skip
                if tx+xIndex < 0 or tx+xIndex >= map.mapDim[0] or ty+yIndex < 0 or ty+yIndex >= map.mapDim[1]: continue
                #get tile id
                tileId = map.map[ty+yIndex][tx+xIndex]
                #if tile is solid, add to collisions
                if tileId in map.collisionDict: collisions.append(map.collisionDict[tileId])
        #collision math
        x, y, vx, vy = _Collisions(x, y, vx, vy, dim, collisions)
    return x, y, vx, vy
