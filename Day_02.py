import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


def parse_data(data: str) -> list[(str, str)]:
    rval: list[(str, str)] = []
    for line in data.splitlines():
        rval.append((line[0], line[2]))
    return rval


def score_round(round: (str, str)) -> int:
    score = 0
    match round[0]:
        case 'A':
            match round[1]:
                case 'X':
                    score += 1
                    score += 3
                case 'Y':
                    score += 2
                    score += 6
                case 'Z':
                    score += 3
        case 'B':
            match round[1]:
                case 'X':
                    score += 1
                case 'Y':
                    score += 2
                    score += 3
                case 'Z':
                    score += 3
                    score += 6
        case 'C':
            match round[1]:
                case 'X':
                    score += 1
                    score += 6
                case 'Y':
                    score += 2
                case 'Z':
                    score += 3
                    score += 3
        case _:
            raise ValueError(f'Expected A, B, or C. Received {round[0]}')
    return score


def calculate_score(strategy: list[(str, str)]) -> int:
    score = 0
    for round in strategy:
        score += score_round(round)
    return score


def part_one(filename):
    data = read_puzzle_input(filename)
    strategy = parse_data(data)
    score = calculate_score(strategy)
    return score


class Test(unittest.TestCase):
    def test_part_one(self):
        result = part_one('Day_02_short_input.txt')
        self.assertEqual(result, 15)

    def test_score_round(self):
        self.assertEqual(8, score_round(('A', 'Y')))
        self.assertEqual(1, score_round(('B', 'X')))
        self.assertEqual(6, score_round(('C', 'Z')))

    def test_calculate_score(self):
        data = read_puzzle_input('Day_02_short_input.txt')
        strategy = parse_data(data)
        self.assertEqual(15, calculate_score(strategy))
