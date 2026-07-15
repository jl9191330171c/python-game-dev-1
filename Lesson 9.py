import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE="Satellites"

satellites = []
lines = []
next_satellite = 0

start_time = 0
total_time = 0
end_time = 0

number_of_satellite = 8

game_over = False

def create_satellites():
    global start_time
    for count in range(0, number_of_satellite):
        satellite = Actor("satellite")
        satellite.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        satellites.append(satellite)
    start_time = time()

def draw():
    global total_time

    screen.blit("backgroundgalaxy", (0,0))
    if game_over==True:
        screen.fill("blue")
        screen.draw.text("Game Over", center=(400,300),colour="red")
        return
    
def create_satellites():
    satellites.append(satellite)
    start_time = time()