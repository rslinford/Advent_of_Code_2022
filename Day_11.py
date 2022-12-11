import re
import unittest
from typing import List, Any


class Monkey:
    if_false_throw_to: int
    if_true_throw_to: int
    test_divisibility: int
    items: list[int]
    operand_two: str
    operand_one: str

    def __init__(self, items, operand_one, operator, operand_two,
                 test_divisibility, if_true_throw_to, if_false_throw_to):
        self.items = items
        self.operand_one = operand_one
        self.operator = operator
        self.operand_two = operand_two
        self.test_divisibility = test_divisibility
        self.if_true_throw_to = if_true_throw_to
        self.if_false_throw_to = if_false_throw_to
        self.inspection_counter = 0

    def __repr__(self):
        rval = []
        rval.append(f'  Items: {self.items}\n')
        rval.append(f'  Operation: new = {self.operand_one} {self.operator} {self.operand_two}\n')
        rval.append(f'  Test: divisible by {self.test_divisibility}\n')
        rval.append(f'    If true: throw to monkey {self.if_true_throw_to}\n')
        rval.append(f'    If false: throw to monkey {self.if_false_throw_to}\n')
        return ''.join(rval)

    def __lt__(self, other):
        return self.inspection_counter < other.inspection_counter

    def evenly_divisible(self, worry):
        return worry % self.test_divisibility == 0

    def operate(self, item):
        if self.operand_one == 'old':
            op1 = item
        else:
            op1 = int(self.operand_one)
        if self.operand_two == 'old':
            op2 = item
        else:
            op2 = int(self.operand_two)
        match self.operator:
            case '+':
                return op1 + op2
            case '*':
                return op1 * op2
            case _:
                raise ValueError(f'Invalid operator {self.operator}')

    def throw_at(self, item, monkey_index, barrel):
        barrel[monkey_index].items.append(item)

    def inspect_items(self, barrel):
        for item in self.items:
            worry = self.operate(item)
            worry = worry % 9699690
            if self.evenly_divisible(worry):
                self.throw_at(worry, self.if_true_throw_to, barrel)
            else:
                self.throw_at(worry, self.if_false_throw_to, barrel)
            self.inspection_counter += 1
        self.items = []


def do_round(barrel):
    for i, monkey in barrel.items():
        monkey.inspect_items(barrel)


short_barrel = {
    0: Monkey([79, 98], 'old', '*', '19', 23, 2, 3),
    1: Monkey([54, 65, 75, 74], 'old', '+', '6', 19, 2, 0),
    2: Monkey([79, 60, 97], 'old', '*', 'old', 13, 1, 3),
    3: Monkey([74], 'old', '+', '3', 17, 0, 1)
}

long_barrel = {
    0: Monkey([64], 'old', '*', '7', 13, 1, 3),
    1: Monkey([60, 84, 84, 65], 'old', '+', '7', 19, 2, 7),
    2: Monkey([52, 67, 74, 88, 51, 61], 'old', '*', '3', 5, 5, 7),
    3: Monkey([67, 72], 'old', '+', '3', 2, 1, 2),
    4: Monkey([80, 79, 58, 77, 68, 74, 98, 64], 'old', '*', 'old', 17, 6, 0),
    5: Monkey([62, 53, 61, 89, 86], 'old', '+', '8', 11, 4, 6),
    6: Monkey([86, 89, 82], 'old', '+', '2', 7, 3, 0),
    7: Monkey([92, 81, 70, 96, 69, 84, 83], 'old', '+', '4', 3, 4, 5),
}


def part_one(barrel: dict[int, Monkey]):
    for r in range(1, 21):
        do_round(barrel)
        # print(f'After round {r}')
        # print(barrel)
    values = list(barrel.values())
    values.sort(reverse=True)
    return values[0].inspection_counter * values[1].inspection_counter


def part_two(barrel):
    for r in range(1, 10001):
        do_round(barrel)
        print(f'After round {r}')
        # print(barrel)
    values = list(barrel.values())
    values.sort(reverse=True)
    return values[0].inspection_counter * values[1].inspection_counter


filename = 'Day_11_input.txt'
short_filename = 'Day_11_short_input.txt'
# print(f'Answer part one: {part_one(long_barrel)}')
print(f'Answer part two: {part_two(long_barrel)}')


# class Test(unittest.TestCase):
#     def test_part_one(self):
#         self.assertEqual(55216, part_one(long_barrel))
#         self.assertEqual(10605, part_one(short_barrel))
#
#     def test_part_two(self):
#         self.assertEqual(2567194800, part_two(short_barrel))
#         self.assertEqual(12848882750, part_two(long_barrel))
