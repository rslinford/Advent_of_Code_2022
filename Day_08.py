import re
import unittest

import numpy as np


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


class TreeGrid:
    grid: np.array

    def __init__(self, data):
        width = len(data[0])
        height = 0
        for _ in data:
            height += 1
        self.grid = np.zeros((height, width), dtype=np.uint)
        self.populate(data)

    def __repr__(self):
        rval = []
        for y in range(self.grid.shape[0]):
            if y > 0:
                rval.append('\n')
            for x in range(self.grid.shape[1]):
                rval.append(str(self.grid[y][x]))
        return ''.join(rval)

    def populate(self, data):
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                self.grid[y][x] = int(c)


def part_one(filename):
    data = read_puzzle_input(filename)
    tg = TreeGrid(data)
    print(tg)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_08_input.txt'
short_filename = 'Day_08_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one(short_filename))
        # self.assertEqual(-1, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(filename))

    def test_repr(self):
        data = read_puzzle_input(short_filename)
        tg = TreeGrid(data)
        self.assertEqual("30373\n"
                         "25512\n"
                         "65332\n"
                         "33549\n"
                         "35390", str(tg))
