import pgzrun
import os
import random

# Center the pygame window on the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'
TITLE="CHASE GAME"
WIDTH=600
HEIGHT=600
background=Actor("background")
player=Actor("player")
coin=Actor("coin",pos=(300,300))
def draw():
    screen.clear()
    background.draw()
    player.draw()
    coin.draw()
def update():
    if keyboard.right:
        player.x+=4
    if keyboard.left:
        player.x+=-4
    if keyboard.up:
        player.y+=-4
    if keyboard.down:
        player.y+=4
    if coin.colliderect(player):
        coin.x=random.randint(0,WIDTH)
        coin.y=random.randint(0,HEIGHT)
pgzrun.go()