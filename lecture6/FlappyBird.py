import pgzrun

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

def update():
    barry_the_bird.y += barry_the_bird.speed
    if top_pipe.x < 0:
        top_pipe.x = WIDTH
    if bottom_pipe.x < 0:
        bottom_pipe.x = WIDTH
    if barry_the_bird.y > HEIGHT:
        reset()
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed

def reset():
    print ("Back to the start...")
    barry_the_bird.speed = 1
    barry_the_bird.center = (75, 350)
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)
def draw():
    screen.blit('background', (0, 0))
    barry_the_bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()

def on_mouse_down():
    print ('The mouse was clicked')
    barry_the_bird.y -= 50

barry_the_bird = Actor('bird1', (75, 350))
gap = 140
scroll_speed = -1
top_pipe = Actor('top', (300, 0))
bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))
print(top_pipe.width, top_pipe.height)
print(bottom_pipe.width, bottom_pipe.height)
barry_the_bird.speed = 1

pgzrun.go()