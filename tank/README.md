# Tank game

## Create the pygame scren

```python
x = 0
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'
import pgzrun
import random

WIDTH=800
HEIGHT=600


pgzrun.go()
```
## Draw the tank in botton line 

1) Creata a tank Actor
```python

tank = Actor('tank_blue')
tank.y = 575
tank.x = 400
tank.angle = 90
```

2) Draw the tank

```python
def draw():
    tank.draw()
```

## Move the tank around 

```python
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
```
## Add the grass background and draw it

1) Create a background actor

```python
background = Actor('grass')
```

2) Draw the background inside the draw function add

```python
background.draw()
```

## Add random walls 

1) Create a array of walls elements and fill them with data
```python
walls = []
for x in range(16):
    for y in range(10):
        if random.randint(0, 100) < 50:
            wall = Actor('wall')
            wall.x = x * 50 + 25
            wall.y = y * 50 + 25 + 50
            walls.append(wall)
```
2) Draw all walls
```python
for wall in walls:
    wall.draw()
```

## Prevent moving though walls

1) In the begging of update method add
```python
original_x = tank.x
original_y = tank.y
```
2) Add the following check at the end of the update method
```python
if tank.collidelist(walls) != -1:
    tank.x = original_x
    tank.y = original_y
```
## Prevent going outside of screen
Add following code inside the update function
```python
if tank.x < 0 or tank.x > 800 or tank.y < 0 or tank.y > 600:
    tank.x = original_x
    tank.y = original_y
```
## Add enemies on the screen
1) Add following code before all methods
```python
enemies = []
for i in range(3):
    enemy = Actor('tank_red')
    enemy.y = 25
    enemy.x = i * 200 + 100
    enemy.angle = 270
    enemy.move_count = 0
    enemies.append(enemy)
```

2) Draw the enemies, add following code inside the draw function
```python
for enemy in enemies:
    enemy.draw()
```

## Let's make enemies moves around 
Inside the update function add following code
```python
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
```
## Let's start shooting -> Player tank

1) Define a variable `bullet_holdoff = 0`
2) Define a variable of type array bullet `bullets = []`
3) Inside the update function add following code
```python
    if bullet_holdoff == 0:
        if keyboard.space:
            bullet = Actor('bulletblue2')
            bullet.angle = tank.angle
            bullet.x = tank.x
            bullet.y = tank.y
            bullets.append(bullet)
            bullet_holdoff = 100
    else:
        bullet_holdoff = bullet_holdoff - 1
```
4) Draw the bullet
```python
        for bullet in bullets:
            bullet.draw()
```
5) Move bullets
```python
    for bullet in bullets:
        if bullet.angle == 0:
            bullet.x = bullet.x + 5
        elif bullet.angle == 90:
            bullet.y = bullet.y - 5
        elif bullet.angle == 180:
            bullet.x = bullet.x - 5
        elif bullet.angle == 270:
            bullet.y = bullet.y + 5

    for bullet in bullets:
        wall_index = bullet.collidelist(walls)
        if wall_index != -1:
            del walls[wall_index]
            bullets.remove(bullet)
            bullet_holdoff =0 
        if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
            bullets.remove(bullet)
            bullet_holdoff =0 
        enemy_index = bullet.collidelist(enemies)
        if enemy_index != -1:
            del enemies[enemy_index]
            bullets.remove(bullet)
            bullet_holdoff =0 
```

## Let's emenies shooting