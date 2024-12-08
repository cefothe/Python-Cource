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

pgzrun.go()