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

"""
1  A Rock      X loose  
2  B Paper     Y draw
3  C Scissors  Z win
"""


def choose_my_move(single_round: (str, str)) -> str:
    my_move = ''
    match single_round[0]:
        case 'A':
            match single_round[1]:
                case 'X':
                    my_move = 'Z'
                case 'Y':
                    my_move = 'X'
                case 'Z':
                    my_move = 'Y'
        case 'B':
            match single_round[1]:
                case 'X':
                    my_move = 'X'
                case 'Y':
                    my_move = 'Y'
                case 'Z':
                    my_move = 'Z'
        case 'C':
            match single_round[1]:
                case 'X':
                    my_move = 'Y'
                case 'Y':
                    my_move = 'Z'
                case 'Z':
                    my_move = 'X'
        case _:
            raise ValueError(f'Expected A, B, or C. Received {single_round[0]}')
    return my_move


def score_round(single_round: (str, str)) -> int:
    score = 0
    match single_round[0]:
        case 'A':
            match single_round[1]:
                case 'X':
                    score += 1
                    score += 3
                case 'Y':
                    score += 2
                    score += 6
                case 'Z':
                    score += 3
        case 'B':
            match single_round[1]:
                case 'X':
                    score += 1
                case 'Y':
                    score += 2
                    score += 3
                case 'Z':
                    score += 3
                    score += 6
        case 'C':
            match single_round[1]:
                case 'X':
                    score += 1
                    score += 6
                case 'Y':
                    score += 2
                case 'Z':
                    score += 3
                    score += 3
        case _:
            raise ValueError(f'Expected A, B, or C. Received {single_round[0]}')
    return score


def calculate_total_score(strategy: list[(str, str)]) -> int:
    score = 0
    for single_round in strategy:
        score += score_round(single_round)
    return score


def translate_strategy(strategy: list[(str, str)]) -> list[(str, str)]:
    translated_strategy = []
    for single_round in strategy:
        my_move = choose_my_move(single_round)
        translated_strategy.append((single_round[0], my_move))
    return translated_strategy


def calculate_score_part_two(strategy: list[(str, str)]) -> int:
    translated_strategy = translate_strategy(strategy)
    return calculate_total_score(translated_strategy)


def part_one(filename):
    data = read_puzzle_input(filename)
    strategy = parse_data(data)
    score = calculate_total_score(strategy)
    return score


def part_two(filename):
    data = read_puzzle_input(filename)
    strategy = parse_data(data)
    score = calculate_score_part_two(strategy)
    return score


print(f'Answer part one: {part_one("Day_02_input.txt")}')
print(f'Answer part two: {part_two("Day_02_input.txt")}')


class Test(unittest.TestCase):
    def test_part_one(self):
        result = part_one('Day_02_short_input.txt')
        self.assertEqual(result, 15)

    def test_score_round_part_one(self):
        self.assertEqual(8, score_round(('A', 'Y')))
        self.assertEqual(1, score_round(('B', 'X')))
        self.assertEqual(6, score_round(('C', 'Z')))

    def test_calculate_score_part_one(self):
        data = read_puzzle_input('Day_02_short_input.txt')
        strategy = parse_data(data)
        self.assertEqual(15, calculate_total_score(strategy))

    def test_choose_my_move(self):
        self.assertEqual('X', choose_my_move(('A', 'Y')))
        self.assertEqual('X', choose_my_move(('B', 'X')))
        self.assertEqual('X', choose_my_move(('C', 'Z')))

    def test_part_two(self):
        result = part_two('Day_02_short_input.txt')
        self.assertEqual(12, result)
