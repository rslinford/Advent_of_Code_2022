import unittest
from dataclasses import dataclass
from enum import Enum, auto


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().split('\n')
    return data


def parse_puzzle_input(data):
    matrix = list()
    directions = ''
    end_of_matrix_reached = False
    for line in data:
        if end_of_matrix_reached:
            directions = line
        if len(line) > 0 and not end_of_matrix_reached:
            matrix.append(line)
        elif len(line) == 0:
            end_of_matrix_reached = True
    return matrix, directions


def find_starting_position(matrix):
    y = 0
    for x, c in enumerate(matrix[0]):
        if c != ' ':
            return x, y


class Heading(Enum):
    EAST = 0
    SOUTH = auto()
    WEST = auto()
    NORTH = auto()


@dataclass
class Board:
    width: int = 0
    height: int = 0
    matrix: list[str] = None

    def initialize(self, matrix):
        self.matrix = []
        max_len = 0
        for line in matrix:
            if len(line) > max_len:
                max_len = len(line)
        self.width = max_len
        self.height = len(matrix)
        for line in matrix:
            if len(line) == self.width:
                self.matrix.append(line)
            elif len(line) < self.width:
                line += ' ' * (self.width - len(line))
                self.matrix.append(line)
            else:
                assert False

    def __repr__(self):
        rval = []
        for line in self.matrix:
            rval.append(line)
            rval.append('\n')
        return ''.join(rval)

    def tile_at(self, x, y):
        return self.matrix[y][x]


@dataclass
class Player:
    x: int = 0
    y: int = 0
    heading: Heading = Heading.EAST

    def follow_directions(self, board, directions):
        token = ''
        for c in directions:
            if c.isdecimal():
                token += c
            else:
                if token:
                    steps = int(token)
                    token = ''
                    for i in range(steps):
                        self.move_one_step(board)
                if c == 'L':
                    if self.heading == Heading.NORTH:
                        self.heading = Heading.WEST
                    elif self.heading == Heading.WEST:
                        self.heading = Heading.SOUTH
                    elif self.heading == Heading.SOUTH:
                        self.heading = Heading.EAST
                    elif self.heading == Heading.EAST:
                        self.heading = Heading.NORTH
                elif c == 'R':
                    if self.heading == Heading.NORTH:
                        self.heading = Heading.EAST
                    elif self.heading == Heading.EAST:
                        self.heading = Heading.SOUTH
                    elif self.heading == Heading.SOUTH:
                        self.heading = Heading.WEST
                    elif self.heading == Heading.WEST:
                        self.heading = Heading.NORTH

    def x_and_y(self):
        return self.x, self.y

    def move_one_step(self, board: Board):
        x, y = self.x_and_y()
        match self.heading:
            case Heading.NORTH:
                y -= 1
                if y < 0:
                    y = board.height - 1
                match board.tile_at(x, y):
                    case ' ':
                        for y2 in range(board.height - 1, y, -1):
                            if board.tile_at(x, y2) == ' ':
                                continue
                            if board.tile_at(x, y2) == '.':
                                self.set_location(x, y2)
                    case '.':
                        self.set_location(x, y)
                    case '#':
                        pass
                    case _:
                        raise ValueError(f'Unrecognized tile {board.tile_at(x, y)}')

            case Heading.EAST:
                x += 1
                if x >= board.width:
                    x = 0
                match board.tile_at(x, y):
                    case ' ':
                        for x2 in range(0, x):
                            if board.tile_at(x2, y) == ' ':
                                continue
                            if board.tile_at(x2, y) == '.':
                                self.set_location(x2, y)
                                break
                            if board.tile_at(x2, y) == '#':
                                break
                    case '.':
                        self.set_location(x, y)
                    case '#':
                        pass
                    case _:
                        raise ValueError(f'Unrecognized tile {board.tile_at(x, y)}')
            case Heading.SOUTH:
                y += 1
                if y >= board.height:
                    y = 0
                match board.tile_at(x, y):
                    case ' ':
                        for y2 in range(0, y):
                            if board.tile_at(x, y2) == ' ':
                                continue
                            if board.tile_at(x, y2) == '.':
                                self.set_location(x, y2)
                                break
                            if board.tile_at(x, y2) == '#':
                                break

                    case '.':
                        self.set_location(x, y)
                    case '#':
                        pass
                    case _:
                        raise ValueError(f'Unrecognized tile {board.tile_at(x, y)}')
            case Heading.WEST:
                x -= 1
                if x < 0:
                    x = board.width - 1
                match board.tile_at(x, y):
                    case ' ':
                        for x2 in range(board.width - 1, x):
                            if board.tile_at(x2, y) == ' ':
                                continue
                            if board.tile_at(x2, y) == '.':
                                self.set_location(x2, y)
                                break
                            if board.tile_at(x2, y) == '#':
                                break
                    case '.':
                        self.set_location(x, y)
                    case '#':
                        pass
                    case _:
                        raise ValueError(f'Unrecognized tile {board.tile_at(x, y)}')

    def set_location(self, x, y):
        self.x = x
        self.y = y


