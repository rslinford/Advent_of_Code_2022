import math
import unittest
from dataclasses import dataclass
from enum import Enum, auto


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


class Dir(Enum):
    NONE = auto()
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()
    EAST = auto()


@dataclass
class Elf:
    x: int
    y: int
    proposal = None

    def propose(self, direction: Dir):
        match direction:
            case Dir.NORTH:
                self.proposal = (self.x, self.y - 1)
            case Dir.SOUTH:
                self.proposal = (self.x, self.y + 1)
            case Dir.WEST:
                self.proposal = (self.x - 1, self.y)
            case Dir.EAST:
                self.proposal = (self.x + 1, self.y)
            case Dir.NONE:
                self.proposal = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def move(self):
        self.x = self.proposal[0]
        self.y = self.proposal[1]


class Board:
    def __init__(self, elves):
        self.elves: list[Elf] = elves
        self.search_order = [Dir.NORTH, Dir.SOUTH, Dir.WEST, Dir.EAST]

    def __repr__(self):
        rval = []
        min_x, max_x, min_y, max_y = self.survey_board_size()
        for y in range(min_y, max_y + 1):
            if y > min_y:
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
        #   if yes: consider moving a direction according to current search order
        #
        # Proposal Stage
        for elf in self.elves:
            elf.propose(Dir.NONE)
            # Do not make a proposal if no neighbor found
            if not self.elf_has_neighbor(elf):
                continue
            # Look ahead for the first way that's clear
            for direction in self.search_order:
                if self.clear_ahead(elf, direction):
                    # The way is clear. Propose direction.
                    elf.propose(direction)
                    break
        # Move Stage
        for elf1 in self.elves:
            conflict_found = False
            for elf2 in self.elves:
                # Elf doesn't conflict with itself
                if elf1 == elf2:
                    continue
                # Two elves conflict if they proposed the same destination
                if elf1.proposal == elf2.proposal:
                    conflict_found = True
                    break
            if conflict_found:
                continue
            # No conflict. Perform move.
            elf1.move()

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

    def clear_ahead(self, elf, direction):
        match direction:
            case Dir.NORTH:
                if self.tile_has_an_elf(elf.x - 1, elf.y - 1) or \
                        self.tile_has_an_elf(elf.x, elf.y - 1) or \
                        self.tile_has_an_elf(elf.x + 1, elf.y - 1):
                    return False
            case Dir.SOUTH:
                if self.tile_has_an_elf(elf.x - 1, elf.y + 1) or \
                        self.tile_has_an_elf(elf.x, elf.y + 1) or \
                        self.tile_has_an_elf(elf.x + 1, elf.y + 1):
                    return False
            case Dir.WEST:
                if self.tile_has_an_elf(elf.x - 1, elf.y - 1) or \
                        self.tile_has_an_elf(elf.x - 1, elf.y) or \
                        self.tile_has_an_elf(elf.x - 1, elf.y + 1):
                    return False
            case Dir.EAST:
                if self.tile_has_an_elf(elf.x + 1, elf.y - 1) or \
                        self.tile_has_an_elf(elf.x + 1, elf.y) or \
                        self.tile_has_an_elf(elf.x + 1, elf.y + 1):
                    return False
        return True


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
    print('Initial State')
    print(board)
    for round in range(1, 11):
        board.spread_out()
        board.rotate_search_order()
        print(f'End Round {round}')
        print(board)

    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '23'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
short_filename_two = f'Day_{day_of_month}_short_input_two.txt'
print(f'Answer part one: {part_one(short_filename_two)}')
print(f'Answer part two: {part_two(short_filename)}')


# class Test(unittest.TestCase):
#     def test_part_one(self):
#         self.assertEqual(-1, part_one(short_filename))
#         self.assertEqual(-1, part_one(long_filename))
#
#     def test_part_two(self):
#         self.assertEqual(-1, part_two(short_filename))
#         self.assertEqual(-1, part_two(long_filename))


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
