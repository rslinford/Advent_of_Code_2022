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


def find_common_letter(s1: str, s2: str) -> str:
    for c1 in s1:
        for c2 in s2:
            if c1 == c2:
                return c1
    raise ValueError(f'No duplicate found in {s1} and {s2}')


def lookup_type_rank(type: str) -> int:
    if type >= 'a' and type <= 'z':
        return ord(type) - ord('a') + 1
    if type >= 'A' and type <= 'Z':
        return ord(type) - ord('A') + 27


def tally_ranks(rucksacks: (str, str)) -> int:
    tally = 0
    for rucksack in rucksacks:
        c = find_common_letter(rucksack[0], rucksack[1])
        tally += lookup_type_rank(c)
    return tally


def part_one(filename):
    data = read_puzzle_input(filename)
    rucksacks = parse_data(data)
    tally = tally_ranks(rucksacks)
    return tally


print(f'Answer part one: {part_one("Day_03_input.txt")}')

class Test(unittest.TestCase):
    def test_parse_data(self):
        data = read_puzzle_input('Day_03_short_input.txt')
        rucksacks = parse_data(data)
        self.assertEqual(rucksacks[0][0], 'vJrwpWtwJgWr')
        self.assertEqual(rucksacks[0][1], 'hcsFMMfFFhFp')
        self.assertEqual(rucksacks[5][0], 'CrZsJsPPZsGz')
        self.assertEqual(rucksacks[5][1], 'wwsLwLmpwMDw')

    def test_find_common_letter(self):
        data = read_puzzle_input('Day_03_short_input.txt')
        rucksacks = parse_data(data)
        self.assertEqual(find_common_letter(rucksacks[0][0], rucksacks[0][1]), 'p')
        self.assertEqual(find_common_letter(rucksacks[1][0], rucksacks[1][1]), 'L')
        self.assertEqual(find_common_letter(rucksacks[2][0], rucksacks[2][1]), 'P')
        self.assertEqual(find_common_letter(rucksacks[3][0], rucksacks[3][1]), 'v')
        self.assertEqual(find_common_letter(rucksacks[4][0], rucksacks[4][1]), 't')
        self.assertEqual(find_common_letter(rucksacks[5][0], rucksacks[5][1]), 's')

    def test_lookup_type_rank(self):
        self.assertEqual(lookup_type_rank('a'), 1)
        self.assertEqual(lookup_type_rank('z'), 26)
        self.assertEqual(lookup_type_rank('A'), 27)
        self.assertEqual(lookup_type_rank('Z'), 52)

    def test_tally_ranks(self):
        data = read_puzzle_input('Day_03_short_input.txt')
        rucksacks = parse_data(data)
        self.assertEqual(tally_ranks(rucksacks), 157)
