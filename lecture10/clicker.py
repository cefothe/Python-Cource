import pgzrun
WIDTH = 500
HEIGHT = 500

is_moving = False
gg = []
for i in range(0,10):
    gg.append(Actor('bird', (i*30, i*30)))


def update():
    global is_moving
    if keyboard.v:
        is_moving = True
    if is_moving:
        for alien in gg:
            alien.x += 2
            if alien.x > WIDTH:
                alien.x = 0
    


def draw():
    screen.clear()
    for a in gg:
        a.draw()
def on_mouse_down(pos, button):
    gg.append(Actor('bird', pos))
pgzrun.go()