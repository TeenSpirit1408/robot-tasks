#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    k = 0
    while not wall_is_on_the_left() or not wall_is_on_the_right():
        while not wall_is_on_the_left():
            move_left()
            if not wall_is_beneath():
                move_down()
                k -= 1
        k += 1
        while not wall_is_on_the_right():
            move_right()
            if not wall_is_beneath():
                move_down()
                k -= 1
        k += 1
        if k > 0:
            break
    while not wall_is_on_the_left():
        move_left()




if __name__ == '__main__':
    run_tasks()
