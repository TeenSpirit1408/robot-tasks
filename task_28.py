#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    l = 0
    while l < 5:
        move_right()
        if cell_is_filled():
            l += 1


if __name__ == '__main__':
    run_tasks()
