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


def find_common_letter_for_three(s1: str, s2: str, s3: str):
    for c1 in s1:
        for c2 in s2:
            if c1 == c2 and c1 in s3:
                return c1
    raise ValueError(f'{s1}, {s2} and {s3} have no common char')


def lookup_type_rank(type: str) -> int:
    if type >= 'a' and type <= 'z':
        return ord(type) - ord('a') + 1
    if type >= 'A' and type <= 'Z':
        return ord(type) - ord('A') + 27
    raise ValueError(f'Expected a letter. Got {type} instead.')


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


def part_two(filename):
    data = read_puzzle_input(filename)
    rucksacks = parse_data(data)
    tally = 0
    for i in range(0, len(rucksacks), 3):
        common_letter = find_common_letter_for_three(
            rucksacks[i][0] + rucksacks[i][1],
            rucksacks[i + 1][0] + rucksacks[i + 1][1],
            rucksacks[i + 2][0] + rucksacks[i + 2][1])
        tally += lookup_type_rank(common_letter)

    return tally

filename = "Day_03_input.txt"
print(f'Answer part one: {part_one(filename)}')
print(f'Answer part two: {part_two(filename)}')


class Test(unittest.TestCase):
    def test_part_two(self):
        self.assertEqual(70, part_two('Day_03_short_input.txt'))

    def test_parse_data(self):
        data = read_puzzle_input('Day_03_short_input.txt')
        rucksacks = parse_data(data)
        self.assertEqual('vJrwpWtwJgWr', rucksacks[0][0])
        self.assertEqual('hcsFMMfFFhFp', rucksacks[0][1])
        self.assertEqual('CrZsJsPPZsGz', rucksacks[5][0])
        self.assertEqual('wwsLwLmpwMDw', rucksacks[5][1])

    def test_find_common_letter(self):
        data = read_puzzle_input('Day_03_short_input.txt')
        rucksacks = parse_data(data)
        self.assertEqual('p', find_common_letter(rucksacks[0][0], rucksacks[0][1]))
        self.assertEqual('L', find_common_letter(rucksacks[1][0], rucksacks[1][1]))
        self.assertEqual('P', find_common_letter(rucksacks[2][0], rucksacks[2][1]))
        self.assertEqual('v', find_common_letter(rucksacks[3][0], rucksacks[3][1]))
        self.assertEqual('t', find_common_letter(rucksacks[4][0], rucksacks[4][1]))
        self.assertEqual('s', find_common_letter(rucksacks[5][0], rucksacks[5][1]))

    def test_lookup_type_rank(self):
        self.assertEqual(1, lookup_type_rank('a'))
        self.assertEqual(26, lookup_type_rank('z'))
        self.assertEqual(27, lookup_type_rank('A'))
        self.assertEqual(52, lookup_type_rank('Z'))

    def test_tally_ranks(self):
        data = read_puzzle_input('Day_03_short_input.txt')
        rucksacks = parse_data(data)
        self.assertEqual(157, tally_ranks(rucksacks))

    def test_find_common_letter_for_three(self):
        c = find_common_letter_for_three(
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg')
        self.assertEqual('r', c)
        c = find_common_letter_for_three(
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw')
        self.assertEqual('Z', c)
