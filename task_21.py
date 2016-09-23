#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    j = 1
    k = 2
    move_down()
    for i in range(1, 14):
        for j in range(1, k):
            move_right()
            fill_cell()
        for j in range(1, k):
            move_left()
        k += 1
        move_down()
    move_right()


if __name__ == '__main__':
    run_tasks()
