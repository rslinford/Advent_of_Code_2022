import re
import unittest


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = set()
        self.add_current_to_history()

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def add_current_to_history(self):
        self.history.add((self.x, self.y))

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

    def is_at(self, p):
        return self.x == p[0] and self.y == p[1]

    def has_been_at(self, p):
        return p in self.history


class RopeSimulator():
    def __init__(self, length):
        self.start = Point(0, 0)
        self.knots = [Point(self.start.x, self.start.y) for _ in range(length)]
        # self.head = Point(self.start.x, self.start.y)
        # self.tail = Point(self.start.x, self.start.y)

    def __repr__(self):
        head_index = 0
        rval = []
        for y in range(-20, 20):
            if len(rval) > 0:
                rval.append('\n')
            for x in range(-20, 20):
                p = (x, y)
                if self.knots[head_index].is_at(p):
                    rval.append('H')
                    continue
                marked = False
                for tail_index in range(head_index+1, len(self.knots)):
                    if self.knots[tail_index].is_at(p):
                        rval.append(str(tail_index))
                        marked = True
                        break
                if marked:
                    continue
                if self.start.is_at(p):
                    rval.append('s')
                    continue
                if self.knots[head_index + 1].has_been_at(p):
                    rval.append('#')
                    continue
                rval.append('.')

        return ''.join(rval)

    def move_head_right(self, head_index):
        self.knots[head_index].move_right()
        self.knots[head_index].add_current_to_history()
        self.consider_tail(head_index)

    def move_head_left(self, head_index):
        self.knots[head_index].move_left()
        self.knots[head_index].add_current_to_history()
        self.consider_tail(head_index)

    def move_head_up(self, head_index):
        self.knots[head_index].move_up()
        self.knots[head_index].add_current_to_history()
        self.consider_tail(head_index)

    def move_head_down(self, head_index):
        self.knots[head_index].move_down()
        self.knots[head_index].add_current_to_history()
        self.consider_tail(head_index)

    def head_and_tail_delta(self, head_index):
        return self.knots[head_index].x - self.knots[head_index + 1].x, \
               self.knots[head_index].y - self.knots[head_index + 1].y

    def head_and_tail_touch(self, head_index):
        delta_x, delta_y = self.head_and_tail_delta(head_index)
        return abs(delta_x) < 2 and abs(delta_y) < 2

    def consider_tail(self, head_index):
        if head_index >= len(self.knots) - 1:
            return
        tail_index = head_index + 1
        if self.head_and_tail_touch(head_index):
            return self.consider_tail(head_index+1)
        delta_x, delta_y = self.head_and_tail_delta(head_index)
        # Non-diagonal
        if delta_x == 0:
            assert abs(delta_y) == 2
            if delta_y > 0:
                self.knots[tail_index].move_down()
            else:
                self.knots[tail_index].move_up()
            self.knots[tail_index].add_current_to_history()
            return self.consider_tail(head_index+1)
        elif delta_y == 0:
            assert abs(delta_x) == 2
            if delta_x < 0:
                self.knots[tail_index].move_left()
            else:
                self.knots[tail_index].move_right()
            self.knots[tail_index].add_current_to_history()
            return self.consider_tail(head_index+1)
        # Diagonal
        assert abs(delta_x) > 0
        assert abs(delta_y) > 0
        if delta_y > 0:
            self.knots[tail_index].move_down()
        else:
            self.knots[tail_index].move_up()
        if delta_x < 0:
            self.knots[tail_index].move_left()
        else:
            self.knots[tail_index].move_right()
        self.knots[tail_index].add_current_to_history()
        return self.consider_tail(head_index+1)


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def follow_directions(rs, data):
    for line in data:
        # print(rs)
        # print()
        # print(line)
        result = re.search('^(.) (\d+)$', line)
        direction = result.group(1)
        distance = int(result.group(2))
        for n in range(distance):
            for head_index in range(len(rs.knots) - 1):
                if head_index == 0:
                    match direction:
                        case 'U':
                            rs.move_head_up(head_index)
                        case 'D':
                            rs.move_head_down(head_index)
                        case 'L':
                            rs.move_head_left(head_index)
                        case 'R':
                            rs.move_head_right(head_index)
                        case _:
                            raise ValueError(f'Expected U, D, L, or R but got {direction}')
                else:
                    rs.consider_tail(head_index)
            # print(f'Turn {n}')
            # print(rs)
            # print()
    # print(rs)


def part_one(filename):
    rs = RopeSimulator(2)
    data = read_puzzle_input(filename)
    follow_directions(rs, data)
    return len(rs.knots[-1].history)


def part_two(filename):
    rs = RopeSimulator(10)
    data = read_puzzle_input(filename)
    follow_directions(rs, data)
    return len(rs.knots[-1].history)


filename = 'Day_09_input.txt'
short_filename = 'Day_09_short_input.txt'
short_filename_two = 'Day_09_short_input_two.txt'
# print(f'Answer part one: {part_one(short_filename)}')
# print(f'Answer part two: {part_two(short_filename)}')

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(13, part_one(short_filename))
        self.assertEqual(88, part_one(short_filename_two))
        self.assertEqual(5902, part_one(filename))

    def test_part_two(self):
        self.assertEqual(1, part_two(short_filename))
        self.assertEqual(36, part_two(short_filename_two))
        self.assertEqual(2445, part_two(filename))
