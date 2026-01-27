import pygame
import numpy as np

from ..basics.Net import Global


def CollisionLogic(vel, pos, dim):
    x, y = pos
    vx, vy = vel

    x, y, vx, vy = _Collisions(x, y, vx, vy, dim, Global.collision)

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
