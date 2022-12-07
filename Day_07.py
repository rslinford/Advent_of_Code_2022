import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


class Tree:
    def __init__(self):
        self.root = Directory('/')
        self.current_dir = self.root
        self.tally = 0

    def __repr__(self):
        rval = [str(self.root)]
        return ''.join(rval)

    def add_entry(self, entry):
        self.current_dir.children.add(entry)
        entry.parent = self.current_dir

    def cd_root(self):
        self.current_dir = self.root

    def cd_parent(self):
        if not self.current_dir.parent:
            raise ValueError(f'cd to parent dir failed. Current dir {self.current_dir} has no parent.')
        self.current_dir = self.current_dir.parent

    def cd(self, name):
        if name == '/':
            self.cd_root()
            return
        if name == '..':
            self.cd_parent()
            return

        for entry in self.current_dir.children:
            if entry.name == name:
                self.current_dir = entry
                return
        raise ValueError(f'Directory by the name {name} not found in dir {self.current_dir.name}')

    def add_dir(self, name):
        self.add_entry(Directory(name))

    def add_file(self, name, size):
        file = File(name, size)
        self.add_entry(file)

    def traverse_dir(self, dir):
        # print(dir, dir.calc_size())
        if dir.calc_size() <= 100000:
            self.tally += dir.calc_size()
        for entry in dir.children:
            if isinstance(entry, Directory):
                self.traverse_dir(entry)

    def traverse_dirs_from_root(self):
        self.tally = 0
        self.traverse_dir(self.root)
        return self.tally


class Entry:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def depth(self):
        n = 0
        entry = self.parent
        while entry:
            n += 1
            entry = entry.parent
        return n


class File(Entry):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        self.parent = None

    def __repr__(self):
        return f'{"   " * self.depth()}- {self.name} (file, size={self.size})'

    def calc_size(self):
        return self.size


class Directory(Entry):
    def __init__(self, name):
        super().__init__(name)
        self.children = set()

    def __repr__(self):
        return f'{"   " * self.depth()}- {self.name} (dir)'

    def repr_recursive(self):
        rval = [f'{"   " * self.depth()}- {self.name} (dir)\n']
        for child in self.children:
            rval.append(f'{child}\n')
        return ''.join(rval)

    def __lt__(self, other):
        return self.name < other.name

    def add_child(self, child):
        self.children.add(child)

    def calc_size(self):
        size = 0
        for entry in self.children:
            size += entry.calc_size()
        return size


def build_tree(data: list[str]):
    tree = Tree()
    for line in data:
        # Commands
        if line[0] == '$':
            if line[2:4] == 'cd':
                name = line[5:]
                tree.cd(name)
            elif line[2:4] == 'ls':
                pass
            else:
                raise ValueError(f'Unrecognized command: {line}')
        # Dir entry
        elif line[0:3] == 'dir':
            name = line[4:]
            tree.add_dir(name)
        # File entry
        else:
            result = re.search('^(\d+) (.*)', line)
            size = int(result.group(1))
            name = result.group(2)
            tree.add_file(name, size)
    return tree


def part_one(filename):
    data = read_puzzle_input(filename)
    tree = build_tree(data)
    # print(tree)
    tally = tree.traverse_dirs_from_root()
    # print('Root size:', tree.root.calc_size())
    return tally


def part_two(filename):
    data = read_puzzle_input(filename)
    return -1


filename = 'Day_07_input.txt'
short_filename = 'Day_07_short_input.txt'
print(f'Answer part one: {part_one(filename)}')
print(f'Answer part two: {part_two(short_filename)}')

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(95437, part_one(short_filename))
        self.assertEqual(1086293, part_one(filename))

    def test_part_two(self):
        self.assertEqual(-1, part_two(short_filename))
        self.assertEqual(-1, part_two(filename))
