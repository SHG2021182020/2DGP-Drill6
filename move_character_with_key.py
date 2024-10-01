from random import random, randint

from pico2d import *

open_canvas()
bg = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')
mouse = load_image('hand_arrow.png')

def move():
    global x,y

    dx = ranx - x
    dy = rany - y
    # 거리 계산
    distance = (dx**2 + dy**2) ** 0.5

    if distance < 1:
        return

    speed = 10  # 이동 속도 설정
    x += speed * dx / distance
    y += speed * dy / distance

    pass

running = True
x = 800 // 2
y = 600 // 2
frame = 0
ranx = randint(100,700)
rany = randint(100,600)
dir = 1

while running:
    clear_canvas()
    bg.draw(400, 100)
    mouse.draw(ranx, rany, 50, 50)
    if ranx > x:
        dir = 1
    else:
        dir = -1

    if(dir == -1):
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, y, 100, 100)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    move()

    if -10 < x - ranx < 10 and -10 < y - rany < 10:
        ranx = randint(100,700)
        rany = randint(100,600)

    frame = (frame + 1) % 8

    # 화면 경계 체크 (화면 크기: 800x600)
    if x < 0:
        x = 0
    elif x > 800:
        x = 800

    if y < 0:
        y = 0
    elif y > 600:
        y = 600

    delay(0.05)

close_canvas()
