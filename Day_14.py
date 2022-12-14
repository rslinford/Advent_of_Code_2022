import math

import numpy as np
import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data

class CaveMap:
    grid: np.chararray

    def __init__(self, min_x, max_x, min_y, max_y):
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        self.grid = np.chararray((height, width))
        self.grid[:] = '.'
        self.min_x = min_x
        self.min_y = min_y

    def __repr__(self):
        rval = []
        for y in range(self.grid.shape[0]):
            if y > 0:
                rval.append('\n')
            for x in range(self.grid.shape[1]):
                rval.append(self.grid[y][x].decode())
        return ''.join(rval)


def parse_points(data):
    """Parse lines of data into rows of x,y points"""
    rval = []
    for line in data:
        points = []
        rval.append(points)
        for p in line.split(' -> '):
            result = re.search('(\d+),(\d+)', p)
            x = int(result.group(1))
            y = int(result.group(2))
            points.append((x,y))

    return rval


def determine_xy_min_max(rows_of_points):
    min_x = math.inf
    min_y = math.inf
    max_x = -math.inf
    max_y = -math.inf
    for row in rows_of_points:
        for point in row:
            x, y = point[0], point[1]
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y
    return min_x, max_x, min_y, max_y


def part_one(filename):
    data = read_puzzle_input(filename)
    rows_of_points = parse_points(data)
    min_x, max_x, min_y, max_y = determine_xy_min_max(rows_of_points)
    cm = CaveMap(min_x, max_x, min_y, max_y)
    print(cm)
    print(rows_of_points)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_14_input.txt'
short_filename = 'Day_14_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one(short_filename))
        self.assertEqual(-1, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(filename))
