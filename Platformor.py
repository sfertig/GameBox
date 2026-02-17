from src.GameBox import *
import pygame

width, height = 800, 600

game = Game(width, height)
G = game._fetch_global()
screen = game.get_screen()

cam = Cammera()

player = Player((width / 2, height / 2), (50, 50), "green")
player.add_physics(0, 0, 0, (25, 25), (0.75, 0.75))
cam.set_target(player)

map = Tilemap("tests/assets/levelTiles.png", (16, 16), 3.0)
map.load_from_json("tests/assets/map1.json")

x, y, z = 0, 0, 0
xDir, yDir, zDir = 1, 1, 1
xCycle, yCycle, zCycle = 0, 0, 0
xMax, yMax, zMax = 255, 255, 255

running = True
while running:
    events = pygame.event.get()
    for event in events:    
        if event.type == pygame.QUIT:
            running = False

    xCycle += xDir
    if xCycle > 255:
        xDir = -1
        xCycle = 255
    x = int(xCycle)

    yCycle += yDir
    if yCycle > 255:
        yDir = -1
        yCycle = 255
    y = int(yCycle)

    zCycle += zDir
    if zCycle > 255:
        zDir = -1
        zCycle = 255
    z = int(zCycle)

    print(x, y, z)
    G.bg_color = (x, y, z)

    player.move.by_WSAD(3.8)

    game.update(events)

game.quit()
pygame.quit()
