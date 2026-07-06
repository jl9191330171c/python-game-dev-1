import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

# Create the player
image = Actor("image")
image.pos = (100, 100)

# Create the pearl
pearl = Actor("pearl")
place = (200, 200)
pearl.pos = place


def draw():
    screen.blit("waterbg", (0, 0))

    pearl.draw()
    image.draw()

    screen.draw.text(
        "Score: " + str(score),
        topleft=(10, 10),
        fontsize=30,
        color="black"
    )

    if game_over:
        screen.fill("pink")
        screen.draw.text(
            "Time's up! Your Final Score: " + str(score),
            midtop=(WIDTH / 2, 10),
            fontsize=40,
            color="red"
        )


def place_pearl():
    pearl.x = randint(70, WIDTH - 70)
    pearl.y = randint(70, HEIGHT - 70)


def time_up():
    global game_over
    game_over = True


def update():
    global score

    if game_over:
        return

    if keyboard.left:
        image.x -= 2
    if keyboard.right:
        image.x += 2
    if keyboard.up:
        image.y -= 2
    if keyboard.down:
        image.y += 2

    # Keep player on screen
    image.x = max(0, min(WIDTH, image.x))
    image.y = max(0, min(HEIGHT, image.y))

    if image.colliderect(pearl):
        score += 10
        place_pearl()


place_pearl()
clock.schedule(time_up, 60.0)

pgzrun.go()