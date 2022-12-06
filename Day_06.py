import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


def part_one(filename):
    data = read_puzzle_input(filename)
    for i,c in enumerate(data):
        four = set()
        for j in range(i,i+4):
            four.add(data[j])
        if len(four) == 4:
            return i + 4
        # print(i, c, four)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_06_input.txt'
short_filename = 'Day_06_short_input.txt'
print(f'Answer part one: {part_one(filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(5, part_one(short_filename))
        self.assertEqual(1356, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(short_filename))
