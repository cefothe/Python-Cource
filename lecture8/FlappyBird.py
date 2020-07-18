import pgzrun
import random

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

def update():
    barry_the_bird.speed += gravity
    barry_the_bird.y += barry_the_bird.speed
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed
    if top_pipe.right < barry_the_bird.x:
        barry_the_bird.score = top_pipe.pair_number
    if top_pipe.right < 0:
        offset = random.randint(140,300)
        gap = random.randint(140,300)
        print(gap)
        top_pipe.midleft = (WIDTH, offset)
        bottom_pipe.midleft = (WIDTH, offset + top_pipe.height + gap)
        top_pipe.pair_number += 1
    if barry_the_bird.y > HEIGHT or barry_the_bird.y < 0:
        reset()
    if (barry_the_bird.colliderect(top_pipe) or barry_the_bird.colliderect(bottom_pipe)):
        hit_pipe()
    # Animation
    if barry_the_bird.alive:
        if barry_the_bird.speed > 0:
            barry_the_bird.image = "bird1"
        else:
            barry_the_bird.image = "bird2"

def draw():
    screen.blit('background', (0, 0))
    barry_the_bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()
    screen.draw.text(
        str(barry_the_bird.score),
        color='white',
        midtop=(20, 10),
        fontsize=70,
    )

def on_mouse_down():
    if (barry_the_bird.alive):
        barry_the_bird.speed = -6.5

def reset():
    print ("Back to the start...")
    barry_the_bird.score = 0
    top_pipe.pair_number = 1
    barry_the_bird.speed = 1
    barry_the_bird.center = (75, 100)
    barry_the_bird.image = "bird1"
    barry_the_bird.alive = True
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)

def hit_pipe():
    print ("Hit pipe!")
    barry_the_bird.image = "birddead"
    barry_the_bird.alive = False

barry_the_bird = Actor('bird1')
gap = 300
top_pipe = Actor('top')
bottom_pipe = Actor('bottom')
scroll_speed = -1
gravity = 0.3
barry_the_bird.score = 0
best_result = 0
reset()


pgzrun.go()