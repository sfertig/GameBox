from src.GameBox import *
import pygame

width, height = 800, 600

game = Game(width, height)
G = game._fetch_global()
screen = game.get_screen()

cam = Cammera(smooth=0.2)

class _player:
    def __init__(self, pos, dim, color):
        self.pos = pygame.Vector2(pos)
        self.dim = pygame.Vector2(dim)
        self.color = color
        G.objs["4"].append(self)

    def rect(self):
        return pygame.Rect(self.pos, self.dim)

    def update(self):
        r = self.rect()
        r.x -= G.cam.pos.x
        r.y -= G.cam.pos.y
        pygame.draw.rect(screen, self.color, r)

p = _player((width / 2, height / 2), (50, 50), "green")
speed = 500
cam.set_target(p)

r = Rect((0, 0), (50, 50), "red")

running = True
while running:
    events = pygame.event.get()
    for event in events:    
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: p.pos.y -= speed * G.dt
    if keys[pygame.K_s]: p.pos.y += speed * G.dt
    if keys[pygame.K_a]: p.pos.x -= speed * G.dt
    if keys[pygame.K_d]: p.pos.x += speed * G.dt

    game.update(events)

game.quit()
pygame.quit()
