import pgzrun
WIDTH = 500
HEIGHT = 500

aliens = []
for i in range(0,10):
    aliens.append(Actor('bird', (i*30, i*30)))

def draw():
    screen.clear()
    for alien in aliens:
        alien.draw()

def update():
    for alien in aliens:
        alien.x += 2
        if alien.x > WIDTH:
            alien.x = 0

def on_mouse_down(pos, button):
    aliens.append(Actor('bird', pos))
pgzrun.go()