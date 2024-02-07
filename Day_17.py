import unittest
from enum import Enum, auto
from typing import List

"""
Rocks take one of 5 shapes:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data


def parse_data(data: str):
    return list(data)


class Dir(Enum):
    LEFT = auto()
    RIGHT = auto()


class GasJets:
    def __init__(self, gas_jets: List[str]):
        self.gas_jets = gas_jets
        self.next = 0

    def get(self):
        c = self.gas_jets[self.next % len(self.gas_jets)]
        self.next += 1
        match c:
            case '<':
                return Dir.LEFT
            case '>':
                return Dir.RIGHT
            case _:
                assert False


class Space:
    def __init__(self):
        self.debug = False
        self.settled_rocks = set()
        self.falling_rocks = set()
        self.spawn_count = 0

    def print(self):
        if not self.debug:
            return
        max_y = self.find_max_y()
        for y in range(max_y, -1, -1):
            print('|', end='')
            for x in range(7):
                if (x, y) in self.settled_rocks:
                    print('#', end='')
                elif (x, y) in self.falling_rocks:
                    print('@', end='')
                else:
                    print('.', end='')
            print('|')
        print('+-------+')

    def find_max_y(self):
        max_y = -1
        for _, y in self.settled_rocks:
            max_y = max(max_y, y)
        for _, y in self.falling_rocks:
            max_y = max(max_y, y)
        return max_y

    def fall_down(self):
        candidate = set()
        for x, y in self.falling_rocks:
            y -= 1
            if y < 0 or (x, y) in self.settled_rocks:
                self.settled_rocks = self.settled_rocks.union(self.falling_rocks)
                self.falling_rocks.clear()
                return False
            candidate.add((x, y))
        self.falling_rocks = candidate
        return True

    def blow_left(self):
        candidate = set()
        for x, y in self.falling_rocks:
            x -= 1
            if x < 0 or (x, y) in self.settled_rocks:
                return False
            candidate.add((x, y))
        self.falling_rocks = candidate
        return True

    def blow_right(self):
        candidate = set()
        for x, y in self.falling_rocks:
            x += 1
            if x > 6 or (x, y) in self.settled_rocks:
                return False
            candidate.add((x, y))
        self.falling_rocks = candidate
        return True

    @staticmethod
    def new_rock_coordinates(i, y):
        if i == 0:
            return (2, y), (3, y), (4, y), (5, y)  # horizontal slab
        elif i == 1:
            return (2, y + 1), (3, y), (3, y + 1), (3, y + 2), (4, y + 1)  # cross
        elif i == 2:
            return (2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)  # inverted L
        elif i == 3:
            return (2, y), (2, y + 1), (2, y + 2), (2, y + 3)  # vertical slab
        elif i == 4:
            return (2, y), (2, y + 1), (3, y), (3, y + 1)  # square
        else:
            assert False

    def spawn_new_rock(self):
        for coordinate in self.new_rock_coordinates(self.spawn_count % 5, self.find_max_y() + 4):
            self.falling_rocks.add(coordinate)
        self.spawn_count += 1


def part_one(filename):
    data = read_puzzle_input(filename)
    jets = GasJets(parse_data(data))
    space = Space()

    for _ in range(2022):
        space.spawn_new_rock()
        space.print()
        while True:
            match jets.get():
                case Dir.LEFT:
                    space.blow_left()
                case Dir.RIGHT:
                    space.blow_right()
            space.print()
            if not space.fall_down():
                space.print()
                break
            space.print()

    return space.find_max_y() + 1


def part_two(filename):
    data = read_puzzle_input(filename)
    gas_jets = parse_data(data)
    return -1


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one('Day_17_long_input.txt'))
        # self.assertEqual(3068, part_one('Day_17_short_input.txt'))

    def test_part_two(self):
        self.assertEqual(-1, part_two('Day_17_long_input.txt'))
        self.assertEqual(-1, part_two('Day_17_short_input.txt'))
