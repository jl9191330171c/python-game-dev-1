import pgzrun
from random import randint

TITLE = "Kill the ALIEN."

WIDTH = 500
HEIGHT = 500
score = 0

message = ""

alien = Actor('alien')



def draw():
    screen.clear()
    screen.fill(color = (128, 0, 0))
    alien.draw()
    if score == 30:
        screen.draw.text("NOOOOO! I'm DEAD because of YOU :()", (0, 250), fontsize=30)
    screen.draw.text(message, center = (270, 30), fontsize= 30)
    screen.draw.text("Score:"+str(score), (30,50), fontsize=25)

def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, HEIGHT-50)

def on_mouse_down(pos):
    global message,score
    if alien.collidepoint(pos):
        message = "AAHG! You shot me!"
        place_alien()
        score=score+1
    else:
        message = "Heh! You're NEVER going to kill me like this :)"
        score = 0



place_alien()
pgzrun.go()