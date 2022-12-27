import math
import re
import unittest
from dataclasses import dataclass


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


@dataclass
class Elf:
    x: int
    y: int


class Board:
    def __init__(self, elves):
        self.elves = elves

    def __repr__(self):
        rval = []
        min_x, max_x, min_y, max_y = self.survey_board_size()
        for y in range(min_y, max_y+1):
            if y > 0:
                rval.append('\n')
            for x in range(min_x, max_x+1):
                if self.tile_has_an_elf(x, y):
                    rval.append('#')
                else:
                    rval.append('.')
        return ''.join(rval)

    def survey_board_size(self):
        min_x, max_x, min_y, max_y = math.inf, -math.inf, math.inf, -math.inf
        for elf in self.elves:
            if elf.x < min_x:
                min_x =elf.x
            if elf.x > max_x:
                max_x = elf.x
            if elf.y < min_y:
                min_y = elf.y
            if elf.y > max_y:
                max_y = elf.y
        return min_x, max_x, min_y, max_y

    def tile_has_an_elf(self, x, y):
        for elf in self.elves:
            if elf.x == x and elf.y == y:
                return True
        return False


def parse_puzzle_input(data: list[str]):
    rval = []
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                rval.append(Elf(x, y))
    return rval


def part_one(filename):
    data = read_puzzle_input(filename)
    elves = parse_puzzle_input(data)
    board = Board(elves)
    print(board)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '23'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one(short_filename))
        self.assertEqual(-1, part_one(long_filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(long_filename))
