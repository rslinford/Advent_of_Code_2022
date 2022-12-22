import unittest
from dataclasses import dataclass


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


@dataclass
class NumberCircle:
    id_counter = 0

    def __init__(self, number):
        self.id = NumberCircle.id_counter
        NumberCircle.id_counter += 1
        self.next = self
        self.prev = self
        self.number = number

    def __repr__(self):
        return str(self.number)

    def __eq__(self, other):
        return self.id == other.id

    def repr_full_circle(self):
        rval = [f'{self.number}\n']
        current = self.next
        while current != self:
            rval.append(f'{current.number}\n')
            current = current.next
        return ''.join(rval)

    def insert_after(self, other):
        old_self_next = self.next
        self.next = other
        other.prev = self
        other.next = old_self_next
        old_self_next.prev = other

    def remove(self):
        """Remove self from circle"""
        self.next.prev = self.prev
        self.prev.next = self.next
        self.next = self
        self.prev = self

    def move(self):
        if self.number == 0:
            return
        n = self.number
        negative = n < 0
        if negative:
            n = -n
            current = self.prev
        else:
            n -= 1
            current = self.next
        for _ in range(n):
            if negative:
                current = current.prev
            else:
                current = current.next
        self.remove()
        current.insert_after(self)

    def snapshot(self):
        """Takes a snapshot, a list, of the entire circle with self as the first element."""
        rval = [self]
        current = self.next
        while current != self:
            rval.append(current)
            current = current.next

        return rval


def parse_puzzle_input(data) -> NumberCircle:
    previous = None
    first = None
    for line in data:
        n = NumberCircle(int(line))
        if not first:
            first = n
        else:
            previous.insert_after(n)
        previous = n
    return first


def mix(circle: NumberCircle):
    initial_snapshot = circle.snapshot()
    print('Initial arrangement:')
    print(initial_snapshot)
    print()
    for i, x in enumerate(initial_snapshot):
        x.move()
        print(f'{i + 1}) moving the {x.number}:')
        print(circle.snapshot())
        print()


def read_grove_coordinates(circle):
    zero = None
    for x in circle.snapshot():
        if x.number == 0:
            zero = x
            break
    current = zero
    a, b, c = 0, 0, 0
    for _ in range(1000):
        current = current.next
        a = current.number
    for _ in range(1000):
        current = current.next
        b = current.number
    for _ in range(1000):
        current = current.next
        c = current.number
    print(a, b, c, a + b + c)


def part_one(filename):
    data = read_puzzle_input(filename)
    circle = parse_puzzle_input(data)
    mix(circle)
    read_grove_coordinates(circle)

    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '20'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
print(f'Answer part one: {part_one(short_filename)}')
print(f'Answer part two: {part_two(short_filename)}')


# class Test(unittest.TestCase):
#     def test_part_one(self):
#         self.assertEqual(-1, part_one(short_filename))
#         self.assertEqual(-1, part_one(long_filename))
#
#     def test_part_two(self):
#         self.assertEqual(-1, part_two(short_filename))
#         self.assertEqual(-1, part_two(long_filename))


class TestNumberCircle(unittest.TestCase):
    def test_insert_after(self):
        a1 = NumberCircle(1)
        a2 = NumberCircle(2)
        a1.insert_after(a2)
        self.assertEqual(2, a1.next.number)
        self.assertEqual(2, a1.prev.number)
        self.assertEqual(1, a2.next.number)
        self.assertEqual(1, a2.prev.number)
        a3 = NumberCircle(3)
        a1.insert_after(a3)
        self.assertEqual(1, a3.prev.number)
        self.assertEqual(2, a3.next.number)

    def test_parse_puzzle_input(self):
        data = read_puzzle_input(short_filename)
        circle = parse_puzzle_input(data)
        self.assertEqual(1, circle.number)
        self.assertEqual(2, circle.next.number)
        self.assertEqual(4, circle.prev.number)
        self.assertEqual(1, circle.prev.next.number)
        self.assertEqual(1, circle.next.prev.number)
