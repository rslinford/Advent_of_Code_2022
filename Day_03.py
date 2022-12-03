import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


def parse_data(data: str) -> list[(str, str)]:
    rval: list[(str, str)] = []
    for line in data.splitlines():
        h = len(line) // 2
        rval.append((line[0:h], line[h:]))
    return rval


def part_one(filename):
    data = read_puzzle_input(filename)
    rucksacks = parse_data(data)
    print(rucksacks)
    return 0


# print(f'Answer part one: {part_one("Day_03_short_input.txt")}')


class Test(unittest.TestCase):
    def test_parse_data(self):
        data = read_puzzle_input('Day_03_short_input.txt')
        rucksacks = parse_data(data)
        self.assertEqual(rucksacks[0][0], 'vJrwpWtwJgWr')
        self.assertEqual(rucksacks[0][1], 'hcsFMMfFFhFp')
        self.assertEqual(rucksacks[5][0], 'CrZsJsPPZsGz')
        self.assertEqual(rucksacks[5][1], 'wwsLwLmpwMDw')

