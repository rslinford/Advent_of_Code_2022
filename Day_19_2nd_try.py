import re
import unittest
from dataclasses import dataclass
from enum import Enum, auto
from copy import copy

class Mineral(Enum):
    ORE = 0
    CLAY = auto()
    OBSIDIAN = auto()
    GEODE = auto()


@dataclass
class Cost:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0

    def array(self):
        return [self.ore, self.clay, self.obsidian]

    def __lt__(self, other):
        return self.ore < other.ore_bot_cost and self.clay < other.clay_bot_cost and self.obsidian < other.obsidian_bot_cost


@dataclass
class BotInventory:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0


@dataclass
class ResourceInventory:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def can_afford(self, cost: Cost):
        return self.ore >= cost.ore and self.clay >= cost.clay and self.obsidian >= cost.obsidian

    def subtract(self, cost: Cost):
        self.ore -= cost.ore
        self.clay -= cost.clay
        self.obsidian -= cost.obsidian


@dataclass
class Blueprint:
    id: int
    ore_bot_cost: Cost
    clay_bot_cost: Cost
    obsidian_bot_cost: Cost
    geode_bot_cost: Cost

    def array(self):
        return [self.ore_bot_cost.array, self.clay_bot_cost.array, self.obsidian_bot_cost.array, self.geode_bot_cost.array]


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def parse_blueprints(data):
    return [Blueprint(int(row[0]),
                      Cost(ore=int(row[1])),
                      Cost(ore=int(row[2])),
                      Cost(ore=int(row[3]), clay=int(row[4])),
                      Cost(ore=int(row[5]), obsidian=int(row[6])))
            for row in [re.findall('\d+', line) for line in data]]


max_geode = 0
def quality_level(bp: Blueprint, time_limit):
    global max_geode
    def maximize_geode(remaining_time, bot_inv: BotInventory, res_inv: ResourceInventory, bot_order: Mineral = None) -> int:
        global max_geode
        print(bp.id, bot_inv, res_inv, remaining_time, max_geode)
        if remaining_time <= 0:
            if res_inv.geode > max_geode:
                max_geode = res_inv.geode
            return max_geode
        # todo: caching optimization here?
        # Harvest minerals
        res_inv.ore += bot_inv.ore
        res_inv.clay += bot_inv.clay
        res_inv.obsidian += bot_inv.obsidian
        res_inv.geode += bot_inv.geode

        # Handle bot creation order
        if bot_order:
            match bot_order:
                case Mineral.GEODE:
                    res_inv.subtract(bp.geode_bot_cost)
                    bot_inv.geode += 1
                case Mineral.OBSIDIAN:
                    res_inv.subtract(bp.obsidian_bot_cost)
                    bot_inv.obsidian += 1
                case Mineral.CLAY:
                    res_inv.subtract(bp.clay_bot_cost)
                    bot_inv.clay += 1
                case Mineral.ORE:
                    res_inv.subtract(bp.ore_bot_cost)
                    bot_inv.ore += 1

        # Geode
        if res_inv.can_afford(bp.geode_bot_cost):
            maximize_geode(remaining_time - 1, copy(bot_inv), copy(res_inv), Mineral.GEODE)

        if res_inv.can_afford(bp.obsidian_bot_cost) and bot_inv.obsidian <= bp.geode_bot_cost.obsidian:
            maximize_geode(remaining_time - 1, copy(bot_inv), copy(res_inv), Mineral.OBSIDIAN)

        if res_inv.can_afford(bp.clay_bot_cost) and \
                bot_inv.clay <= bp.obsidian_bot_cost.clay and \
                res_inv.clay < bp.obsidian_bot_cost.clay:
            maximize_geode(remaining_time - 1, copy(bot_inv), copy(res_inv), Mineral.CLAY)

        if res_inv.can_afford(bp.ore_bot_cost) and bot_inv.ore <= max(bp.ore_bot_cost.ore, bp.clay_bot_cost.ore, bp.obsidian_bot_cost.ore, bp.geode_bot_cost.ore):
            maximize_geode(remaining_time - 1, copy(bot_inv), copy(res_inv), Mineral.ORE)

        maximize_geode(remaining_time - 1, copy(bot_inv), copy(res_inv), None)

        return max_geode

    return bp.id * maximize_geode(time_limit, BotInventory(ore=1), ResourceInventory())


def part_one(filename):
    data = read_puzzle_input(filename)
    blueprints = parse_blueprints(data)
    result = [quality_level(blueprint, 24) for blueprint in blueprints]
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

    def test_cost(self):
        a = Cost(2, 3, 4)
        b = Cost(1, 2, 3)
        self.assertGreater(a, b)
        self.assertLess(b, a)
        c = Cost(2, 3, 4)
        self.assertEqual(a, c)
        self.assertNotEqual(b, c)

    def test_mineral(self):
        self.assertEqual(0, Mineral.ORE.value)
        self.assertEqual(1, Mineral.CLAY.value)
        self.assertEqual(2, Mineral.OBSIDIAN.value)
        self.assertEqual(3, Mineral.GEODE.value)

        a = Cost(4, 5, 6)
        self.assertEqual(4, a.array()[Mineral.ORE.value])
        self.assertEqual(5, a.array()[Mineral.CLAY.value])
        self.assertEqual(6, a.array()[Mineral.OBSIDIAN.value])

    def test_parse_blueprint(self):
        data = read_puzzle_input(short_filename)
        b = parse_blueprints(data)
        self.assertEqual(2, len(b))
        self.assertEqual(1, b[0].id)
        self.assertEqual(4, b[0].ore_bot_cost.ore)
        self.assertEqual(0, b[0].ore_bot_cost.clay)
        self.assertEqual(0, b[0].ore_bot_cost.obsidian)
