import pgzrun
import random

from pgzero.clock import clock

alien = Actor('alien')
trump = Actor('alien')

WIDTH = 2000
HEIGHT = 1450
HAPPENED = False
GRAVITY = 1
trump.dead = False
trump.vy = 0
hit = 0
Game_start = False
choosen_hit = 0
timer = 0
greating = True


def trump_position():
    x = random.randint(0, WIDTH - 10)
    y = 25
    trump.pos = x, y


def random_spawn_trump(HAPPENED):
    max_chance = 30
    chance = 0
    if HAPPENED == False:
        chance = random.randint(1, max_chance)
        trump_position()
    if chance == max_chance:
        HAPPENED = True
    else:
        trump.draw()

    return HAPPENED


def update(dt):
    global timer, Game_start
    trump.y += GRAVITY
    if trump.bottom > HEIGHT:
        trump.top = 0
    if hit != choosen_hit:
        timer += dt


def draw():
    global Game_start, choosen_hit, timer
    if Game_start == False:
        screen.fill((128, 130, 66))
        if greating == True:
            screen.draw.text("welcome to the SYNYX AIM TRAINER!!", fontsize=100, center=(WIDTH / 2, HEIGHT / 2))
        else:
            screen.draw.text("TO START PRESS S", fontsize=60, center=(WIDTH / 2, HEIGHT / 2))
            screen.draw.text("press P to add 10 hit's to the numbers of hit's you want to do", (400, 500), fontsize=30)
            screen.draw.text("press F to substract 10 hit's to the numbers of hit's you want to do", (400, 600),fontsize=30)
            screen.draw.text(str(choosen_hit), (25, 25), fontsize=30)
    else:
        screen.clear()
        screen.fill((135, 191, 86))
        screen.draw.text(str(hit), (25, 25), fontsize=30)
        screen.draw.text(str(choosen_hit), (25, 50), fontsize=30)
        screen.draw.text("seconds" + str(round(timer)), (WIDTH / 2 - 50, 25), color="white", fontsize=50,
                         align="center")
        if hit >= choosen_hit:
            screen.draw.text(
                "GAME IS FINSH!!YOUR SCORE is: {} \n YOUR TIME IS: {} SECONDS \n to replay press R".format(hit, round(
                    timer)), fontsize=40, center=(WIDTH / 2, HEIGHT / 2))
        else:
            alien.draw()
            global HAPPENED
            HAPPENED = random_spawn_trump(HAPPENED)


def on_key_down(key):
    global hit, Game_start, HAPPENED, choosen_hit, timer
    if key == keys.S:
        Game_start = True
    if key == keys.R:
        hit = 0
        timer = 0
        Game_start = False
        HAPPENED = False
    if key == keys.P:
        choosen_hit += 10
    if key == keys.F:
        if choosen_hit >= 0:
            choosen_hit -= 10


def on_mouse_down(pos):
    global HAPPENED, hit, greating
    if alien.collidepoint(pos):
        random_spawn()
        hit += 1
    if trump.collidepoint(pos):
        HAPPENED = False
        hit += 1
    greating = False


def random_spawn():
    x = random.randint(0, WIDTH - 10)
    y = random.randint(0, HEIGHT - 10)
    alien.pos = x, y


random_spawn()

pgzrun.go()
