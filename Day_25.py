import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def snafu_to_decimal(snafu):
    decimal = 0
    for i, c in enumerate(snafu[::-1]):
        place = 5 ** i
        if c in ['0', '1', '2']:
            decimal += place * int(c)
        elif c == '-':
            decimal -= place
        elif c == '=':
            decimal -= place * 2
    return decimal


def part_one(filename):
    data = read_puzzle_input(filename)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '25'
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

    def test_snafu_to_decimal(self):
        self.assertEqual(0, snafu_to_decimal('0'))
        self.assertEqual(1, snafu_to_decimal('1'))
        self.assertEqual(2, snafu_to_decimal('2'))
        self.assertEqual(3, snafu_to_decimal('1='))
        self.assertEqual(4, snafu_to_decimal('1-'))
        self.assertEqual(5, snafu_to_decimal('10'))
        self.assertEqual(6, snafu_to_decimal('11'))
        self.assertEqual(7, snafu_to_decimal('12'))
        self.assertEqual(8, snafu_to_decimal('2='))
        self.assertEqual(9, snafu_to_decimal('2-'))
        self.assertEqual(10, snafu_to_decimal('20'))
        self.assertEqual(15, snafu_to_decimal('1=0'))
        self.assertEqual(20, snafu_to_decimal('1-0'))
        self.assertEqual(2022, snafu_to_decimal('1=11-2'))
        self.assertEqual(12345, snafu_to_decimal('1-0---0'))
        self.assertEqual(314159265, snafu_to_decimal('1121-1110-1=0'))
