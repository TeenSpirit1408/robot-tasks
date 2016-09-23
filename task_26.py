#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    for i in range(4):
        for j in range(9):
            move_right()
            fill_cell()
            for k in range(2):
                move_down()
                fill_cell()
            move_left()
            move_up()
            fill_cell()
            for k in range(2):
                move_right()
                fill_cell()
            move_right(2)
            move_up()
        move_right()
        fill_cell()
        for k in range(2):
            move_down()
            fill_cell()
        move_left()
        move_up()
        fill_cell()
        for k in range(2):
            move_right()
            fill_cell()
        move_left(38)
        move_down(3)
    for j in range(9):
        move_right()
        fill_cell()
        for k in range(2):
            move_down()
            fill_cell()
        move_left()
        move_up()
        fill_cell()
        for k in range(2):
            move_right()
            fill_cell()
        move_right(2)
        move_up()
    move_right()
    fill_cell()
    for k in range(2):
        move_down()
        fill_cell()
    move_left()
    move_up()
    fill_cell()
    for k in range(2):
        move_right()
        fill_cell()
    move_left(38)
    move_up(1)








if __name__ == '__main__':
    run_tasks()
