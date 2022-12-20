import re
import unittest
from dataclasses import dataclass


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


@dataclass
class Blueprint:
    blueprint_id: int
    ore_robot_ore_cost: int
    clay_robot_ore_cost: int
    obsidian_robot_ore_cost: int
    obsidian_robot_clay_cost: int
    geode_robot_ore_cost: int
    geode_robot_obsidian_cost: int

@dataclass
class Inventory:
    ore_robot: int = 1
    clay_robot: int = 0
    obsidian_robot: int = 0
    geode_robot: int = 0
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

def parse_puzzle_input(data):
    rval = []
    for line in data:
        result = re.search('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', line)
        blueprint = Blueprint(int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4)),
                              int(result.group(5)), int(result.group(6)), int(result.group(7)))
        rval.append(blueprint)
    return

def part_one(filename):
    data = read_puzzle_input(filename)
    blueprints = parse_puzzle_input(data)
    inventory = Inventory()
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '19'
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
