import random
import pgzrun


WIDTH = 800
HEIGHT = 600
MAX_BULLETS = 3

level = 1
lives = 3
score = 0

background = Actor("background")
player = Actor("player", (200, 580))
enemies = []
bullets = []
bombs = []

def draw_text():
    screen.draw.text("Level " + str(level), (0, 0), color="red")
    screen.draw.text("Score " + str(score), (100, 0), color="red")
    screen.draw.text("Lives " + str(lives), (200, 0), color="red")

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

pgzrun.go()

