#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    k = 1
    move_right()
    fill_cell()
    while not wall_is_on_the_right():
        for i in range(k):
            if wall_is_on_the_right():
                break
            move_right()
        if wall_is_on_the_right():
            break
        fill_cell()
        k += 1



if __name__ == '__main__':
    run_tasks()
