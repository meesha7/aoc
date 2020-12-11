# -*- coding: utf-8 -*-
"""

"""

import math

map_data = []

from functools import reduce  # Required in Python 3
import operator
def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def transform_line(line):
    return [True if x == '#' else False for x in line]

with open('input.txt', 'r') as fread:
    for line in fread:
        map_data.append(transform_line(line.strip()))

def traverse(map_data, step_row, step_col):
    num_trees = 0
    row = step_row
    col = step_col
    COLS = len(map_data[0])

    while row < len(map_data):
        point = map_data[row][col]

        if point:
            num_trees += 1

        # Step
        row += step_row
        col += step_col

        # Wrap
        if col >= COLS:
            col -= COLS

    return num_trees


STEPS = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1)
]

trees = [traverse(map_data, step_row, step_col) for (step_row, step_col) in STEPS]
print(trees)
print(prod(trees))
