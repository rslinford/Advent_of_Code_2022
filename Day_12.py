import re
import unittest

import numpy as np


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


class MapGrid:
    grid: np.chararray

    def __init__(self, map_data):
        height = len(map_data)
        width = len(map_data[0])
        self.grid = np.chararray((height, width))
        for y, line in enumerate(map_data):
            for x, c in enumerate(line):
                self.grid[y][x] = c

    def __repr__(self):
        rval = []
        for y in range(self.grid.shape[0]):
            if y > 0:
                rval.append('\n')
            for x in range(self.grid.shape[1]):
                rval.append(str(self.grid[y][x])[2])
        return ''.join(rval)



def part_one(filename):
    data = read_puzzle_input(filename)
    grid = MapGrid(data)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_12_input.txt'
short_filename = 'Day_12_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one(short_filename))
        self.assertEqual(-1, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(filename))

class TestMapGrid(unittest.TestCase):
    def test_init(self):
        data = read_puzzle_input(short_filename)
        grid = MapGrid(data)
        self.assertEqual("Sabqponm\n"
                         "abcryxxl\n"
                         "accszExk\n"
                         "acctuvwj\n"
                         "abdefghi", str(grid))
