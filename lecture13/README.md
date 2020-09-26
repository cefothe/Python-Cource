# Space Invaders
## Aliens lasers
### Add laser into lasers array
Now is the time to make aliens laser to work. So they will try to kill our ship. 
On order to do that we need to update the following function `updateAliens`. When we change to 
`alien1b` we need to add random `randint(0, 10)` this will generate every time random number between
0 to 10. Then we can add the laser only when the return value is 0, this basically will not do a shot for every alien.
```python3
    if randint(0, 10) == 0:
       lasers.append(Actor("laser1", (aliens[a].x, aliens[a].y)))
       lasers[len(lasers) - 1].status = 0
       lasers[len(lasers) - 1].type = 0
``` 
### Moving alien lasers to the ship
Now we need move the aliens laser to ship in order to do that we need to update `updateLasers`.
First we need to check the laser type if the laser is from alien or from the ship. The laser type `0` is for aliens laser,
the laser type `1` is for the ship. Then we need to move the `y` position by `lasers[l].y += (2 * DIFFICULTY)`. 
Where the `DIFFICULTY` 
```python3
if lasers[l].type == 0:
    lasers[l].y += (2 * DIFFICULTY)
```
### Check if the laser is more than 600
Now we need to change the status of the laser if laser y go more than 600. Then in 
`listCleanup` will clean up the list. Let's add one more if clause and change the status to 
`1`
```python3
if lasers[l].y > 600: lasers[l].status = 1
```
### Check if the aliens laser hit the ship
Let's create a new function called `checkLaserHit` that accept `l` as a parameter. In that
function we need yo check if the player collidepoint the laser. Then we need to change the player status to `1`, 
and laser status to `1`
```python3
def checkLaserHit(l):
    global player
    if player.collidepoint((lasers[l].x, lasers[l].y)):
        player.status = 1
        lasers[l].status = 1
```
So we need to involve that function right after the previous function.
### Stop the game when aliens laser fit the ship
We want to stop the game when the aliens laser fit the the ship, in order to do that we need to add if clause in
`update` function. At the following as a first part of the the update function.
```python3
if player.status < 30 and len(aliens) > 0:
```
then move everything in that if. And the end you need to add following else clause
```python3
else:
    if keyboard.RETURN: exit();
```

### Add animation when laser fit the ship
The first step of the animation you need to add array list of the images  in `init` function.
```python3
player.images = ["player", "explosion1", "explosion2", "explosion3", "explosion4", "explosion5"]
```
When that part is done we need to create a animation. To do that you need to the following if in `update` function as inner if in `player.status < 30 and len(aliens) > 0:`

```python3
if player.status > 0:
    player.status += 1
```
Then in the `draw` function we need to do some math calculation.
```python3
player.image = player.images[math.floor(player.status / 6)]
```
### Add Game over message
Write after the animation finished we need to add `Game Over`  message on the screen.
In order to do that we need to create update the `draw`. We need to add if clause that check if the 
player status is equals or more than 30
```python3
if player.status >= 30:
    screen.draw.text("GAME OVER\nPress Enter to play again", center=(400, 300), owidth=0.5, ocolor=(255, 255, 255),
    color=(255, 64, 0), fontsize=60)
```

### Add a WIN message
When the number of aliens is equals to `0`
```python3
if len(aliens) == 0:
    screen.draw.text("YOU WON!\nPress Enter to play again", center=(400, 300), owidth=0.5, ocolor=(255, 255, 255),
    color=(255, 64, 0), fontsize=60)

```

# Create a functionality to plain the game without restarting the program
