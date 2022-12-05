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
    def __init__(self, number_of_stacks):
        self.stacks = []
        for i in range(number_of_stacks):
            self.stacks.append([])

    def __repr__(self):
        
        rval = []
        s = ''
        for i in range(len(self.stacks)):
            s += ' ' + str(i+1) + ' '
        rval.append(s)
        return ''.join(rval)
    
    def max_stack_height(self):
        max = 0
        for stack in self.stacks:
            if len(stack) > max:
                max = len(stack)
        return max

def load_initial_state_of_stack_array(data: str) -> StackArray:
    number_of_stacks = determine_number_of_stacks(data)
    sa = StackArray(number_of_stacks)
    divide_index = find_divide(data)
    for line in data[divide_index-2::-1]:
        for stack_i in range(number_of_stacks):
            crate = line[stack_i * 4 + 1]
            if crate != ' ':
                sa.stacks[stack_i].append(crate)
    return sa


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
        
    def test_load_initial_state_of_stack_array(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        sa = load_initial_state_of_stack_array(data)
        # print(sa)
        
class TestStackArray(unittest.TestCase):
    def test_max_stack_height(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        sa = load_initial_state_of_stack_array(data)
        self.assertEqual(3, sa.max_stack_height())