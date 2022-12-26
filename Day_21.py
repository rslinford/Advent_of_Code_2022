import re
import unittest
from dataclasses import dataclass


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def parse_puzzle_input(data):
    monkeys = {}
    for line in data:
        result = re.search('^(....): (.+)$', line)
        m = Monkey(result.group(1), result.group(2))
        monkeys[m.id] = m
    return monkeys


@dataclass
class Monkey:
    id: str
    job: str

    def is_yelling(self):
        try:
            int(self.job)
            return True
        except ValueError:
            return False

    def parse_job(self) -> tuple[str, str, str]:
        result = re.search('(....) (.) (....)$', self.job)
        return result.group(1), result.group(2), result.group(3)

    def solve(self, operand1, operator, operand2):
        op1 = int(operand1)
        op2 = int(operand2)
        match operator:
            case '+':
                self.job = str(op1 + op2)
            case '-':
                self.job = str(op1 - op2)
            case '*':
                self.job = str(op1 * op2)
            case '/':
                self.job = str(op1 // op2)

    def set_job(self, job):
        self.job = job


def part_one(filename):
    data = read_puzzle_input(filename)
    monkeys = parse_puzzle_input(data)
    while True:
        for monkey in monkeys.values():
            if monkey.is_yelling():
                continue
            operand1, operator, operand2 = monkey.parse_job()
            if not monkeys[operand1].is_yelling() or not monkeys[operand2].is_yelling():
                continue
            monkey.solve(monkeys[operand1].job, operator, monkeys[operand2].job)
            if monkey.id == 'root':
                return int(monkey.job)


# def counting_numbers():
#     i = 1
#     while True:
#         yield i
#         i += 1

def part_two(filename):
    data = read_puzzle_input(filename)
    monkeys = parse_puzzle_input(data)
    # cn = counting_numbers()
    test_value = 1
    while True:
        for monkey in monkeys.values():
            if monkey.id == 'humn':
                # test_value = str(next(cn))
                monkey.set_job(str(test_value))
            if monkey.is_yelling():
                continue
            operand1, operator, operand2 = monkey.parse_job()
            if monkey.id == 'root':
                if monkeys[operand1].is_yelling() and monkeys[operand2].is_yelling():
                    if monkeys[operand1].job == monkeys[operand2].job:
                        return test_value
                    else:
                        test_value += 1
                        if test_value == 301:
                            print("here")
                        monkeys = parse_puzzle_input(data)
                        break
            if not monkeys[operand1].is_yelling() or not monkeys[operand2].is_yelling():
                continue
            monkey.solve(monkeys[operand1].job, operator, monkeys[operand2].job)



day_of_month = '21'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
print(f'Answer part one: {part_one(long_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(152, part_one(short_filename))
        self.assertEqual(56490240862410, part_one(long_filename))

    # def test_part_two(self):
    #     self.assertEqual(-1, part_two(short_filename))
    #     self.assertEqual(-1, part_two(long_filename))
