import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def part_one(filename):
    data = read_puzzle_input(filename)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_12_input.txt'
short_filename = 'Day_12_short_input.txt'
print(f'Answer part one: {part_one(filename)}')
print(f'Answer part two: {part_two(filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one(short_filename))
        self.assertEqual(-1, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(filename))
