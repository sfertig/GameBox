import pygame
from ..Net import Global

def clamp(value, min, max):
    return max(min, min(value, max))

def on_screen(pos, padding=125):
    return pos.x > 0-padding and pos.x < Global.screen.get_width()+padding and pos.y > 0-padding and pos.y < Global.screen.get_height()+padding
