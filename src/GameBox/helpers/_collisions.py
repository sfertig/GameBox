from ast import Break
import pygame
import numpy as np

from ..basics.Net import Global


def CollisionLogic(vel, pos, dim, sample):
    x, y = pos
    vx, vy = vel

    x, y, vx, vy = _Collisions(x, y, vx, vy, dim, Global.collision)
    x, y, vx, vy = _tilemapCollisions(x, y, vx, vy, dim, sample)

    pos = np.array([x, y], dtype=float)
    vel = np.array([vx, vy], dtype=float)

    return pos, vel


def _Collisions(x, y, vx, vy, dim, shapes):

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
            break
    # -----------------
    # X-axis movement
    # -----------------
    x += vx
    rect = pygame.Rect((x, y), dim)

    for collision in shapes:
        pygame.draw.rect(Global.screen, "red", collision, 1)
        if rect.colliderect(collision):
            if vx > 0:
                x = collision.left - dim[0]
            elif vx < 0:
                x = collision.right
            vx = 0
            rect.x = x
            break

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
                #get shape
                tile = str(map.map[int(ty+yIndex)][int(tx+xIndex)])
                if tile not in map.collisionDict: continue
                shape = map.collisionDict[str(tile)]
                rect = getattr(map.collisionShapes, shape).copy()
                rect.x += (tx+xIndex)*map.tileDim[0]
                rect.y += (ty+yIndex)*map.tileDim[1]
                collisions.append(rect)
        #collision math
        x, y, vx, vy = _Collisions(x, y, vx, vy, dim, collisions)
    return x, y, vx, vy
