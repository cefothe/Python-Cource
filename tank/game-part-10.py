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
    for enemy in enemies:
        choice = random.randint(0, 2)
        if enemy.move_count > 0:
            enemy.move_count = enemy.move_count - 1

            original_x = enemy.x
            original_y = enemy.y
            if enemy.angle == 0:
                enemy.x = enemy.x + 2
            elif enemy.angle == 90:
                enemy.y = enemy.y - 2
            elif enemy.angle == 180:
                enemy.x = enemy.x - 2
            elif enemy.angle == 270:
                enemy.y = enemy.y + 2

            if enemy.collidelist(walls) != -1:
                enemy.x = original_x
                enemy.y = original_y
                enemy.moveCount = 0

            if enemy.x < 0 or enemy.x > 800 or enemy.y < 0 or enemy.y > 600:
                enemy.x = original_x
                enemy.y = original_y
                enemy.move_count = 0

        elif choice == 0:
            enemy.move_count = 20
        elif choice == 1:
            enemy.angle = random.randint(0, 3) * 90
pgzrun.go()