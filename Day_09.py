import re
import unittest

import numpy as np


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = set()
        self.add_current_to_history()

    def add_current_to_history(self):
        self.history.add((self.x, self.y))

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

    def is_at(self, p):
        return self.x == p[0] and self.y == p[1]

    def has_been_at(self, p):
        return p in self.history


class RopeSimulator():
    def __init__(self):
        self.start = Point(0, 0)
        self.head = Point(self.start.x, self.start.y)
        self.tail = Point(self.start.x, self.start.y)

    def __repr__(self):
        rval = []
        for y in range(-10, 10):
            if len(rval) > 0:
                rval.append('\n')
            for x in range(-10, 10):
                p = (x, y)
                if self.head.is_at(p):
                    rval.append('H')
                    continue
                if self.tail.is_at(p):
                    rval.append('T')
                    continue
                if self.start.is_at(p):
                    rval.append('s')
                    continue
                if self.tail.has_been_at(p):
                    rval.append('#')
                    continue
                rval.append('.')

        return ''.join(rval)

    def move_head_right(self):
        self.head.move_right()
        self.head.add_current_to_history()
        self.consider_tail()

    def move_head_left(self):
        self.head.move_left()
        self.head.add_current_to_history()
        self.consider_tail()

    def move_head_up(self):
        self.head.move_up()
        self.head.add_current_to_history()
        self.consider_tail()

    def move_head_down(self):
        self.head.move_down()
        self.head.add_current_to_history()
        self.consider_tail()

    def head_and_tail_delta(self):
        return self.head.x - self.tail.x, self.head.y - self.tail.y

    def head_and_tail_touch(self):
        delta_x, delta_y = self.head_and_tail_delta()
        return abs(delta_x) < 2 and abs(delta_y) < 2

    def consider_tail(self):
        if self.head_and_tail_touch():
            return
        delta_x, delta_y = self.head_and_tail_delta()
        # Non-diagonal
        if delta_x == 0:
            assert abs(delta_y) == 2
            if delta_y > 0:
                self.tail.move_down()
            else:
                self.tail.move_up()
            self.tail.add_current_to_history()
            return
        elif delta_y == 0:
            assert abs(delta_x) == 2
            if delta_x < 0:
                self.tail.move_left()
            else:
                self.tail.move_right()
            self.tail.add_current_to_history()
            return
        # Diagonal
        assert abs(delta_x) > 0
        assert abs(delta_y) > 0
        if delta_y > 0:
            self.tail.move_down()
        else:
            self.tail.move_up()
        if delta_x < 0:
            self.tail.move_left()
        else:
            self.tail.move_right()
        self.tail.add_current_to_history()
        return


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def part_one(filename):
    rs = RopeSimulator()
    data = read_puzzle_input(filename)
    for line in data:
        # print(rs)
        # print()
        # print(line)
        result = re.search('^(.) (\d+)$', line)
        direction = result.group(1)
        distance = int(result.group(2))
        for n in range(distance):
            match direction:
                case 'U':
                    rs.move_head_up()
                case 'D':
                    rs.move_head_down()
                case 'L':
                    rs.move_head_left()
                case 'R':
                    rs.move_head_right()
                case _:
                    raise ValueError(f'Expected U, D, L, or R but got {direction}')
    #         print(f'Turn {n}')
    #         print(rs)
    #         print()
    # print(rs)
    return len(rs.tail.history)


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_09_input.txt'
short_filename = 'Day_09_short_input.txt'
print(f'Answer part one: {part_one(filename)}')
print(f'Answer part two: {part_two(short_filename)}')

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(13, part_one(short_filename))
        self.assertEqual(5902, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(filename))
