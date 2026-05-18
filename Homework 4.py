import pgzrun

WIDTH = 800
HEIGHT = 600

def draw():
    screen.fill("white")
    
    #circles
    screen.draw.filled_circle((200, 200), 50, "red")
    screen.draw.filled_circle((400, 200), 75, "blue")
    
    #lines
    screen.draw.line((100, 400), (700, 400), "black")
    screen.draw.line((100, 500), (700, 300), "green")


pgzrun.go()