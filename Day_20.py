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
        old_self_next = self.next
        self.next = other
        other.prev = self
        other.next = old_self_next
        old_self_next.prev = other


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
        a1 = NumberCircle(1)
        a2 = NumberCircle(2)
        a1.insert_after(a2)
        self.assertEqual(2, a1.next.number)
        self.assertEqual(2, a1.prev.number)
        self.assertEqual(1, a2.next.number)
        self.assertEqual(1, a2.prev.number)
        a3 = NumberCircle(3)
        a1.insert_after(a3)
        self.assertEqual(1, a3.prev.number)
        self.assertEqual(2, a3.next.number)
