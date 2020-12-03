import numpy
from coordinates import Coordinate

Coordinate.default_order = 'xy'


def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


if __name__ == '__main__':
    lines = read_lines("3.txt")
    mod = len(lines[0])
    slopes = [Coordinate(1, 1), Coordinate(3, 1), Coordinate(5, 1), Coordinate(7, 1), Coordinate(1, 2)]
    pos = Coordinate(0, 0)
    trees = []
    for slope in slopes:
        count = 0
        while pos.y < len(lines):
            if lines[pos.y][pos.x % mod] == '#':
                count += 1
            pos = pos + slope

        print(f'{slope} -> {count}')
        pos = Coordinate(0, 0)
        trees.append(count)

    result = numpy.prod(trees)
    print(f'result: {result}')
