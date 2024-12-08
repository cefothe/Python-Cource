x = 0
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'
import pgzrun
import random

WIDTH=800
HEIGHT=600


tank = Actor('tank_blue')
tank.y = 575
tank.x = 400
tank.angle = 90

def draw():
    tank.draw()

def update():
    if keyboard.left:
        tank.x = tank.x - 2
        tank.angle = 180
    elif keyboard.right:
        tank.x = tank.x + 2
        tank.angle = 0
    elif keyboard.up:
        tank.y = tank.y - 2
        tank.angle = 90
    elif keyboard.down:
        tank.y = tank.y + 2
        tank.angle = 270

pgzrun.go()