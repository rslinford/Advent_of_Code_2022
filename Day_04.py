import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


def parse_ranges(line: str):
    result = re.search('^(\d+)-(\d+),(\d+)-(\d+)', line)
    e1_min = int(result.group(1))
    e1_max = int(result.group(2))
    e2_min = int(result.group(3))
    e2_max = int(result.group(4))
    return e1_min, e1_max, e2_min, e2_max


def parse_data(data: str) -> list[(str, str)]:
    rval: list[(str, str)] = []
    for line in data.splitlines():
        ranges = parse_ranges(line)
        rval.append(ranges)
    return rval


def part_one(filename):
    data = read_puzzle_input(filename)
    assignments = parse_data(data)
    tally = 0
    for assignment in assignments:
        if one_range_fully_contains_the_other(*assignment):
            tally += 1
    return tally


def part_two(filename):
    data = read_puzzle_input(filename)
    assignments = parse_data(data)
    tally = 0
    for assignment in assignments:
        if ranges_overlap(*assignment):
            tally += 1
    return tally


def one_range_fully_contains_the_other(
        e1_min: int, e1_max: int, e2_min: int, e2_max: int) -> bool:
    if e1_min <= e2_min and e1_max >= e2_max:
        return True
    if e1_min >= e2_min and e1_max <= e2_max:
        return True
    return False


def ranges_overlap(
        e1_min: int, e1_max: int, e2_min: int, e2_max: int) -> bool:
    if e1_min < e2_min and e1_max < e2_min:
        return False
    if e1_min > e2_max:
        return False
    return True


filename = "Day_04_input.txt"
print(f'Answer part one: {part_one(filename)}')
print(f'Answer part two: {part_two(filename)}')


class Test(unittest.TestCase):
    def test_part_two(self):
        self.assertEqual(2, part_one('Day_04_short_input.txt'))

    def test_part_two(self):
        self.assertEqual(4, part_two('Day_04_short_input.txt'))

    def test_parse_data(self):
        data = read_puzzle_input('Day_04_short_input.txt')
        pd = parse_data(data)
        self.assertEqual(2, pd[0][0])
        self.assertEqual(4, pd[0][1])
        self.assertEqual(6, pd[0][2])
        self.assertEqual(8, pd[0][3])

    def test_one_range_fully_contains_the_other(self):
        data = read_puzzle_input('Day_04_short_input.txt')
        pd = parse_data(data)
        self.assertFalse(one_range_fully_contains_the_other(*pd[0]))
        self.assertTrue(one_range_fully_contains_the_other(*pd[3]))
        self.assertTrue(one_range_fully_contains_the_other(*pd[4]))
        self.assertFalse(one_range_fully_contains_the_other(*pd[5]))

    def test_ranges_overlap(self):
        data = read_puzzle_input('Day_04_short_input.txt')
        pd = parse_data(data)
        self.assertFalse(ranges_overlap(*pd[0]))
        self.assertFalse(ranges_overlap(*pd[1]))
        self.assertTrue(ranges_overlap(*pd[2]))
        self.assertTrue(ranges_overlap(*pd[3]))
        self.assertTrue(ranges_overlap(*pd[4]))
        self.assertTrue(ranges_overlap(*pd[5]))
        self.assertFalse(ranges_overlap(*pd[6]))
