import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def parse_ranges(line: str):
    result =  re.search('^(\d+)-(\d+),(\d+)-(\d+)', line)
    e1_min = int(result.group(1))
    e1_max = int(result.group(2))
    e2_min = int(result.group(3))
    e2_max = int(result.group(4))
    return e1_min, e1_max, e2_min, e2_max

def parse_data(data: str) -> list[(str, str)]:
    rval: list[(str, str)] = []
    for line in data.splitlines():
        ranges = parse_ranges(line)
        print(ranges)
        rval.append(ranges)
    return rval



def part_one(filename):
    data = read_puzzle_input(filename)
    pd = parse_data(data)
    # todo: implement
    return 0


filename = "Day_04_input.txt"
print(f'Answer part one: {part_one(filename)}')
# print(f'Answer part two: {part_two(filename)}')


class Test(unittest.TestCase):
    def test_part_two(self):
        pass
        # todo:implement
        # self.assertEqual(1, part_one('Day_04_short_input.txt'))
