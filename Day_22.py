import re
import unittest


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


def part_one(filename):
    data = read_puzzle_input(filename)
    matrix, directions = parse_puzzle_input(data)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '22'
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
