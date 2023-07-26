import pygame
from datetime import datetime

pygame.init()
scr = pygame.display.set_mode((1000,500))


def vert(start_x, start_y):
    pygame.draw.polygon(scr, (255, 0, 0),
                      [[start_x-5, start_y+10], [start_x, start_y], [start_x+5, start_y], [start_x+10, start_y+10],
                       [start_x+10, start_y+100], [start_x+5, start_y+110], [start_x, start_y+110], [start_x-5, start_y+100]])


def horiz(start_x, start_y):
    pygame.draw.polygon(scr, (255, 0, 0),
                      [[start_x+10, start_y-5], [start_x, start_y], [start_x, start_y+5], [start_x+10, start_y+10],
                       [start_x+85, start_y+10], [start_x+95, start_y+5], [start_x+95, start_y], [start_x+85, start_y-5]])


def zero(def_x, def_y):
    vert(def_x, def_y)
    horiz(def_x + 10, def_y - 10)
    vert(def_x + 110, def_y)
    vert(def_x, def_y + 125)
    vert(def_x + 110, def_y + 125)
    horiz(def_x + 10, def_y + 240)


def one(def_x, def_y):
    vert(def_x + 110, def_y)
    vert(def_x + 110, def_y + 125)


def two(def_x, def_y):
    horiz(def_x + 10, def_y - 10)
    vert(def_x + 110, def_y)
    horiz(def_x + 10, def_y + 115)
    vert(def_x, def_y + 125)
    horiz(def_x + 10, def_y + 240)


def three(def_x, def_y):
    horiz(def_x + 10, def_y - 10)
    vert(def_x + 110, def_y)
    horiz(def_x + 10, def_y + 115)
    vert(def_x + 110, def_y + 125)
    horiz(def_x + 10, def_y + 240)


def four(def_x, def_y):
    vert(def_x, def_y)
    vert(def_x + 110, def_y)
    horiz(def_x + 10, def_y + 115)
    vert(def_x + 110, def_y + 125)


def five(def_x, def_y):
    vert(def_x, def_y)
    horiz(def_x + 10, def_y - 10)
    horiz(def_x + 10, def_y + 115)
    vert(def_x + 110, def_y + 125)
    horiz(def_x + 10, def_y + 240)


def six(def_x, def_y):
    vert(def_x, def_y)
    horiz(def_x + 10, def_y - 10)
    horiz(def_x + 10, def_y + 115)
    vert(def_x, def_y + 125)
    vert(def_x + 110, def_y + 125)
    horiz(def_x + 10, def_y + 240)


def seven(def_x, def_y):
    horiz(def_x + 10, def_y - 10)
    vert(def_x + 110, def_y)
    vert(def_x + 110, def_y + 125)


def eight(def_x, def_y):
    vert(def_x, def_y)
    horiz(def_x+10, def_y-10)
    vert(def_x+110, def_y)
    horiz(def_x+10, def_y+115)
    vert(def_x, def_y+125)
    vert(def_x+110, def_y+125)
    horiz(def_x+10, def_y+240)


def nine(def_x, def_y):
    vert(def_x, def_y)
    horiz(def_x + 10, def_y - 10)
    vert(def_x + 110, def_y)
    horiz(def_x + 10, def_y + 115)
    vert(def_x + 110, def_y + 125)
    horiz(def_x + 10, def_y + 240)

def trans(num, x, y):
    if int(num) == 0:
        return zero(x, y)
    elif int(num)==1:
        return one(x, y)
    elif int(num)==2:
        return two(x, y)
    elif int(num)==3:
        return three(x, y)
    elif int(num)==4:
        return four(x, y)
    elif int(num)==5:
        return five(x, y)
    elif int(num)==6:
        return six(x, y)
    elif int(num)==7:
        return seven(x, y)
    elif int(num)==8:
        return eight(x, y)
    elif int(num)==9:
        return nine(x, y)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    scr.fill((0, 0, 0))
    pygame.draw.rect(scr, (0, 0, 0), (0, 0, 1000, 166))
    pygame.draw.rect(scr, (255, 255, 0), (0, 166, 1000, 166))
    pygame.draw.rect(scr, (255, 255, 255), (0, 332, 1000, 166))
    trans(str(datetime.now())[11], 85, 110)
    trans(str(datetime.now())[12], 215, 110)
    pygame.draw.circle(scr, (255, 0, 0), (358, 170), 10)
    pygame.draw.circle(scr, (255, 0, 0), (358, 290), 10)
    trans(str(datetime.now())[14], 385, 110)
    trans(str(datetime.now())[15], 515, 110)
    pygame.draw.circle(scr, (255, 0, 0), (658, 170), 10)
    pygame.draw.circle(scr, (255, 0, 0), (658, 290), 10)
    trans(str(datetime.now())[17], 685, 110)
    trans(str(datetime.now())[18], 815, 110)

    pygame.display.flip()
