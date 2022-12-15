import math
import re
from colorama import Fore, Back, Style

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

    def distance_to_beacon(self):
        return calculate_manhatten_distance(self.x, self.y, self.beacon.x, self.beacon.y)


class CaveMap:
    def __init__(self, sensors, target_row):
        min_x, max_x, min_y, max_y = determine_xy_min_max(sensors)
        self.x_offset = 2
        self.min_x = min_x - self.x_offset
        self.min_y = min_y
        self.max_x = max_x + self.x_offset
        self.max_y = max_y
        self.width = max_x - min_x + 1
        self.height = max_y - min_y + 1
        self.sensors = sensors
        self.target_row = target_row

    def __repr__(self):
        rval = [f'({self.min_x}, {self.min_y}) target row {self.target_row}\n']
        for y in range(self.height):
            if y > 0:
                rval.append('\n')
            if y == self.target_row:
                rval.append(Fore.CYAN)
            for x in range(self.width):
                rval.append(self.char_at(x, y))
            if y == self.target_row:
                rval.append(Style.RESET_ALL)
        return ''.join(rval)

    def char_at(self, x, y):
        x -= self.x_offset
        for sensor in self.sensors:
            if sensor.x == x and sensor.y == y:
                return 'S'
            elif sensor.beacon.x == x and sensor.beacon.y == y:
                return 'B'
        return '.'

def calculate_manhatten_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def determine_xy_min_max(sensors: list[Sensor]):
    min_x = math.inf
    min_y = math.inf
    max_x = -math.inf
    max_y = -math.inf
    for sensor in sensors:
        if sensor.x > max_x:
            max_x = sensor.x
        if sensor.x < min_x:
            min_x = sensor.x
        if sensor.y > max_y:
            max_y = sensor.y
        if sensor.y < min_y:
            min_y = sensor.y
        if sensor.beacon.x > max_x:
            max_x = sensor.beacon.x
        if sensor.beacon.x < min_x:
            min_x = sensor.beacon.x
        if sensor.beacon.y > max_y:
            max_y = sensor.beacon.y
        if sensor.beacon.y < min_y:
            min_y = sensor.beacon.y
    return min_x, max_x, min_y, max_y


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


def part_one(filename, target_row):
    data = read_puzzle_input(filename)
    sensors = parse_sensors(data)
    cm = CaveMap(sensors, target_row)
    print(cm)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1

short = True

day_of_month = '15'
if short:
    filename = f'Day_{day_of_month}_short_input.txt'
    target_row = 10
else:
    filename = f'Day_{day_of_month}_long_input.txt'
    target_row = 2,000,000
print(f'Answer part one: {part_one(filename, target_row)}')
print(f'Answer part two: {part_two(filename)}')


# class Test(unittest.TestCase):
#     def test_part_one(self):
#         self.assertEqual(-1, part_one(short_filename))
#         self.assertEqual(-1, part_one(long_filename))
#
#     def test_part_two(self):
#         self.assertEqual(-1, part_two(short_filename))
#         self.assertEqual(-1, part_two(long_filename))
