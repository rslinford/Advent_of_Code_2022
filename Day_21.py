import re
import unittest
from dataclasses import dataclass


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def parse_puzzle_input(data):
    monkeys = {}
    for line in data:
        result = re.search('^(....): (.+)$', line)
        m = Monkey(result.group(1), result.group(2))
        monkeys[m.id] = m
    return monkeys


@dataclass
class Monkey:
    id: str
    job: str

    def is_yelling(self):
        return self.job.isnumeric()


def part_one(filename):
    data = read_puzzle_input(filename)
    monkeys = parse_puzzle_input(data)
    for monkey in monkeys.values():
        if monkey.is_yelling():
            continue

    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '21'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
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
