# Chase game
In this lecture we will build a complete chase game together, step by step. The Python we will use is very simple:
 just conditionals and loops.
 
## Moving Actor over a background
You need to use the `player` and the `background` image provided in image folder. 
And then you need to move the player with keyboards (left, right, up, down arrows).
- [ ] Let's first create a windows first size 600X600
- [ ] Draw the player and the background (you need to define draw function and do that their)
- [ ] Move the player with keyboards (you need to define update function and perform those operation their)
- [ ] Run the program and move the Actor around with the keys.

## Screen wrap-around
One problem you will soon find with the program is that you can move off the edge of the screen and 
get lost. One way to solve this would be to stop movement at the screen edges. Instead we going to make 
the player teleport to the opposite edge when he leaves the screen. Add this code to the end of the program, 
and make sure it is indented so that it becomes part of the update() function.

```python3
if player.x > WIDTH:
   player.x = 0
if player.x < 0:
   player.x = WIDTH
if player.y < 0:
   player.y = HEIGHT
if player.y > HEIGHT:
   player.y = 0
```

## Enemy chases the player
Let’s add an enemy to chase the player. At the top of the program, 
create a variable to store the enemy Actor:
```python3
enemy = Actor("alien")
```
- [ ] Update draw function to show enemy
- [ ] Ad the end of update function apply following lines
```python3
   if enemy.x < player.x:
        enemy.x = enemy.x + 1
    if enemy.x > player.x:
        enemy.x = enemy.x - 1
    if enemy.y < player.y:
        enemy.y = enemy.y + 1
    if enemy.y > player.y:
        enemy.y = enemy.y - 1
    if player.colliderect(enemy):
        exit()    
```

## Collecting items
Use image file called coin.png that in saved in image folder.  
- [ ] Create a Actor with that image
- [ ] Show the actor on the screen
- [ ] Create variable for score 
- [ ] In update function add a check if our player have collisions with coin actor, 
and increase the score if that happen (use keyword global)
- [ ] Move the coin in random position on the screen

## Showing the score on the screen
At the end of the draw() function (but still indented so part of the function), draw a title on the screen:
```python3
screen.draw.text("My game", (200,0), color='red')
```
The draw.text() function is not like print() - it can only print strings of text, not numbers. Therefore we must convert the score into a string. 
Add these lines to the end of the draw() function:
```python3
    score_string = str(score)
    screen.draw.text(score_string, (0,0), color='green')
```
## Timer
Add a variable at the top of the program (but preferably after any import statements) 
to store the number of seconds of time remaining in the game:

```python3 
timer = 20
```
Pygame Zero calls our update() function many times per second. We can ask it to tell us how much time has passed by adding a parameter to the function, delta. 
We then subtract this from the remaining time. Modify update() so the first lines look like this:
```python3
def update(delta):
    global score, timer
    timer = timer - delta
    if timer <= 0:
         exit()
```