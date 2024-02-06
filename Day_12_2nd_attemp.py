import unittest
from collections import deque

from colorama import Fore


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


def parse_data(data: str):
    return [list(a) for a in data.splitlines()]


class Graph:
    def __init__(self, grid):
        self.grid = grid

    def find_start(self):
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if col == 'S':
                    return x, y
        assert False

    def find_starts(self):
        starts = []
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if col == 'S' or col == 'a':
                    starts.append((x, y))
        return starts

    def find_end(self):
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if col == 'E':
                    return x, y
        assert False

    def in_bounds(self, location):
        x, y = location
        height = len(self.grid)
        width = len(self.grid[0])
        return (0 <= x < width) and (0 <= y < height)

    def elevation_at(self, location):
        x, y = location
        match self.grid[y][x]:
            case 'S':
                c = 'a'
            case 'E':
                c = 'z'
            case _:
                c = self.grid[y][x]
        return ord(c) - ord('a')

    def print_grid(self, x_curr, y_curr, visited):
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if x == x_curr and y == y_curr:
                    print(Fore.RED + col, end='')
                elif (x, y) in visited:
                    print(Fore.BLUE + col, end='')
                else:
                    print(Fore.LIGHTWHITE_EX + col, end='')
            print()

    def neighbors(self, location):
        x, y = location
        target_locations = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        target_locations = list(filter(self.in_bounds, target_locations))
        rval = []
        for target_location in target_locations:
            climb = self.elevation_at(target_location) - self.elevation_at(location)
            if climb <= 1:
                rval.append(target_location)
        return rval


def bfs(graph, start, end):
    frontier = deque()
    frontier.append(start)
    came_from = dict()
    came_from[start] = None
    while frontier:
        current = frontier.popleft()
        if current == end:
            break
        for next_loc in graph.neighbors(current):
            if next_loc not in came_from:
                frontier.append(next_loc)
                came_from[next_loc] = current
    return came_from


def reconstruct_path(came_from, start, end):
    if end not in came_from:
        return None
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


def part_one(filename):
    data = read_puzzle_input(filename)
    grid = parse_data(data)
    graph = Graph(grid)
    came_from = bfs(graph, graph.find_start(), graph.find_end())
    path = reconstruct_path(came_from, graph.find_start(), graph.find_end())
    return len(path)


def part_two(filename):
    data = read_puzzle_input(filename)
    grid = parse_data(data)
    graph = Graph(grid)
    starts = graph.find_starts()
    end = graph.find_end()
    shortest = float('inf')
    for start in starts:
        came_from = bfs(graph, start, end)
        path = reconstruct_path(came_from, start, end)
        if path:
            shortest = min(shortest, len(path))
    return shortest


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(425, part_one('Day_12_input.txt'))
        self.assertEqual(31, part_one('Day_12_short_input.txt'))

    def test_part_two(self):
        self.assertEqual(418, part_two('Day_12_input.txt'))
        self.assertEqual(29, part_two('Day_12_short_input.txt'))
