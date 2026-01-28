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
    # Apply movement
    x += vx
    y += vy

    rect = pygame.Rect(x, y, dim[0], dim[1])

    for collision in shapes:
        if not rect.colliderect(collision):
            continue

        # Calculate overlap on each side
        overlap_left   = rect.right - collision.left
        overlap_right  = collision.right - rect.left
        overlap_top    = rect.bottom - collision.top
        overlap_bottom = collision.bottom - rect.top

        # Find smallest overlap
        min_x = min(overlap_left, overlap_right)
        min_y = min(overlap_top, overlap_bottom)

        # Resolve on the axis with least penetration
        if min_x < min_y:
            if overlap_left < overlap_right:
                rect.right = collision.left
            else:
                rect.left = collision.right
            vx = 0
        else:
            if overlap_top < overlap_bottom:
                rect.bottom = collision.top
            else:
                rect.top = collision.bottom
            vy = 0

    return rect.x, rect.y, vx, vy


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