def part_one(filename):
    data = read_puzzle_input(filename)
    matrix, directions = parse_puzzle_input(data)
    x, y = find_starting_position(matrix)
    player = Player(x, y, Heading.EAST)
    board = Board()
    board.initialize(matrix)
    print(board)
    player.follow_directions(board, directions)

    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '22'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
# print(f'Answer part one: {part_one(short_filename)}')
# print(f'Answer part two: {part_two(short_filename)}')


# class Test(unittest.TestCase):
#     def test_part_one(self):
#         self.assertEqual(-1, part_one(short_filename))
#         self.assertEqual(-1, part_one(long_filename))
#
#     def test_part_two(self):
#         self.assertEqual(-1, part_two(short_filename))
#         self.assertEqual(-1, part_two(long_filename))


class TestPlayer(unittest.TestCase):
    def test_move_one_step(self):
        data = read_puzzle_input(short_filename)
        matrix, directions = parse_puzzle_input(data)
        x, y = find_starting_position(matrix)
        player = Player(x, y, Heading.EAST)
        board = Board()
        board.initialize(matrix)
        self.assertEqual((8, 0), player.x_and_y())
        player.move_one_step(board)
        self.assertEqual((9, 0), player.x_and_y())
        player.move_one_step(board)
        self.assertEqual((10, 0), player.x_and_y())
        player.move_one_step(board)
        self.assertEqual((10, 0), player.x_and_y())
        player.heading = Heading.NORTH
        player.move_one_step(board)
        self.assertEqual((10, 11), player.x_and_y())
        player.heading = Heading.SOUTH
        player.move_one_step(board)
        self.assertEqual((10, 0), player.x_and_y())
        player.heading = Heading.WEST
        player.move_one_step(board)
        player.move_one_step(board)
        self.assertEqual((8, 0), player.x_and_y())
        player.move_one_step(board)
        self.assertEqual((8, 0), player.x_and_y())
        player.heading = Heading.EAST
        player.move_one_step(board)
        player.move_one_step(board)
        self.assertEqual((10, 0), player.x_and_y())
        player.heading = Heading.NORTH
        player.move_one_step(board)
        self.assertEqual((10, 11), player.x_and_y())
        player.heading = Heading.EAST
        player.move_one_step(board)
        self.assertEqual((11, 11), player.x_and_y())
        player.heading = Heading.SOUTH
        player.move_one_step(board)
        self.assertEqual((11, 11), player.x_and_y())
        print(board)

class test_heading(unittest.TestCase):
    def test(self):
        self.assertEqual(0, Heading.EAST.value)
        self.assertEqual(1, Heading.SOUTH.value)
        self.assertEqual(2, Heading.WEST.value)
        self.assertEqual(3, Heading.NORTH.value)
