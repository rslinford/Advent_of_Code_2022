import math
import re
import unittest
from dataclasses import dataclass
from enum import Enum, auto


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


@dataclass
class Elf:
    x: int
    y: int


class Dir(Enum):
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()
    EAST = auto()


class Board:
    def __init__(self, elves):
        self.elves: list[Elf] = elves
        self.search_order = [Dir.NORTH, Dir.SOUTH, Dir.WEST, Dir.EAST]

    def __repr__(self):
        rval = []
        min_x, max_x, min_y, max_y = self.survey_board_size()
        for y in range(min_y, max_y + 1):
            if y > 0:
                rval.append('\n')
            for x in range(min_x, max_x + 1):
                if self.tile_has_an_elf(x, y):
                    rval.append('#')
                else:
                    rval.append('.')
        return ''.join(rval)

    def rotate_search_order(self):
        self.search_order.append(self.search_order.pop(0))

    def survey_board_size(self):
        min_x, max_x, min_y, max_y = math.inf, -math.inf, math.inf, -math.inf
        for elf in self.elves:
            if elf.x < min_x:
                min_x = elf.x
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

    def spread_out(self):
        # Each elf considers whether it needs to move
        #   if no: propose nothing
        #   if yes: consider moving a directions according to current search order
        for elf in self.elves:
            if not self.elf_has_neighbor(elf):
                continue

    def elf_has_neighbor(self, elf):
        # North
        if self.tile_has_an_elf(elf.x, elf.y - 1):
            return True
        # North East
        if self.tile_has_an_elf(elf.x + 1, elf.y - 1):
            return True
        # East
        if self.tile_has_an_elf(elf.x + 1, elf.y):
            return True
        # South East
        if self.tile_has_an_elf(elf.x + 1, elf.y + 1):
            return True
        # South
        if self.tile_has_an_elf(elf.x, elf.y + 1):
            return True
        # South West
        if self.tile_has_an_elf(elf.x - 1, elf.y + 1):
            return True
        # West
        if self.tile_has_an_elf(elf.x - 1, elf.y):
            return True
        # North West
        if self.tile_has_an_elf(elf.x - 1, elf.y - 1):
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
    board.spread_out()

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


class TestBoard(unittest.TestCase):
    def test_elf_has_neighbor(self):
        data = read_puzzle_input(short_filename)
        elves = parse_puzzle_input(data)
        board = Board(elves)
        for elf in board.elves:
            self.assertTrue(board.elf_has_neighbor(elf))
        self.assertFalse(board.elf_has_neighbor(Elf(10, 10)))
        board.elves.append(Elf(11, 11))
        self.assertTrue(board.elf_has_neighbor(Elf(10, 10)))
        self.assertTrue(board.elf_has_neighbor(Elf(11, 10)))
        self.assertTrue(board.elf_has_neighbor(Elf(12, 10)))
        self.assertTrue(board.elf_has_neighbor(Elf(12, 11)))
        self.assertTrue(board.elf_has_neighbor(Elf(12, 12)))
        self.assertTrue(board.elf_has_neighbor(Elf(11, 12)))
        self.assertTrue(board.elf_has_neighbor(Elf(10, 12)))
        self.assertTrue(board.elf_has_neighbor(Elf(10, 11)))

