# Space Invaders
## Moving the player ship
We need the player ship to respond to key presses, so we’ll check the Pygame Zero 
keyboard object to see if certain keys are currently pressed. Let’s make a new function to 
deal with these inputs. We will call the function checkKeys() and we’ll need to call it from our update() function.
In the checkKeys() function, we write if keyboard.left: and then if player.x > 40: player.x -= 5. 
We need to declare the player Actor object as global inside our checkKeys() function. 
We then write a similar piece of code to deal with the right arrow key; figure1.py 
shows how this all fits together.
```python3
import pgzrun

player = Actor("player", (400, 550)) # Load in the player Actor image

def draw(): # Pygame Zero draw function
    screen.blit('background', (0, 0))
    player.draw()

def update(): # Pygame Zero update function
    checkKeys()

def checkKeys():
    global player
    if keyboard.left:
        if player.x > 40: player.x -= 5
    if keyboard.right:
        if player.x < 760: player.x += 5

pgzrun.go()
```

## An alien concept
We now want to create a load of aliens in formation. 
You can have them in whatever format you want, but we’ll set up 
three rows of aliens with six on each row. We have an image called 
alien.png and can make an Actor for each alien that we will store in a 
list so that we can easily loop through the list to perform actions on them. 
When we create the alien Actors, we will use a bit of maths to set the initial x and y co-ordinates. 
It would be a good idea to define a function to set up the aliens – initAliens() – and because we will 
want to set up other elements too, we could define a function init(), from which we can call all the 
setup functions.
##  Doing the maths
To position our aliens and to create them as Actors, we can declare a list – aliens = [] – and then create a loop using for a in range(18):. 
In this loop, we need to create each Actor and then work out where their x and y co-ordinates will 
be to start. We can do this in the loop by writing: aliens.append(Actor("alien1", (210+(a % 6)80,100+(int(a/6)64)))). 
This may look a little daunting, but we can break it down by saying ‘x is 210 plus the remainder of dividing by 6 multiplied by 80’.

This will provide us with x co-ordinates starting at 210 and with a spacing of 80 between each. 
The y calculation is similar, but we use normal division, make it an integer, and multiply by 64.

## Believing the strangest things
After that slightly obscure title reference, we shall introduce the idea of the alien having a status. 
As we have seen in previous instalments, we can add extra data to our Actors, and in this case we will 
want to add a status variable to the alien after we have created it. We’ll explain how we are going to 
use this a bit later. Now it’s time to get the little guys on the screen and ready for action. 
We can write a simple function called drawAlien() and just loop through the alien list to draw them by 
writing: for a in range(len(aliens)): aliens[a].draw(). Call the drawAlien() function inside the draw() function.

## The aliens are coming!
We are going to create a function that we call inside our update() function that keeps track of 
what should happen to the aliens. We’ll call it updateAliens(). We don’t want to move the aliens every 
time the update cycle runs, so we’ll keep a counter called moveCounter and increment it each update(); 
then, if it gets to a certain value (moveDelay), we will zero the counter. 
If the counter is zero, we call updateAliens(). The updateAliens() function will calculate how much they need to 
move in the x and y directions to get them to go backwards 
and forwards across the screen and move down when they reach the edges.

```python3
 def updateAliens():
    global moveSequence, moveDelay
    movex = movey = 0
    if moveSequence < 10 or moveSequence > 30: movex = -15
    if moveSequence == 10 or moveSequence == 30:
        movey = 50
    if moveSequence >10 and moveSequence < 30: movex = 15
    for a in range(len(aliens)):
        animate(aliens[a], pos=(aliens[a].x + movex, aliens[a].y + movey), duration=0.5, tween='linear')
        if randint(0, 1) == 0:
            aliens[a].image = "alien1"
        else:
            aliens[a].image = "alien1b"
    moveSequence +=1
    if moveSequence == 40: moveSequence = 0
```

# Making the lasers work
You can see in figure4.py that we can create a laser from the player by adding a check for the 
SPACE key being pressed in our checkKeys() function. We will use the blue laser image called laser2.png. Once the new laser is in our list of lasers, 
it will be drawn to the screen if we call the drawLasers() function inside our draw() function. 
In our updateLasers() function we loop through the list of lasers and check which type it is. So if it is type 1 (player), we move the laser up the screen and then check to see if it hit anything. Notice the calls to a listCleanup() 
function at the bottom. We will come to this in a bit.

```python3
def checkKeys():
    global player, lasers
    if keyboard.left:
        if player.x > 40: player.x -= 5
    if keyboard.right:
        if player.x < 760: player.x += 5
    if keyboard.space:
        if player.laserActive == 1:
            player.laserActive = 0
            clock.schedule(makeLaserActive, 1.0)
            l = len(lasers)
            lasers.append(Actor("laser2", (player.x, player.y - 32)))
            lasers[l].status = 0
            lasers[l].type = 1
def drawLasers():
    for l in range(len(lasers)): lasers[l].draw()
def updateLasers():
    global lasers, aliens
    for l in range(len(lasers)):
        if lasers[l].type == 1:
            lasers[l].y -= 5
            checkPlayerLaserHit(l)
            if lasers[l].y < 10: lasers[l].status = 1
    lasers = listCleanup(lasers)
    aliens = listCleanup(aliens)
def listCleanup(l):
    newList = []
    for i in range(len(l)):
        if l[i].status == 0: newList.append(l[i])
    return newList
```
