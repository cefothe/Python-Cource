import pgzrun
from random import randint
import math

DIFFICULTY = 1
player = Actor("player", (400, 550))  # Load in the player Actor image


def draw():  # Pygame Zero draw function
    screen.blit('background', (0, 0))
    player.image = player.images[math.floor(player.status / 6)]
    player.draw()
    drawLasers()
    drawAliens()


def update():  # Pygame Zero update function
    global moveCounter, player
    if player.status < 30 and len(aliens) > 0:
        checkKeys()
        updateLasers()
        moveCounter += 1
        if moveCounter == moveDelay:
            moveCounter = 0
            updateAliens()
        if player.status > 0: player.status += 1
    else:
        if keyboard.RETURN: init()


def drawAliens():
    for a in range(len(aliens)): aliens[a].draw()


def drawLasers():
    for l in range(len(lasers)): lasers[l].draw()


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


def makeLaserActive():
    global player
    player.laserActive = 1


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


def checkLaserHit(l):
    global player
    if player.collidepoint((lasers[l].x, lasers[l].y)):
        player.status = 1
        lasers[l].status = 1


def checkPlayerLaserHit(l):
    global score

    for a in range(len(aliens)):
        if aliens[a].collidepoint((lasers[l].x, lasers[l].y)):
            lasers[l].status = 1
            aliens[a].status = 1
            score += 1000


def updateAliens():
    global moveSequence, lasers, moveDelay
    movex = movey = 0
    if moveSequence < 10 or moveSequence > 30: movex = -15
    if moveSequence == 10 or moveSequence == 30:
        movey = 50 + (10 * DIFFICULTY)
        moveDelay -= 1
    if moveSequence > 10 and moveSequence < 30: movex = 15
    for a in range(len(aliens)):
        animate(aliens[a], pos=(aliens[a].x + movex, aliens[a].y + movey), duration=0.5, tween='linear')
        if randint(0, 1) == 0:
            aliens[a].image = "alien1"
        else:
            aliens[a].image = "alien1b"
        if aliens[a].y > player.y and player.status == 0:
            player.status = 1
    moveSequence += 1
    if moveSequence == 40: moveSequence = 0


def init():
    global lasers, score, player, moveSequence, moveCounter, moveDelay
    initAliens()
    moveCounter = moveSequence = player.status = score = player.laserCountdown = 0
    lasers = []
    moveDelay = 30
    player.images = ["player", "explosion1", "explosion2", "explosion3", "explosion4", "explosion5"]
    player.laserActive = 1


def initAliens():
    global aliens
    aliens = []
    for a in range(18):
        aliens.append(Actor("alien1", (210 + (a % 6) * 80, 100 + (int(a / 6) * 64))))
        aliens[a].status = 0

init()
pgzrun.go()