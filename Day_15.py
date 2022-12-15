import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Beacon({self.x}, {self.y})'


class Sensor:
    def __init__(self, x, y, beacon: Beacon):
        self.x = x
        self.y = y
        self.beacon = beacon

    def __repr__(self):
        return f'Sensor({self.x}, {self.y}, {self.beacon})'


def parse_sensors(data):
    sensors = []
    for line in data:
        result = re.search('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        xs = int(result.group(1))
        ys = int(result.group(2))
        xb = int(result.group(3))
        yb = int(result.group(4))
        sensors.append(Sensor(xs, ys, Beacon(xb, yb)))

    return sensors


def part_one(filename):
    data = read_puzzle_input(filename)
    sensors = parse_sensors(data)
    for sensor in sensors:
        print(sensor)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '15'
filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one(short_filename))
        self.assertEqual(-1, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(filename))
