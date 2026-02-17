import pygame

from ..basics.Net import Global


def CollisionLogic(vel, pos, dim):
    x, y = pos
    vx, vy = vel

    x, y, vx, vy = _Collisions(x, y, vx, vy, dim, Global.collision)
    x, y, vx, vy = _tilemapCollisions(x, y, vx, vy, dim)

    pos = pygame.Vector2(x, y)
    vel = pygame.Vector2(vx, vy)

    return pos, vel


def _Collisions(x, y, vx, vy, dim, shapes):
    # Apply movement
    x += vx
    y += vy

    rect = pygame.Rect(x, y, dim.x, dim.y)

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


def _tilemapCollisions(x, y, vx, vy, dim):
    for map in Global.tilemaps:
        #get player tilemap pos
        tx = x//map.tileDim[0]
        ty = y//map.tileDim[1]
        x, y, vx, vy = _Collisions(x, y, vx, vy, dim, map.get_collisions_around((pygame.Vector2(tx, ty))))
    return x, y, vx, vy
