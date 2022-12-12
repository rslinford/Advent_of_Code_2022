import math
import unittest

import numpy as np
from colorama import Fore, Back, Style
import sys

sys.setrecursionlimit(5000)

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
        altitude1 = self.altitude_at(x1, y1)
        altitude2 = self.altitude_at(x2, y2)
        delta_altitude = altitude2 - altitude1
        return delta_altitude


class Hiker:
    def __init__(self, map: MapGrid):
        self.map = map
        # self.current_x, self.current_y = map.find_start()
        self.end_x, self.end_y = map.find_end()
        # self.step_tally = 0
        # self.bread_crumbs = set()
        self.shortest_step_tally = math.inf
        self.total_visits_counter = 0

    def render_map(self, current_x, current_y, bread_crumbs):
        rval = []
        for y in range(self.map.grid.shape[0]):
            if y > 0:
                rval.append('\n')
            for x in range(self.map.grid.shape[1]):
                c = self.map.grid[y][x].decode()
                if x == current_x and y == current_y:
                    rval.append(Fore.RED)
                    rval.append(c)
                    rval.append(Style.RESET_ALL)
                elif (x, y) in bread_crumbs:
                    rval.append(Fore.LIGHTCYAN_EX)
                    rval.append(c)
                    rval.append(Style.RESET_ALL)
                else:
                    rval.append(c)
        return ''.join(rval)

    def explore(self):
        x, y = self.map.find_start()
        self.explore_location(x, y, -1, set())
        return self.shortest_step_tally

    def explore_location(self, x, y, step_tally, bread_crumbs):
        if (x, y) in bread_crumbs:
            return
        bread_crumbs.add((x, y))
        step_tally += 1
        self.total_visits_counter += 1
        if self.total_visits_counter % 100000 == 0:
            print(f'\nStep {step_tally}')
            print(self.render_map(x, y, bread_crumbs))
        if x == self.end_x and y == self.end_y:
            # End Found
            print(f'Steps taken {step_tally}')
            if step_tally < self.shortest_step_tally:
                self.shortest_step_tally = step_tally
            return
        self.look_north_of(x, y, step_tally, bread_crumbs.copy())
        self.look_south_of(x, y, step_tally, bread_crumbs.copy())
        self.look_east_of(x, y, step_tally, bread_crumbs.copy())
        self.look_west_of(x, y, step_tally, bread_crumbs.copy())
        return

    def look_north_of(self, x, y, step_tally, bread_crumbs):
        if y <= 0:
            return
        delta = self.map.delta_altitude_between(x, y, x, y - 1)
        if delta <= 1:
            self.explore_location(x, y - 1, step_tally, bread_crumbs)

    def look_south_of(self, x, y, step_tally, bread_crumbs):
        if y >= self.map.grid.shape[0] - 1:
            return
        delta = self.map.delta_altitude_between(x, y, x, y + 1)
        if delta <= 1:
            self.explore_location(x, y + 1, step_tally, bread_crumbs)

    def look_east_of(self, x, y, step_tally, bread_crumbs):
        if x >= self.map.grid.shape[1] - 1:
            return
        delta = self.map.delta_altitude_between(x, y, x + 1, y)
        if delta <= 1:
            self.explore_location(x + 1, y, step_tally, bread_crumbs)

    def look_west_of(self, x, y, step_tally, bread_crumbs):
        if x <= 0:
            return
        delta = self.map.delta_altitude_between(x, y, x - 1, y)
        if delta <= 1:
            self.explore_location(x - 1, y, step_tally, bread_crumbs)


def part_one(filename):
    data = read_puzzle_input(filename)
    map = MapGrid(data)
    hiker = Hiker(map)
    return hiker.explore()


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


long_filename = 'Day_12_input.txt'
short_filename = 'Day_12_short_input.txt'
print(f'Answer part one: {part_one(long_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


# class Test(unittest.TestCase):
#     def test_part_one(self):
#         self.assertEqual(-1, part_one(short_filename))
#         self.assertEqual(-1, part_one(long_filename))
#
#     def test_part_two(self):
#         self.assertEqual(-1, part_two(short_filename))
#         self.assertEqual(-1, part_two(long_filename))


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
