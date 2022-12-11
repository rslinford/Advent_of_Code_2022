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

    def __repr__(self):
        rval = []
        rval.append(f'  Items: {self.items}\n')
        rval.append(f'  Operation: new = {self.operand_one} {self.operator} {self.operand_two}\n')
        rval.append(f'  Test: divisible by {self.test_divisibility}\n')
        rval.append(f'    If true: throw to monkey {self.if_true_throw_to}\n')
        rval.append(f'    If false: throw to monkey {self.if_false_throw_to}\n')
        return ''.join(rval)

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


    def inspect_items(self):
        for item in self.items:
            worry = self.operate(item)
            worry //= 3
            if self.evenly_divisible(worry):
                pass
            else:
                pass
        self.items = []


def do_round(barrel):
    for monkey in barrel:
        monkey.inspect_items()

short_barrel = [Monkey([79, 98], 'old', '*', '19', 23, 2, 3),
                Monkey([54, 65, 75, 74], 'old', '+', '6', 19, 2, 0),
                Monkey([79, 60, 97], 'old', '*', 'old', 13, 1, 3),
                Monkey([74], 'old', '+', '3', 17, 0, 1),
                ]
do_round(short_barrel)



def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def part_one(filename):
    data = read_puzzle_input(filename)
    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_11_input.txt'
short_filename = 'Day_11_short_input.txt'
print(f'Answer part one: {part_one(filename)}')
print(f'Answer part two: {part_two(filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(-1, part_one(short_filename))
        self.assertEqual(-1, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(filename))
