#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    ax = 0
    k = 0
    if wall_is_beneath() and wall_is_above():
        fill_cell()
    while not wall_is_on_the_right():
        move_right()
        if wall_is_beneath() and wall_is_above():
            fill_cell()
        if not wall_is_above() and wall_is_beneath():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    k += 1
                    mov("ax", k)
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
        if not wall_is_above() and not wall_is_beneath():
            break
if __name__ == '__main__':
    run_tasks()
