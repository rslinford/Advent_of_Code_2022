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

    def is_visible_up(self, x_target, y_target):
        target_value = self.grid[y_target][x_target]
        for y in range(y_target - 1, -1, -1):
            if self.grid[y][x_target] >= target_value:
                return False
        return True

    def is_visible_down(self, x_target, y_target):
        target_value = self.grid[y_target][x_target]
        for y in range(y_target + 1, self.grid.shape[0], 1):
            if self.grid[y][x_target] >= target_value:
                return False
        return True

    def is_visible_right(self, x_target, y_target):
        target_value = self.grid[y_target][x_target]
        for x in range(x_target + 1, self.grid.shape[1], 1):
            if self.grid[y_target][x] >= target_value:
                return False
        return True

    def is_visible_left(self, x_target, y_target):
        target_value = self.grid[y_target][x_target]
        for x in range(x_target - 1, -1, -1):
            if self.grid[y_target][x] >= target_value:
                return False
        return True

    def is_visible(self, x_target, y_target):
        if y_target == 0 or x_target == 0:
            return True
        if y_target + 1 == self.grid.shape[0] or x_target + 1 == self.grid.shape[1]:
            return True
        # todo: look up/down left/right
        if self.is_visible_up(x_target, y_target):
            return True
        if self.is_visible_down(x_target, y_target):
            return True
        if self.is_visible_right(x_target, y_target):
            return True
        if self.is_visible_left(x_target, y_target):
            return True
        return False
    
    def count_visible(self):
        tally = 0 
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                if self.is_visible(x, y):
                    tally += 1
        return tally
                

    def value(self, x, y):
        return self.grid[y][x]


def part_one(filename):
    data = read_puzzle_input(filename)
    tg = TreeGrid(data)
    return tg.count_visible()


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_08_input.txt'
short_filename = 'Day_08_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(21, part_one(short_filename))
        self.assertEqual(-1, part_one(filename))

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

    def test_is_visible(self):
        data = read_puzzle_input(short_filename)
        tg = TreeGrid(data)
        self.assertEqual((5, 5), tg.grid.shape)
        self.assertEqual(True, tg.is_visible(0, 0))
        self.assertEqual(True, tg.is_visible(4, 4))
        self.assertEqual(True, tg.is_visible(4, 2))
        self.assertEqual(True, tg.is_visible(2, 4))
        self.assertEqual(5, tg.value(1, 1))
        self.assertEqual(True, tg.is_visible(1, 1))
        self.assertEqual(True, tg.is_visible(2, 1))
        self.assertEqual(False, tg.is_visible(3, 1))
        self.assertEqual(True, tg.is_visible(1, 2))
        self.assertEqual(False, tg.is_visible(2, 2))
        self.assertEqual(True, tg.is_visible(1, 4))
