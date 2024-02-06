import numpy as np
import networkx as nx
from time import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


def up_val(ix, iy, alt_map):
    if ord(alt_map[ix - 1, iy]) - ord(alt_map[ix, iy]) > 1:
        return 0
    else:
        return 1


def down_val(ix, iy, alt_map):
    if ord(alt_map[ix + 1, iy]) - ord(alt_map[ix, iy]) > 1:
        return 0
    else:
        return 1


def left_val(ix, iy, alt_map):
    if ord(alt_map[ix, iy - 1]) - ord(alt_map[ix, iy]) > 1:
        return 0
    else:
        return 1


def right_val(ix, iy, alt_map):
    if ord(alt_map[ix, iy + 1]) - ord(alt_map[ix, iy]) > 1:
        return 0
    else:
        return 1


@timer_func
def day12(filepath, if_any=False):
    with open(filepath) as fin:
        alt_map = np.genfromtxt(filepath, delimiter=1, dtype=str)

    start = tuple(np.argwhere(alt_map == 'S')[0])
    end = tuple(np.argwhere(alt_map == 'E')[0])
    alt_map[start] = 'a'
    alt_map[end] = 'z'

    G = nx.DiGraph()

    for ix, iy in np.ndindex(alt_map.shape):
        if ix > 0:
            if up_val(ix, iy, alt_map):
                G.add_edge((ix, iy), (ix - 1, iy))
        if ix < alt_map.shape[0] - 1:
            if down_val(ix, iy, alt_map):
                G.add_edge((ix, iy), (ix + 1, iy))
        if iy > 0:
            if left_val(ix, iy, alt_map):
                G.add_edge((ix, iy), (ix, iy - 1))
        if iy < alt_map.shape[1] - 1:
            if right_val(ix, iy, alt_map):
                G.add_edge((ix, iy), (ix, iy + 1))

    if not if_any:
        steps = nx.dijkstra_path_length(G, start, end)
    else:
        starts = [tuple(x) for x in np.argwhere(alt_map == 'a')]
        results = nx.multi_source_dijkstra(G, starts, end)
        steps = results[0]

    return steps


def main():
    # assert day12('test12') == 31
    print(day12('Day_12_short_input.txt'))

    # assert day12('test12', True) == 29
    print(day12('Day_12_short_input.txt', True))


if __name__ == '__main__':
    main()