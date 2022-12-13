import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def compare_ints(left, right):
    if left < right:
        return 1
    if left > right:
        return -1
    return 0


def compare_objects(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return compare_ints(left, right)
    if isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right)
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    return compare_lists(left, right)


def compare_lists(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return -1
        left_item = left[i]
        right_item = right[i]
        result = compare_objects(left_item, right_item)
        if result == 1 or result == -1:
            return result
    if len(left) < len(right):
        return 1
    if len(left) > len(right):
        return -1
    return 0


def part_one(filename):
    data = read_puzzle_input(filename)
    left = None
    index = 0
    tally = 0
    indices = []
    for line in data:
        if not line:
            continue
        if left == None:
            left = eval(line)
            continue
        right = eval(line)
        index += 1
        print(index, left, right)
        if compare_lists(left, right) == 1:
            indices.append(index)
            tally += index
        left = None
    print(f'Indices: {indices}')
    return tally


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


long_filename = 'Day_13_input.txt'
short_filename = 'Day_13_short_input.txt'
print(f'Answer part one: {part_one(long_filename)}')
print(f'Answer part two: {part_two(short_filename)}')

# class Test(unittest.TestCase):
#     def test_part_one(self):
#         self.assertEqual(-1, part_one(short_filename))
#         self.assertEqual(-1, part_one(long_filename))
#
#     def test_part_two(self):
#         self.assertEqual(-1, part_two(short_filename))
#         self.assertEqual(-1, part_two(long_filename))
