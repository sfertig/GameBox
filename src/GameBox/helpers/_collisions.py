import pygame
import numpy as np

from ..basics._net import Global


def CheckCollisions(x, y, vx, vy, dim, sample, obj):
        x, y = x + vx, y + vy


        #basic object collisions
        x, y, vx, vy = _mainCollisionLogic(Global.collisions, x, y, vx, vy, dim)
        x, y, vx, vy = _checkTilemapCollisions(x, y, vx, vy, dim, sample, obj)

        return x, y, vx, vy
    
def _mainCollisionLogic(collisions, x, y, vx, vy, dim):
    new_rect = pygame.Rect((x, y), dim)
    for collision in collisions:
        #pygame.draw.rect(Global.screen, (255, 0, 0), collision, 1)
        if collision.colliderect(new_rect):
            if vx > 0:
                x = collision.left - dim[0]
            elif vx < 0:
                x = collision.right
            vx = 0

    # Y-axis collisions
    new_rect = pygame.Rect((x, y), dim)
    for collision in collisions:
        #pygame.draw.rect(Global.screen, (255, 0, 0), collision, 1)
        if collision.colliderect(new_rect):
            if vy > 0:  # falling
                y = collision.top - dim[1]
                vy = 0
            elif vy < 0:  # jumping
                y = collision.bottom
                vy = 0

    return x, y, vx, vy
    
def _checkTilemapCollisions(x, y, vx, vy, dim, sample, obj):
    if len(Global.tilemap) == 0:
        return x, y, vx, vy
    
    for tilemap in Global.tilemap:
    
        #get player reletive tilemap  pos
        prect = pygame.Rect(x, y, dim[0], dim[1])
        prx, pry = prect.center
        if Global.cam.follow != obj:
            if Global.cam.x != 0 or Global.cam.y != 0:
                px = int((prx) - Global.cam.x)
                py = int((pry) - Global.cam.y) 
                px = int(px  // tilemap.tileDim[0])
                py = int(py  // tilemap.tileDim[1])
            else:
                px = int((x) / tilemap.tileDim[0])
                py = int((y ) / tilemap.tileDim[1])
        else:
            if Global.cam.x != 0 or Global.cam.y != 0:
                px = int(((prx + Global.cam.x)) // tilemap.tileDim[0])
                py = int(((pry + Global.cam.y)) // tilemap.tileDim[1])
            else:
                px = int((x) / tilemap.tileDim[0])
                py = int((y) / tilemap.tileDim[1])


        #check if player is on tilemap
        if px < 0 or px >= tilemap.mapDim[0] or py < 0 or py >= tilemap.mapDim[1]:
            return x, y, vx, vy
        #get collision rects around player
        collisions: list[pygame.Rect] = []
        for tx in range(px - sample, px + sample):
            for ty in range(py - sample, py + sample):
                nx = int(px + tx)
                ny = int(py + ty)
                #if tile is on map
                if nx < 0 or nx >= tilemap.mapDim[0] or ny < 0 or ny >= tilemap.mapDim[1]:
                    continue
                #if tile has defined collision shape
                tile = str(tilemap.map[ny][nx])
                if tile not in tilemap.collisionDict: continue

                #get collision shape 
                rectshape = tilemap.collisionDict[str(tile)]
                rect = getattr(tilemap.collisionShapes, rectshape).copy()

                # Position rect correctly in the world
                if Global.cam.follow != obj:
                    if Global.cam.x != 0 or Global.cam.y != 0:
                        rect.x = ((nx * tilemap.tileDim[0])) - Global.cam.x
                        rect.y = ((ny * tilemap.tileDim[1])) - Global.cam.y
                    else:
                        rect.x += (nx * tilemap.tileDim[0]) - Global.cam.x
                        rect.y += (ny * tilemap.tileDim[1]) - Global.cam.y
                else:
                    if Global.cam.x != 0 or Global.cam.y != 0:
                        rect.x += ((nx * tilemap.tileDim[0])) - Global.cam.x
                        rect.y += ((ny * tilemap.tileDim[1])) - Global.cam.y
                    else:
                        rect.x += (nx * tilemap.tileDim[0]) - Global.cam.x
                        rect.y += (ny * tilemap.tileDim[1]) - Global.cam.y
                collisions.append(rect)

        #check collisions
        x, y, vx, vy = _mainCollisionLogic(collisions, x, y, vx, vy, dim)

        return x, y, vx, vy

