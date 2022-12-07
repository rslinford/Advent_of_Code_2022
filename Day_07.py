import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def build_tree(data: list[str]):
    for line in data:
        if line[0] == '$':
            if line[2:4] == 'cd':
                name = line[5:]
                print('$ cd ' + name)
            elif line[2:4] == 'ls':
                print('$ ls')
            else:
                raise ValueError(f'Unrecognized command: {line}')
        elif line[0:3] == 'dir':
            name = line[4:]
            print('dir ' + name)
        else:
            result = re.search('^(\d+) (.*)', line)
            size = int(result.group(1))
            name = result.group(2)
            print(f'{size} {name}')


def part_one(filename):
    data = read_puzzle_input(filename)
    tree = build_tree(data)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_07_input.txt'
short_filename = 'Day_07_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


# class Test(unittest.TestCase):
#     def test_part_one(self):
#         self.assertEqual(-1, part_one(short_filename))
#         self.assertEqual(-1, part_one(filename))
# 
#     def test_part_two(self):
#         self.assertEqual(-1, part_two(short_filename))
#         self.assertEqual(-1, part_two(filename))
