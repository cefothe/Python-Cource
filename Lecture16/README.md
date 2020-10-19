# Shooting game

The `player` and `background` variables will contain Actors. The others
are lists which we initialize to the empty list `[]`. Actors will be
appended to the lists later.

```python
    import random

    WIDTH = 600
    HEIGHT = 800
    MAX_BULLETS = 3

    level = 1
    lives = 3
    score = 0

    background = Actor("background")
    player = Actor("player", (200, 580))
    enemies = []
    bullets = []
    bombs = []
```
### Draw your Actors
-----------------------------------------------------------------------------------------

Every Pygame game needs an `draw()` function, and it should draw all the
Actors we created above.

```python
    def draw():
        screen.clear()
        background.draw()
        player.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        for bomb in bombs:
            bomb.draw()
        draw_text()
```
### Move your Actors
-----------------------------------------------------------------------------------------

Every Pygame game needs an `update()` function to move the Actors, check
for collisions, etc.

``` python

    def update(delta):
        move_player()
        move_bullets()
        move_enemies()
        create_bombs()
        move_bombs()
        check_for_end_of_level()
```


### Define your functions
----------------------------------------------------------------------------------------------

Python cannot call a function that has not yet been defined. Therefore
we must at least provide empty, dummy versions of our functions that
don’t do anything so we can fill them in later. However Python cannot
define a completely empty function - it must contain at least one line.
Therefore we use the `pass` keyword to create a line that doesn’t do
anything.

```python

    def move_player():
        pass

    def move_enemies():
        pass

    def move_bullets():
        pass

    def create_bombs():
        pass

    def move_bombs():
        pass

    def check_for_end_of_level():
        pass

    def draw_text():
        pass
```
to the end of the file. Verify the game now runs and you can see the
player at the bottom of the screen. (He can’t move yet.)

### Create enemies
-------------------------------------------------------------------------------

Add this new function to the end of the program, and then call it
immediately. It uses a loop within a loop to create enemy Actors and put
them in the `enemies` list. The reason we put this in a function is we
will need to call it again at the start of each level.
```python
    def create_enemies():
        for x in range(0, 600, 60):
            for y in range(0, 200, 60):
                enemy = Actor("enemy", (x, y))
                enemy.vx = level * 2
                enemies.append(enemy)


    create_enemies()
```
### Move the player
--------------------------------------------------------------------------------

Replace the `move_player()` dummy function definition with this.
Remember **there can only be one function with a given name**. *There
cannot be two `move_player()` function definitions.*
```python
    def move_player():
        if keyboard.right:
            player.x = player.x + 5
        if keyboard.left:
            player.x = player.x - 5
        if player.x > WIDTH:
            player.x = WIDTH
        if player.x < 0:
            player.x = 0
```
### Move the enemies
---------------------------------------------------------------------------------

Replace the `move_enemies()` dummy function definition with this:
```python
    def move_enemies():
        global score
        for enemy in enemies:
            enemy.x = enemy.x + enemy.vx
            if enemy.x > WIDTH or enemy.x < 0:
                enemy.vx = -enemy.vx
                animate(enemy, duration=0.1, y=enemy.y + 60)
            for bullet in bullets:
                if bullet.colliderect(enemy):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score = score + 1
            if enemy.colliderect(player):
                exit()
```
### Draw text on the screen
----------------------------------------------------------------------------------------

Replace the `draw_text()` dummy function definition with this:
```python
    def draw_text():
        screen.draw.text("Level " + str(level), (0, 0), color="red")
        screen.draw.text("Score " + str(score), (100, 0), color="red")
        screen.draw.text("Lives " + str(lives), (200, 0), color="red")
```
### Player bullets
-------------------------------------------------------------------------------

Add this new function to the end of the program. Pygame will call it for
us automatically when a key is pressed.
```python
    def on_key_down(key):
        if key == keys.SPACE and len(bullets) < MAX_BULLETS:
            bullet = Actor("bullet", pos=(player.x, player.y))
            bullets.append(bullet)
```
Replace the `move_bullets()` dummy function definition with this:
```python
    def move_bullets():
        for bullet in bullets:
            bullet.y = bullet.y - 6
            if bullet.y < 0:
                bullets.remove(bullet)
```                

### Enemy bombs
-----------------------------------------------------------------------------

Replace the `create_bombs()` dummy function definition with this:

    def create_bombs():
        if random.randint(0, 100 - level * 6) == 0:
            enemy = random.choice(enemies)
            bomb = Actor("bomb", enemy.pos)
            bombs.append(bomb)

Replace the `move_bombs()` dummy function definition with this:
```python
    def move_bombs():
        global lives
        for bomb in bombs:
            bomb.y = bomb.y + 10
            if bomb.colliderect(player):
                bombs.remove(bomb)
                lives = lives - 1
                if lives == 0:
                    exit()
```                    

### Check for end of level
--------------------------------------------------------------

Replace the `check_for_end_of_level()` dummy function definition with
this:

```python
    def check_for_end_of_level():
        global level
        if len(enemies) == 0:
            level = level + 1
            create_enemies()
```