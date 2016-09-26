#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    k = 0
    a = 1
    b = 0
    while not wall_is_on_the_right():
        k += 1
        move_right()
    while not wall_is_on_the_left():
        move_left()


    while b != (k//2):
        move_right()
        for i in range(k - a):
            fill_cell()
            move_right()


        move_down()
        for i in range(k - a):
            fill_cell()
            move_down()


        move_left()
        for i in range(k - a):
            fill_cell()
            move_left()


        move_up()
        for i in range(k - a):
            fill_cell()
            move_up()
        b += 1
        move_down()
        move_right()
        a += 2


    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()















if __name__ == '__main__':
    run_tasks()
