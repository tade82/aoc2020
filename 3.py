import collections

import numpy


def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


Pos = collections.namedtuple('Pos', 'x y')


def move(a: Pos, b: Pos):
    return Pos(a.x + b.x, a.y + b.y)


if __name__ == '__main__':
    lines = read_lines("3.txt")
    mod = len(lines[0])
    slopes = [Pos(1, 1), Pos(3, 1), Pos(5, 1), Pos(7, 1), Pos(1, 2)]
    pos = Pos(0, 0)
    tree_per_slope = {}
    for slope in slopes:
        count = 0
        while pos.y < len(lines):
            if lines[pos.y][pos.x % mod] == '#':
                count += 1
            pos = move(pos, slope)

        print(f'{slope} -> {count}')
        pos = Pos(0, 0)
        tree_per_slope[slope] = count

    result = numpy.prod(list(tree_per_slope.values()))
    print(f'result: {result}')
