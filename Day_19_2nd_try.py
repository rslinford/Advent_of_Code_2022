import re
import unittest
from dataclasses import dataclass
from enum import Enum, auto


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
        return self.ore < other.ore and self.clay < other.clay and self.obsidian < other.obsidian


@dataclass
class Blueprint:
    id: int
    ore: Cost
    clay: Cost
    obsidian: Cost
    geode: Cost

    def array(self):
        return [self.ore.array, self.clay.array, self.obsidian.array, self.geode.array]


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def parse_blueprints(data):
    return [Blueprint(int(row[0]),
                      Cost(int(row[1]), 0, 0),
                      Cost(int(row[2]), 0, 0),
                      Cost(int(row[3]), int(row[4]), 0),
                      Cost(int(row[5]), 0, int(row[6])))
            for row in [re.findall('\d+', line) for line in data]]


def part_one(filename):
    data = read_puzzle_input(filename)
    result = parse_blueprints(data)
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
        self.assertEqual(4, b[0].ore.ore)
        self.assertEqual(0, b[0].ore.clay)
        self.assertEqual(0, b[0].ore.obsidian)
