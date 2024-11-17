import pgzrun

import os

# Center the pygame window on the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 500
HEIGHT = 500
vx=4
vy=4
skibidihit=0
ball = Rect((150, 400), (20, 20))
batt = Rect((200,480),(60,20))
def draw():
    screen.clear()
    screen.draw.filled_rect(ball,"red")
    screen.draw.filled_rect(batt,"white")
    if ball.bottom > HEIGHT:
        screen.draw.text(
            "#GAMEOVERBRO",
            color = 'red',
            midtop=(250,200),
            fontsize=70
        )
    screen.draw.text(
        str(skibidihit),
        color='lime',
        midtop=(20,20),
        fontsize=70
    )
def update():
    global vx,vy, skibidihit
    ball.x+=vx
    ball.y+=vy
    if ball.right> WIDTH or ball.left < 0:
        vx= -vx
    if ball.top<0:
        vy= -vy 
    if ball.colliderect(batt):
        skibidihit=skibidihit+1
        vy= -(vy+int(skibidihit/4))
    if keyboard.right:
        batt.x+=4
    if keyboard.left:
        batt.x+=-4
 
    
pgzrun.go()