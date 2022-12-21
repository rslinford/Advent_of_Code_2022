import re
import unittest
from dataclasses import dataclass


@dataclass
class Cost:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0

    def array(self):
        return [self.ore, self.clay, self.obsidian]

    def __lt__(self, other):
        return self.ore < other.ore and self.clay < other.clay and self.obsidian < other.obsidian


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def part_one(filename):
    data = read_puzzle_input(filename)
    result = [re.findall('\d+', line) for line in data]
    print(result)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '19'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
print(f'Answer part one: {part_one(long_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one(short_filename))
        self.assertEqual(-1, part_one(long_filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(long_filename))

    def test_cost(self):
        a = Cost(2, 3, 4)
        b = Cost(1, 2, 3)
        self.assertGreater(a, b)
        self.assertLess(b, a)
        c = Cost(2, 3, 4)
        self.assertEqual(a, c)
        self.assertNotEqual(b, c)
