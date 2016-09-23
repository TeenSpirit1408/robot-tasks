#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for i in range(1, 13):
        for j in range(1, 28):
            move_right()
            fill_cell()
        for k in range(1, 28):
            move_left()
        move_down()
    move_right()



if __name__ == '__main__':
    run_tasks()
