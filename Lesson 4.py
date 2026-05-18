import pgzrun

WIDTH=500
HEIGHT=400

def draw():
    #starting corner
    corner1=(20,30)
    #ending corner
    corner2=(400,200)
    #making rectangle
    rect = Rect(corner1,corner2)
    screen.draw.filled_rect(rect,(0,255,255))
    screen.draw.rect(rect,(255,0,4))






pgzrun.go()