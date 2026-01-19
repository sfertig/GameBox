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
    offset = 0

    prev_rect = pygame.Rect(x - vx, y - vy, dim[0], dim[1])
    rect = pygame.Rect(x, y, dim[0], dim[1])

    # =====================
    # Y AXIS COLLISION
    # =====================
    y_hit = None

    for collision in collisions:
        if Global._debug:
            pygame.draw.rect(Global.screen, "yellow", collision, 2)

        if collision.colliderect(rect):
            if vy > 0 and prev_rect.bottom <= collision.top:
                if y_hit is None or collision.top < y_hit.top:
                    y_hit = collision
            elif vy < 0 and prev_rect.top >= collision.bottom:
                if y_hit is None or collision.bottom > y_hit.bottom:
                    y_hit = collision

    if y_hit:
        if vy > 0:
            y = y_hit.top - dim[1] - offset
        else:
            y = y_hit.bottom + offset
        vy = 0

    # update rect after Y resolution
    rect.y = y

    # =====================
    # X AXIS COLLISION
    # =====================
    x_hit = None

    for collision in collisions:
        if collision.colliderect(rect):

            # ONLY resolve X if we were NOT overlapping horizontally last frame
            if prev_rect.right <= collision.left and vx > 0:
                if x_hit is None or collision.left < x_hit.left:
                    x_hit = collision

            elif prev_rect.left >= collision.right and vx < 0:
                if x_hit is None or collision.right > x_hit.right:
                    x_hit = collision

    if x_hit:
        if vx > 0:
            x = x_hit.left - dim[0] - offset
        else:
            x = x_hit.right + offset
        vx = 0

    if Global._debug:
        pygame.draw.rect(
            Global.screen,
            "green",
            rect,
            2
        )
        pygame.draw.rect(
            Global.screen,
            "red",
            prev_rect,
            1
        )
        pygame.draw.rect(
            Global.screen,
            "blue",
            (x, y, dim[0], dim[1]),
            2
        )

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

