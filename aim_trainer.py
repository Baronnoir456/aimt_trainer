import pgzrun
import random



alien = Actor('alien')
trump = Actor('alien')

WIDTH = 1500
HEIGHT = 1250
HAPPENED = False
GRAVITY = 1
trump.dead = False
trump.vy = 0

def trump_position():
    x = random.randint(0, WIDTH - 10)
    y = 25
    trump.pos = x, y
#random_spawn_trump(HAPPENED)
def random_spawn_trump(HAPPENED):
    max_chance = 10
    chance = 0
    if HAPPENED == False:
        chance = random.randint(1, max_chance)
        trump_position()
        if chance == max_chance:
            HAPPENED = True
    else:
        trump.draw()
    return HAPPENED


def update():
    trump.y += GRAVITY
    if trump.bottom > HEIGHT:
        trump.top= 0


def draw():
    screen.clear()
    screen.fill((145, 150, 155))
    alien.draw()
    global HAPPENED
    HAPPENED = random_spawn_trump(HAPPENED)

    # trump.draw()


# -------die chancen sind zu:----------#
# 1/1800
# 1/3600


def on_mouse_down(pos):
    global HAPPENED
    if alien.collidepoint(pos):
        random_spawn()
    else:
        print("You missed me!")
    if trump.collidepoint(pos):
        HAPPENED=False



def random_spawn():
    x = random.randint(0, WIDTH - 10)
    y = random.randint(0, HEIGHT - 10)
    alien.pos = x, y


random_spawn()
pgzrun.go()

