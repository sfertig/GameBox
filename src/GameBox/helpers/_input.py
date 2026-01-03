import pygame

from ..basics._net import Global


class _keys:
    def __init__(self):
        #alphabet
        self.a = pygame.K_a
        self.b = pygame.K_b
        self.c = pygame.K_c
        self.d = pygame.K_d
        self.e = pygame.K_e
        self.f = pygame.K_f
        self.g = pygame.K_g
        self.h = pygame.K_h
        self.i = pygame.K_i
        self.j = pygame.K_j
        self.k = pygame.K_k
        self.l = pygame.K_l
        self.m = pygame.K_m
        self.n = pygame.K_n
        self.o = pygame.K_o
        self.p = pygame.K_p
        self.q = pygame.K_q
        self.r = pygame.K_r
        self.s = pygame.K_s
        self.t = pygame.K_t
        self.u = pygame.K_u
        self.v = pygame.K_v
        self.w = pygame.K_w
        self.x = pygame.K_x
        self.y = pygame.K_y
        self.z = pygame.K_z

        #numbers
        self.n0 = pygame.K_0
        self.n1 = pygame.K_1
        self.n2 = pygame.K_2
        self.n3 = pygame.K_3
        self.n4 = pygame.K_4
        self.n5 = pygame.K_5
        self.n6 = pygame.K_6
        self.n7 = pygame.K_7
        self.n8 = pygame.K_8
        self.n9 = pygame.K_9

        #special keys
        self.enter = pygame.K_RETURN
        self.escape = pygame.K_ESCAPE
        self.space = pygame.K_SPACE
        self.backspace = pygame.K_BACKSPACE

        #arrow keys
        self.up = pygame.K_UP
        self.down = pygame.K_DOWN
        self.left = pygame.K_LEFT
        self.right = pygame.K_RIGHT


Keys = _keys()