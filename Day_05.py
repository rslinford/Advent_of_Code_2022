import re
import unittest


def read_puzzle_input(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                data.append(line[:-1])
            else:
                data.append(line)

    return data


def find_divide(data: list[str]) -> int:
    for i, line in enumerate(data):
        if line == '':
            return i
    raise ValueError('Expected blank line to separate the stacks from instructions.')


def determine_number_of_stacks(data: list[str]) -> int:
    divide_index = find_divide(data)
    result = re.search('(\d+) *$', data[divide_index - 1])
    return int(result.group(1))


class StackArray:
    def __init__(self):
        self.stacks = []

    def __repr__(self):
        rval = []
        for row in range(self.max_stack_height() - 1, -1, -1):
            s = ''
            for stack in self.stacks:
                if len(s) > 0:
                    s += ' '
                if len(stack) > row:
                    s += '[' + stack[row] + ']'
                else:
                    s += '   '
            rval.append(s)
            rval.append('\n')
        s = ''
        for i in range(len(self.stacks)):
            if len(s) > 0:
                s += '  '
            s += ' ' + str(i + 1)
        rval.append(s)
        rval.append('\n')
        return ''.join(rval)

    def max_stack_height(self):
        max = 0
        for stack in self.stacks:
            if len(stack) > max:
                max = len(stack)
        return max

    def reset(self, data: list[str]):
        number_of_stacks = determine_number_of_stacks(data)
        self.stacks = []
        for i in range(number_of_stacks):
            self.stacks.append([])

    def load_initial_state(self, data: list[str]):
        self.reset(data)
        divide_index = find_divide(data)
        for line in data[divide_index - 2::-1]:
            for stack_i in range(len(self.stacks)):
                crate = line[stack_i * 4 + 1]
                if crate != ' ':
                    self.stacks[stack_i].append(crate)

    def get_top_crates(self):
        rval = ''
        for stack in self.stacks:
            rval += str(stack[-1])
        return rval

    def parse_instruction(self, line):
        result = re.search('^move (\d+) from (\d+) to (\d+)$', line)
        move_count = int(result.group(1))
        from_stack = self.stacks[int(result.group(2)) - 1]
        to_stack = self.stacks[int(result.group(3)) - 1]
        return move_count, from_stack, to_stack

    def follow_instructions_9000(self, data):
        divide_index = find_divide(data)
        for line in data[divide_index + 1:]:
            self.follow_instruction_9000(line)

    def follow_instruction_9000(self, line):
        move_count, from_stack, to_stack = self.parse_instruction(line)
        for i in range(move_count):
            crate = from_stack.pop()
            to_stack.append(crate)

    def follow_instructions_9001(self, data):
        divide_index = find_divide(data)
        for line in data[divide_index + 1:]:
            self.follow_instruction_9001(line)

    def follow_instruction_9001(self, line):
        to_stack: list[str]
        move_count, from_stack, to_stack = self.parse_instruction(line)
        temp = []
        # print(f'Before move {line}\n{self}')
        for i in range(move_count):
            crate = from_stack.pop()
            temp.append(crate)
        to_stack.extend(temp[::-1])
        # print(f'After move {line}\n{self}')


def part_one(filename):
    data = read_puzzle_input(filename)
    sa = StackArray()
    sa.load_initial_state(data)
    sa.follow_instructions_9000(data)
    return sa.get_top_crates()


def part_two(filename):
    data = read_puzzle_input(filename)
    sa = StackArray()
    sa.load_initial_state(data)
    sa.follow_instructions_9001(data)
    return sa.get_top_crates()


filename = "Day_05_input.txt"
print(f'Answer part one: {part_one(filename)}')
print(f'Answer part two: {part_two(filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual('CMZ', part_one('Day_05_short_input.txt'))
        self.assertEqual('QMBMJDFTD', part_one('Day_05_input.txt'))

    def test_part_two(self):
        self.assertEqual('MCD', part_two('Day_05_short_input.txt'))
        self.assertEqual('NBTVTJNFJ', part_two('Day_05_input.txt'))

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


class TestStackArray(unittest.TestCase):
    def test_max_stack_height(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        sa = StackArray()
        sa.load_initial_state(data)
        self.assertEqual(3, sa.max_stack_height())

    def test_repr(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        sa = StackArray()
        sa.load_initial_state(data)
        self.assertEqual("    [D]    \n"
                         "[N] [C]    \n"
                         "[Z] [M] [P]\n"
                         " 1   2   3\n", str(sa))

    def test_load_initial_state(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        sa = StackArray()
        sa.load_initial_state(data)
        self.assertEqual('Z', sa.stacks[0][0])
        self.assertEqual('N', sa.stacks[0][1])
        self.assertEqual('P', sa.stacks[2][0])

    def test_get_top_crates(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        sa = StackArray()
        sa.load_initial_state(data)
        self.assertEqual('NDP', sa.get_top_crates())

    def test_follow_instructions(self):
        data = read_puzzle_input('Day_05_short_input.txt')
        sa = StackArray()
        sa.load_initial_state(data)
        sa.follow_instructions_9000(data)
        self.assertEqual('C', sa.stacks[0][-1])
        self.assertEqual('M', sa.stacks[1][-1])
        self.assertEqual('Z', sa.stacks[2][-1])
