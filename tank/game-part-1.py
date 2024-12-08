x = 0
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'
import pgzrun
import random

WIDTH=800
HEIGHT=600


pgzrun.go()