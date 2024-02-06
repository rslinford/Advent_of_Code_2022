import math
import re
from itertools import permutations
from typing import Tuple

from numpy import asarray, diagonal, ndarray


class Valve:
    def __init__(self, label, flow_rate):
        self.label = label
        self.flow_rate = flow_rate
        self.neighbors = []
        self.is_open = False

    def __repr__(self):
        return f'Valve({self.label}, {self.flow_rate}, {self.neighbors})'

    def __lt__(self, other):
        return self.label < other.label


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def parse_lines(data: list[str]) -> list[Valve]:
    rval = []
    for line in data:
        result = re.search(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
        label = result.group(1)
        flow_rate = int(result.group(2))
        neighbors = result.group(3)
        valve = Valve(label, flow_rate)
        for v in neighbors.strip().split(', '):
            valve.neighbors.append(v)
        rval.append(valve)
        rval.sort()
    return rval


# def breadth_first_search_recursive(valves: dict[str, Valve], valve_label: str, visited_valves):
#     if valve_label in visited_valves:
#         return
#     visited_valves.add(valve_label)
#     print(f'Visiting {valve_label}')
#     for neighbor_label in valves[valve_label].neighbors:
#         breadth_first_search_recursive(valves, neighbor_label, visited_valves)


def initialize_adjacency_matrix(n):
    m = [[math.inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        m[i][i] = 0
    return m


def look_up_index(label: str, valves: list[Valve]):
    for index in range(len(valves)):
        if valves[index].label == label:
            return index
    raise ValueError(f'Label {label} not found.')


def check_and_convert_adjacency_matrix(adjacency_matrix):
    mat = asarray(adjacency_matrix)
    (nrows, ncols) = mat.shape
    assert nrows == ncols
    n = nrows
    assert (diagonal(mat) == 0.0).all()
    return (mat, n)


def floyd_warshall_inplace(adjacency_matrix):
    (mat, n) = check_and_convert_adjacency_matrix(adjacency_matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[i, j] = min(mat[i, j], mat[i, k] + mat[k, j])

    return mat


def create_adjacency_matrix(valves: list[Valve]):
    n = len(valves)
    m = initialize_adjacency_matrix(n)
    for i in range(n):
        for adjacent_label in valves[i].neighbors:
            adjacent_index = look_up_index(adjacent_label, valves)
            m[i][adjacent_index] = 1
    return m


# def breadth_first_search(valves):
#     breadth_first_search_recursive(valves, 'AA', set())

def list_valves_that_flow(valves: list[Valve]) -> list[str]:
    return [valve.label for valve in valves if valve.flow_rate > 0]


def calculate_total_flow_for(ordering: Tuple[str, ...], valves: list[Valve], distance_matrix: ndarray):
    current_label = 'AA'
    remaining_minutes = 30
    flow = 0
    for next_label in ordering:
        current_index = look_up_index(current_label, valves)
        next_index = look_up_index(next_label, valves)
        distance = distance_matrix[current_index][next_index]
        remaining_minutes -= distance + 1
        if remaining_minutes <= 0:
            break
        flow += valves[next_index].flow_rate * remaining_minutes
        current_label = next_label
    return flow


def part_one(filename):
    data = read_puzzle_input(filename)
    valves = parse_lines(data)
    # breadth_first_search(valves)
    adjacency_matrix = create_adjacency_matrix(valves)
    distance_matrix = floyd_warshall_inplace(adjacency_matrix)
    print(asarray(adjacency_matrix))
    print(distance_matrix)
    flow_valves = list_valves_that_flow(valves)
    # result = [x for x in product(flow_valves, repeat=5) if all(x[i - 1] != x[i] for i in range(1, len(x)))]
    max_flow = -math.inf
    total_perms = math.factorial(len(flow_valves))
    counter = 1
    print(f'Looping through {total_perms} orderings.')
    for ordering in permutations(flow_valves):
        flow = calculate_total_flow_for(ordering, valves, distance_matrix)
        counter += 1
        if counter % 10000000 == 0:
            print(f'Percent done: {counter/total_perms}')
        if flow > max_flow:
            max_flow = flow
            print(ordering, flow, max_flow)

    return -1


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


day_of_month = '16'
long_filename = f'Day_{day_of_month}_long_input.txt'
short_filename = f'Day_{day_of_month}_short_input.txt'
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
