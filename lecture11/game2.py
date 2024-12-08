import pgzrun
import os

WIDTH = 600
HEIGHT = 600

os.environ['SDL_VIDEO_CENTERED'] = '1'
background = Actor("background")

def draw():
    screen.clear()
    background.draw()

def update():
     if keyboard.right:
        player.x = player.x + 4

pgzrun.go()
