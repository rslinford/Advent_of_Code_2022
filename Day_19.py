import re
import unittest
from dataclasses import dataclass
from enum import Enum, auto


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


class Resource(Enum):
    ORE = auto()
    CLAY = auto()
    OBSIDIAN = auto()
    GEODE = auto()


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
    ore_robot_on_order: int = 0
    clay_robot_on_order: int = 0
    obsidian_robot_on_order: int = 0
    geode_robot_on_order: int = 0


def parse_puzzle_input(data):
    rval = []
    for line in data:
        result = re.search(
            'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.',
            line)
        blueprint = Blueprint(int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4)),
                              int(result.group(5)), int(result.group(6)), int(result.group(7)))
        rval.append(blueprint)
    return rval


def collect_ore(inventory):
    inventory.ore += inventory.ore_robot
    inventory.clay += inventory.clay_robot
    inventory.obsidian += inventory.obsidian_robot
    inventory.geode += inventory.geode_robot


def spend_resources(bp: Blueprint, inv: Inventory):
    if bp.geode_robot_ore_cost <= inv.ore and bp.geode_robot_obsidian_cost <= inv.obsidian:
        inv.geode_robot_on_order = 1
        inv.ore -= bp.geode_robot_ore_cost
        inv.obsidian -= bp.geode_robot_obsidian_cost
        return

    if bp.obsidian_robot_ore_cost <= inv.ore and bp.obsidian_robot_clay_cost <= inv.clay:
        inv.obsidian_robot_on_order = 1
        inv.ore -= bp.obsidian_robot_ore_cost
        inv.clay -= bp.obsidian_robot_clay_cost
        return

    if bp.ore_robot_ore_cost <= inv.ore and inv.ore_robot < max(bp.ore_robot_ore_cost, bp.clay_robot_ore_cost,
                                                                bp.obsidian_robot_ore_cost, bp.geode_robot_ore_cost):
        inv.ore_robot_on_order = 1
        inv.ore -= bp.ore_robot_ore_cost
        return

    if bp.clay_robot_ore_cost <= inv.ore and inv.clay_robot < bp.obsidian_robot_clay_cost:
        inv.clay_robot_on_order = 1
        inv.ore -= bp.clay_robot_ore_cost
        return

def deploy_new_robots(inventory):
    inventory.ore_robot += inventory.ore_robot_on_order
    inventory.ore_robot_on_order = 0
    inventory.clay_robot += inventory.clay_robot_on_order
    inventory.clay_robot_on_order = 0
    inventory.obsidian_robot += inventory.obsidian_robot_on_order
    inventory.obsidian_robot_on_order = 0
    inventory.geode_robot += inventory.geode_robot_on_order
    inventory.geode_robot_on_order = 0


def evaluate_blueprint(blueprint: Blueprint, inventory: Inventory):
    for minute in range(1, 25):
        deploy_new_robots(inventory)
        spend_resources(blueprint, inventory)
        collect_ore(inventory)
        print(f'== Minute {minute} ==')
        print(inventory)


def evaluate_blueprints(blueprints):
    for bp in blueprints:
        inventory = Inventory()
        evaluate_blueprint(bp, inventory)


def part_one(filename):
    data = read_puzzle_input(filename)
    blueprints = parse_puzzle_input(data)
    total = evaluate_blueprints(blueprints)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '19'
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
