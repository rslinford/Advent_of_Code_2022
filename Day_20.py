import re
import unittest
from dataclasses import dataclass


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def part_one(filename):
    data = read_puzzle_input(filename)
    return -1


@dataclass
class NumberCircle:
    def __init__(self, number):
        self.next = self
        self.prev = self
        self.number = number

    def __repr__(self):
        return str(self.number)

    def insert_after(self, other):
        other_next = other.next
        other_prev = other.prev
        other.prev = self.prev
        other.next = self.next
        self.next = other_next
        self.prev = other_prev


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '20'
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


class TestNumberCircle(unittest.TestCase):
    def test_insert_after(self):
        a = NumberCircle(5)
        b = NumberCircle(6)
        a.insert_after(b)
        print(a)
        print(b)
