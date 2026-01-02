import pygame
import math
import numpy as np

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)
def moveTward(value, target, speed):
    if value < target:
        value += speed
    elif value > target:
        value -= speed
    return value

def zeroOut(value, max):
    if value < 0 and value > -max: value = 0
    if value > 0 and value < max: value = 0
    return value
