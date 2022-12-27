import unittest
from dataclasses import dataclass
from enum import Enum, auto


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()
    EAST = auto()


@dataclass
class Blizzard:
    x: int
    y: int
    direction: Direction

    def move(self, width, height):
        match self.direction:
            case Direction.NORTH:
                self.y -= 1
                if self.y == 0:
                    self.y = height - 1
            case Direction.SOUTH:
                self.y += 1
                if self.y >= height - 1:
                    self.y = 1
            case Direction.WEST:
                self.x -= 1
                if self.x == 0:
                    self.x = width - 1
            case Direction.EAST:
                self.x += 1
                if self.x >= height - 1:
                    self.x = 1

@dataclass
class Expedition:
    x:int
    y:int

class Board:
    def __init__(self, blizzards: list[Blizzard], height, width):
        self.blizzards = blizzards
        self.height = height
        self.width = width
        self.expedition = Expedition(1, 0)
        self.goal = (self.width - 2, self.height - 1)

    def __repr__(self):
        rval = []
        if self.expedition.x == 1 and self.expedition.y == 0:
            rval.append('#E' + ('#' * (self.width - 2)) + '\n')
        else:
            rval.append('#.' + ('#' * (self.width - 2)) + '\n')
        for y in range(1, self.height - 1):
            rval.append('#')
            for x in range(1, self.width - 1):
                if self.expedition.x == x and self.expedition.y == y:
                    rval.append('E')
                    continue
                local_blizzards = self.blizzards_at(x, y)
                if len(local_blizzards) == 0:
                    rval.append('.')
                elif len(local_blizzards) > 1 and len(local_blizzards) < 10:
                    rval.append(str(len(local_blizzards)))
                elif len(local_blizzards) >= 10:
                    rval.append('*')
                elif len(local_blizzards) == 1:
                    match local_blizzards[0].direction:
                        case Direction.NORTH:
                            rval.append('^')
                        case Direction.SOUTH:
                            rval.append('v')
                        case Direction.WEST:
                            rval.append('<')
                        case Direction.EAST:
                            rval.append('>')
            rval.append('#\n')
        if self.goal ==  (self.expedition.x, self.expedition.y):
            rval.append('#' * (self.width - 2) + 'E#')
        else:
            rval.append('#' * (self.width - 2) + '.#')

        return ''.join(rval)

    def blizzards_at(self, x, y) -> list[Blizzard]:
        rval = []
        for blizzard in self.blizzards:
            if blizzard.x == x and blizzard.y == y:
                rval.append(blizzard)
        return rval

    def move_all(self):
        for blizzard in self.blizzards:
            blizzard.move(self.width, self.height)

def parse_puzzle_input(data: list[str]) -> Board:
    blizzards = []
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            direction = None
            # up (^), down (v), left (<), or right (>)
            match c:
                case '^':
                    direction = Direction.NORTH
                case 'v':
                    direction = Direction.SOUTH
                case '<':
                    direction = Direction.WEST
                case '>':
                    direction = Direction.EAST
            if direction:
                blizzards.append(Blizzard(x, y, direction))
    height = len(data)
    width = len(data[0])
    return Board(blizzards, height, width)


def part_one(filename):
    data = read_puzzle_input(filename)
    board = parse_puzzle_input(data)
    print(board)
    for _ in range(10):
        board.move_all()
        print(board)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '24'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
short_filename_two = f'Day_{day_of_month}_short_input_two.txt'
print(f'Answer part one: {part_one(short_filename)}')
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
    def test_repr(self):
        data = read_puzzle_input(short_filename)
        board = parse_puzzle_input(data)
        self.assertEqual("#.#####\n"
                         "#.....#\n"
                         "#>....#\n"
                         "#.....#\n"
                         "#...v.#\n"
                         "#.....#\n"
                         "#####.#", board.__repr__())
