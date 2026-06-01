import pgzrun

WIDTH = 400
HEIGHT = 500

def draw():
    screen.clear()
    screen.fill((135, 206, 235))

    screen.draw.filled_circle((200, 350), 80, "white")
    screen.draw.filled_circle((200, 220), 60, "white")
    screen.draw.filled_circle((200, 130), 40, "white")

    screen.draw.filled_circle((185, 120), 5, "black")
    screen.draw.filled_circle((215, 120), 5, "black")

    screen.draw.filled_circle((200, 135), 3, "orange")

    screen.draw.filled_circle((200, 200), 4, "black")
    screen.draw.filled_circle((200, 220), 4, "black")
    screen.draw.filled_circle((200, 240), 4, "black")

    screen.draw.filled_circle((200, 320), 5, "black")
    screen.draw.filled_circle((200, 350), 5, "black")
    screen.draw.filled_circle((200, 380), 5, "black")

pgzrun.go()