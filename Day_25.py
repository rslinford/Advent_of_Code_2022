import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def snafu_to_decimal(snafu: str):
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


def decimal_to_snafu(decimal: int):
    snafu = '0'
    for i in range(1, decimal + 1):
        snafu = increment_snafu(snafu)
        if decimal > 5000 and i % 1000000 == 0:
            print(f'{snafu} {i / decimal}')
    return snafu


SNAFU_MAP = {'0': '1', '1': '2', '2': '=', '=': '-', '-': '0'}


def increment_snafu(snafu: str):
    rval = []
    needs_increment = True
    for c in snafu[::-1]:
        if needs_increment:
            rval.insert(0, SNAFU_MAP.get(c))
            needs_increment = c == '2'
        else:
            rval.insert(0, c)
            needs_increment = False
    if needs_increment:
        rval.insert(0, '1')
    return ''.join(rval)


def part_one(filename):
    data = read_puzzle_input(filename)
    total = 0
    for i, line in enumerate(data):
        print(f'{i} / {len(data)} {line}')
        total += snafu_to_decimal(line)
        # 36,671,616,971,741
    return decimal_to_snafu(total)


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '25'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
# print(f'Answer part one: {part_one(short_filename)}')
# print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual('2=-1=0', part_one(short_filename))
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

    def test_increment_snafu(self):
        self.assertEqual('1', increment_snafu('0'))
        self.assertEqual('2', increment_snafu('1'))
        self.assertEqual('1=', increment_snafu('2'))
        self.assertEqual('1-', increment_snafu('1='))
        self.assertEqual('10', increment_snafu('1-'))
        self.assertEqual('11', increment_snafu('10'))
        self.assertEqual('12', increment_snafu('11'))
        self.assertEqual('2=', increment_snafu('12'))
        self.assertEqual('2-', increment_snafu('2='))
        self.assertEqual('20', increment_snafu('2-'))

    def test_decimal_to_snafu(self):
        self.assertEqual('0', decimal_to_snafu(0))
        self.assertEqual('1', decimal_to_snafu(1))
        self.assertEqual('2', decimal_to_snafu(2))
        self.assertEqual('1=', decimal_to_snafu(3))
        self.assertEqual('1-', decimal_to_snafu(4))
        self.assertEqual('10', decimal_to_snafu(5))
        self.assertEqual('1=-0-2', decimal_to_snafu(1747))
        self.assertEqual('12111', decimal_to_snafu(906))
        self.assertEqual('1=-1=', decimal_to_snafu(353))