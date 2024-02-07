import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data


def parse_data(data: str):
    droplets = set()
    for row in data.split():
        result = re.findall(r'\d+', row)
        droplets.add((int(result[0]), int(result[1]), int(result[2])))
    return droplets


def neighboring_squares(location):
    x, y, z = location
    return [(x, y, z + 1),  # up
            (x, y, z - 1),  # down
            (x - 1, y, z),  # left
            (x + 1, y, z),  # right
            (x, y + 1, z),  # front
            (x, y - 1, z)]  # back


class LavaPool:
    def __init__(self, droplets):
        self.droplets = droplets

    def count_uncovered_sides(self, location):
        uncovered_sides = 6
        for neighbor in neighboring_squares(location):
            if neighbor in self.droplets:
                uncovered_sides -= 1
        return uncovered_sides


def part_one(filename):
    data = read_puzzle_input(filename)
    pool = LavaPool(parse_data(data))
    exposed_surface_area = 0
    for droplet in pool.droplets:
        exposed_surface_area += pool.count_uncovered_sides(droplet)
    return exposed_surface_area


def part_two(filename):
    data = read_puzzle_input(filename)
    data = parse_data(data)
    return -1


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(4580, part_one('Day_18_long_input.txt'))
        self.assertEqual(64, part_one('Day_18_short_input.txt'))

    def test_part_two(self):
        self.assertEqual(-1, part_two('Day_18_long_input.txt'))
        self.assertEqual(-1, part_two('Day_18_short_input.txt'))
