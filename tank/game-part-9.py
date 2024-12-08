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


background = Actor('grass')

walls = []
for x in range(16):
    for y in range(10):
        if random.randint(0, 100) < 50:
            wall = Actor('wall')
            wall.x = x * 50 + 25
            wall.y = y * 50 + 25 + 50
            walls.append(wall)


enemies = []
for i in range(3):
    enemy = Actor('tank_red')
    enemy.y = 25
    enemy.x = i * 200 + 100
    enemy.angle = 270
    enemy.move_count = 0
    enemies.append(enemy)

def draw():
    background.draw()
    tank.draw()
    for enemy in enemies:
        enemy.draw()
    for wall in walls:
        wall.draw()

def update():
    original_x = tank.x
    original_y = tank.y

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
        
    if tank.collidelist(walls) != -1:
        tank.x = original_x
        tank.y = original_y
        
    if tank.x < 0 or tank.x > 800 or tank.y < 0 or tank.y > 600:
        tank.x = original_x
        tank.y = original_y

pgzrun.go()