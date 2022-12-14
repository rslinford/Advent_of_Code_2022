import math
import re

import numpy as np


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


class CaveMap:
    grid: np.chararray

    def __init__(self, min_x, max_x, max_y):
        min_y = 0
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        self.grid = np.chararray((height, width))
        self.grid[:] = '.'
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.sand_x, self.sand_y = 0, 0

    def __repr__(self):
        rval = []
        rval.append(f'({self.min_x}, {self.min_y})\n')
        for y in range(self.grid.shape[0]):
            if y > 0:
                rval.append('\n')
            for x in range(self.grid.shape[1]):
                if x + self.min_x == 500 and y + self.min_y == 0:
                    rval.append('+')
                else:
                    rval.append(self.grid[y][x].decode())
        return ''.join(rval)

    def draw_rock_lines(self, rows_of_points):
        for row in rows_of_points:
            for i in range(len(row) - 1):
                x1, y1 = row[i][0], row[i][1]
                x2, y2 = row[i + 1][0], row[i + 1][1]
                if x1 == x2:
                    if y1 - y2 > 0:
                        y1, y2 = y2, y1
                    for y in range(y1, y2 + 1):
                        self.draw_char(x1, y, '#')
                else:
                    assert (y1 == y2)
                    if x1 - x2 > 0:
                        x1, x2 = x2, x1
                    for x in range(x1, x2 + 1):
                        self.grid[y1 - self.min_y][x - self.min_x] = '#'

    def draw_char(self, x, y, c):
        self.grid[y - self.min_y][x - self.min_x] = c

    def char_at(self, x, y):
        return self.grid[y - self.min_y][x - self.min_x].decode()

    def fall_down(self):
        fallen = False
        while True:
            if self.char_at(self.sand_x, self.sand_y + 1) == '.':
                self.sand_y += 1
                fallen = True
            else:
                break
        return fallen

    def fall_down_and_left(self):
        if self.char_at(self.sand_x - 1, self.sand_y + 1) == '.':
            self.sand_x -= 1
            self.sand_y += 1
            return True
        else:
            return False

    def fall_down_and_right(self):
        if self.char_at(self.sand_x + 1, self.sand_y + 1) == '.':
            self.sand_x += 1
            self.sand_y += 1
            return True
        else:
            return False

    def simulate_sand(self):
        self.sand_x, self.sand_y = 500, 0
        while True:
            self.fall_down()
            if not self.fall_down_and_left():
                if not self.fall_down_and_right():
                    break
        self.draw_char(self.sand_x, self.sand_y, 'o')


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
            points.append((x, y))

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
    cm = CaveMap(min_x, max_x, max_y)
    cm.draw_rock_lines(rows_of_points)
    tally = 0
    while True:
        try:
            cm.simulate_sand()
            tally += 1
        except IndexError:
            break
        print(f'Sand {tally}\n{cm}')
    return tally


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_14_input.txt'
short_filename = 'Day_14_short_input.txt'
print(f'Answer part one: {part_one(filename)}')
print(f'Answer part two: {part_two(short_filename)}')

# class Test(unittest.TestCase):
#     def test_part_one(self):
#         self.assertEqual(-1, part_one(short_filename))
#         self.assertEqual(-1, part_one(filename))
#
#     def test_part_two(self):
#         self.assertEqual(-1, part_two(short_filename))
#         self.assertEqual(-1, part_two(filename))
