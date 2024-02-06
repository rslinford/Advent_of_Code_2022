import re
import unittest
from typing import List


class Valve:
    def __init__(self, label, flow_rate):
        self.label = label
        self.flow_rate = flow_rate
        self.neighbors = []
        self.is_open = False

    def __repr__(self):
        return f'Valve({self.label}, {self.flow_rate}, {self.neighbors})'

    def __lt__(self, other):
        return self.label < other.label


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def parse_lines(data: list[str]) -> dict[str, Valve]:
    rval: dict[str, Valve] = {}
    for line in data:
        result = re.search(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
        label = result.group(1)
        flow_rate = int(result.group(2))
        neighbors = result.group(3)
        valve = Valve(label, flow_rate)
        for v in neighbors.strip().split(', '):
            valve.neighbors.append(v)
        rval[valve.label] = valve
    return rval


class Graph:
    def __init__(self, valves: dict[str, Valve]):
        self.valves = valves

    def neighbors(self, location: str) -> List[str]:
        return self.valves[location].neighbors


def part_one(filename):
    data = read_puzzle_input(filename)
    valves = parse_lines(data)
    graph = Graph(valves)

    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


class Test(unittest.TestCase):
    def test_part_one(self):
        # self.assertEqual(-1, part_one('Day_16_long_input.txt'))
        self.assertEqual(-1, part_one('Day_16_short_input.txt'))

    def test_part_two(self):
        self.assertEqual(-1, part_two('Day_16_long_input.txt'))
        self.assertEqual(-1, part_two('Day_16_short_input.txt'))
