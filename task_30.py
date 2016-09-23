#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    k = 0
    a = 1
    while not wall_is_on_the_right():
        k += 1
        move_right()
    while not wall_is_on_the_left():
        move_left()
    for i in range(k-a):
        move_right()
        fill_cell()
    a += 2
    while not wall_is_on_the_left():
        move_left()
    move_down()
    move_right(a-2)
    for i in range(k-a):
        move_right()
        fill_cell()
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_right():
        move_right()



    a = 1
    for i in range(k-a):
        move_down()
        fill_cell()
    a += 2
    while not wall_is_above():
        move_up()
    move_left()
    move_down(a-2)
    for i in range(k-a):
        move_down()
        fill_cell()
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_right():
        move_right()



    a = 1
    for i in range(k-a):
        move_left()
        fill_cell()
    a += 2
    while not wall_is_on_the_right():
        move_right()
    move_up()
    move_left(a-2)
    for i in range(k-a):
        move_left()
        fill_cell()
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()



    a = 1
    for i in range(k-a):
        move_up()
        fill_cell()
    a += 2
    while not wall_is_beneath():
        move_down()
    move_right()
    move_up(a-2)
    for i in range(k-a):
        move_up()
        fill_cell()
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()










if __name__ == '__main__':
    run_tasks()
