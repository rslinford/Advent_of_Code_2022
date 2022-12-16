import re
import unittest


class Valve:
    def __init__(self, label, flow_rate):
        self.label = label
        self.flow_rate = flow_rate
        self.neighbors = []
    def __repr__(self):
        return f'Valve({self.label}, {self.flow_rate}, {self.neighbors})'


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def parse_lines(data):
    rval = {}
    for line in data:
        result = re.search('Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
        label = result.group(1)
        flow_rate = result.group(2)
        neighbors = result.group(3)
        valve = Valve(label, flow_rate)
        for v in neighbors.strip().split(', '):
            valve.neighbors.append(v)
        rval[valve.label] = valve
    return rval


def part_one(filename):
    data = read_puzzle_input(filename)
    valves = parse_lines(data)
    for v in valves.values():
        print(v)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '16'
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
