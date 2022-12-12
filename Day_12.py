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
                rval.append(self.grid[y][x].decode())
        return ''.join(rval)

    def char_at(self, x, y):
        return self.grid[y][x].decode()

    def altitude_at(self, x, y):
        c = self.char_at(x, y)
        if c == 'S':
            c = 'a'
        elif c == 'E':
            c = 'z'
        return ord(c) - ord('a')

    def find_start(self):
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                if self.char_at(x, y) == 'S':
                    return (x, y)

    def find_end(self):
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                if self.char_at(x, y) == 'E':
                    return (x, y)

    def delta_altitude_between(self, x1, y1, x2, y2):
        altitude1 = self.map.altitude_at(x1, y1)
        altitude2 = self.map.altitude_at(x2, y2)
        delta_altitude = altitude2 - altitude1
        return delta_altitude


class Hiker:
    def __init__(self, map: MapGrid):
        self.map = map
        # self.current_x, self.current_y = map.find_start()
        self.end_x, self.end_y = map.find_end()
        self.step_tally = 0
        self.bread_crumbs = set()

    def explore(self):
        x, y = self.map.find_start()
        return self.explore_location(x, y)

    def explore_location(self, x, y):
        if (x, y) in self.bread_crumbs:
            return self.step_tally
        self.bread_crumbs.add((x, y))
        self.step_tally += 1
        if x == self.end_x and y == self.end_y:
            # End Found. todo: collect possible solutions here
            return self.step_tally
        self.look_north_of(x, y)
        self.look_south_of(x, y)
        self.look_east_of(x, y)
        self.look_west_of(x, y)
        return self.step_tally

    def look_north_of(self, x, y):
        if y <= 0:
            return
        delta = self.map.delta_altitude_between(x, y, x, y - 1)
        if delta <= 1:
            self.explore_location(x, y - 1)

    def look_south_of(self, x, y):
        if y >= self.map.grid.shape[0] - 1:
            return
        delta = self.map.delta_altitude_between(x, y, x, y + 1)
        if delta <= 1:
            self.explore_location(x, y + 1)

    def look_east_of(self, x, y):
        if x >= self.map.grid.shape[1] - 1:
            return
        delta = self.map.delta_altitude_between(x, y, x + 1, y)
        if delta <= 1:
            self.explore_location(x + 1, y)

    def look_west_of(self, x, y):
        if x <= 0:
            return
        delta = self.map.delta_altitude_between(x, y, x - 1, y)
        if delta <= 1:
            self.explore_location(x - 1, y)


def part_one(filename):
    data = read_puzzle_input(filename)
    grid = MapGrid(data)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


long_filename = 'Day_12_input.txt'
short_filename = 'Day_12_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one(short_filename))
        self.assertEqual(-1, part_one(long_filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(long_filename))


class TestMapGrid(unittest.TestCase):
    def test_init(self):
        data = read_puzzle_input(short_filename)
        map = MapGrid(data)
        self.assertEqual("Sabqponm\n"
                         "abcryxxl\n"
                         "accszExk\n"
                         "acctuvwj\n"
                         "abdefghi", str(map))
        self.assertEqual('S', str(map.grid[0][0])[2])
        self.assertEqual('S', map.char_at(0, 0))
        self.assertEqual('i', map.char_at(7, 4))

    def test_find_start(self):
        data = read_puzzle_input(short_filename)
        map = MapGrid(data)
        self.assertEqual((0, 0), map.find_start())

    def test_find_end(self):
        data = read_puzzle_input(short_filename)
        map = MapGrid(data)
        self.assertEqual((5, 2), map.find_end())

    def test_altitude_at(self):
        data = read_puzzle_input(short_filename)
        map = MapGrid(data)
        self.assertEqual(0, map.altitude_at(0, 0))
        self.assertEqual(25, map.altitude_at(5, 2))
        self.assertEqual(2, map.altitude_at(1, 3))


class TestHiker(unittest.TestCase):
    def test_init(self):
        data = read_puzzle_input(short_filename)
        map = MapGrid(data)
        hiker = Hiker(map)
        # self.assertEqual(0, hiker.current_x)
        # self.assertEqual(0, hiker.current_y)
        self.assertEqual(5, hiker.end_x)
        self.assertEqual(2, hiker.end_y)
