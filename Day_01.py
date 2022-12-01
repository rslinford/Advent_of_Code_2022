import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


def parse_data(data: str) -> list[int]:
    rval: list[int] = []
    calories = 0
    for line in data.splitlines():
        if line == '':
            rval.append(calories)
            calories = 0
            continue
        calories += int(line)
    if calories:
        rval.append(calories)
    return rval


def part_one(filename):
    data = read_puzzle_input(filename)
    elf_list = parse_data(data)
    max_elf = max(elf_list)
    return max_elf


def part_two(filename):
    data = read_puzzle_input(filename)
    elf_list = parse_data(data)
    elf_list.sort(reverse=True)
    top_three_elves = elf_list[0] + elf_list[1] + elf_list[2]
    print(top_three_elves, elf_list)
    return top_three_elves


class Test(unittest.TestCase):
    def test_part_one(self):
        result = part_one('Day_01_input.txt')
        self.assertEqual(result, 68442)

    def test_part_two(self):
        result = part_two('Day_01_input.txt')
        self.assertEqual(result, 204837)
