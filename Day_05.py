import re
import unittest


def read_puzzle_input(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(line[:-1])
    return data


def find_divide(data: str) -> int:
    for i, line in enumerate(data):
        if line == '':
            return i
    raise ValueError('Expected blank line to separate the stacks from instructions.')

def determine_number_of_stacks(data: str) -> int:
    divide_index = find_divide(data)
    result = re.search('(\d+) *$', data[divide_index-1])
    return int(result.group(1))


class StackArray:
    pass


def load_initial_state_of_stack_array(data: str) -> StackArray:
    pass


def part_one(filename):
    data = read_puzzle_input(filename)
    top_crates = 'CMZ'
    # todo: implement
    return top_crates


filename = "Day_05_short_input.txt"
print(f'Answer part one: {part_one(filename)}')


class Test(unittest.TestCase):
    def test_part_two(self):
        self.assertEqual('CMZ', part_one('Day_05_short_input.txt'))

    def test_read_puzzle_input(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        self.assertEqual('    [D]    ', data[0])
        self.assertEqual('[N] [C]    ', data[1])
        self.assertEqual('[Z] [M] [P]', data[2])

    def test_find_divide(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        self.assertEqual(4, find_divide(data))

    def test_determine_number_of_stacks(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        self.assertEqual(3, determine_number_of_stacks(data))
        