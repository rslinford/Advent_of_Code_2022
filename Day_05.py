import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


def part_one(filename):
    data = read_puzzle_input(filename)
    top_crates = ''
    # todo: implement
    return top_crates


filename = "Day_05_short_input.txt"
print(f'Answer part one: {part_one(filename)}')


class Test(unittest.TestCase):
    def test_part_two(self):
        self.assertEqual('CMZ', part_one('Day_05_short_input.txt'))
