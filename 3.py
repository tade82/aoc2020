import numpy
from coordinates import Coordinate

Coordinate.default_order = 'xy'


def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


def count_trees(*slopes):
    lines = read_lines("3.txt")
    mod = len(lines[0])
    pos = Coordinate(0, 0)
    trees = []
    for slope in slopes:
        count = 0
        while pos.y < len(lines):
            if lines[pos.y][pos.x % mod] == '#':
                count += 1
            pos = pos + slope

        pos = Coordinate(0, 0)
        trees.append(count)
    return numpy.prod(trees)


if __name__ == '__main__':
    print(f'1st result: {count_trees(Coordinate(3, 1))}')
    print(f'2nd result: {count_trees(Coordinate(1, 1), Coordinate(3, 1), Coordinate(5, 1), Coordinate(7, 1), Coordinate(1, 2))}')
