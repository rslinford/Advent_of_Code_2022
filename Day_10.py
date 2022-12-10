import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def part_one(filename):
    data = read_puzzle_input(filename)
    X = 1
    cycle = 1
    tally = 0
    check_cycles = {20, 60, 100, 140, 180, 220}
    for line in data:
        if line == 'noop':
            if cycle in check_cycles:
                tally += cycle * X
            cycle += 1
        else:
            if cycle in check_cycles:
                tally += cycle * X
            elif cycle+1 in check_cycles:
                tally += (cycle+1) * X
            result = re.search('addx (-?\d+)', line)
            V = int(result.group(1))
            X += V
            cycle += 2
    return tally


def part_two(filename):
    data = read_puzzle_input(filename)
    X = 1
    cycle = 1
    line_length = 0
    for line in data:
        print('#', end='')
        line_length += 1
        if line_length >= 40:
            print()
            line_length=0
        if line == 'noop':
            cycle += 1
        else:
            print('.', end='')
            line_length += 1
            if line_length >= 40:
                print()
                line_length = 0
            result = re.search('addx (-?\d+)', line)
            V = int(result.group(1))
            X += V
            cycle += 2
    return -1


filename = 'Day_10_input.txt'
short_filename = 'Day_10_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(13140, part_one(short_filename))
        self.assertEqual(12520, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        # self.assertEqual(-1, part_two(filename))
