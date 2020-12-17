import itertools


def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


def print_space(s, l):
    for z in range(-6, l+6):
        print(z)
        for x in range(-6, l+6):
            for y in range(-6, l+6):
                print(s[(x, y, z)], end='')
            print('')


def neighbors(k):
    neighbors = []
    for x, y, z, w in itertools.product(range(-1, 2), range(-1, 2), range(-1, 2), range(-1, 2)):
        if (x, y, z, w) != (0, 0, 0, 0):
            neighbors.append((k[0] + x, k[1] + y, k[2] + z, k[3] + w))
    return neighbors


if __name__ == '__main__':
    lines = read_lines("17.txt")
    l = len(lines[0])
    space = {}
    for x, y, z, w in itertools.product(range(-6, l+6), range(-6, l+6), range(-6, l+6), range(-6, l+6)):
        space[(x, y, z, w)] = lines[x][y] if z == 0 and w == 0 and x in range(l) and y in range(l) else '.'

    for i in range(6):
        tmp = space.copy()
        for k, v in space.items():
            if v == '#' and len([space[i] for i in neighbors(k) if space.get(i) and space[i] == '#']) not in [2, 3]:
                tmp[k] = '.'
            if v == '.' and len([space[i] for i in neighbors(k) if space.get(i) and space[i] == '#']) == 3:
                tmp[k] = '#'
        space = tmp

    print(f'2nd result: {sum([1 for i in space.values() if i == "#"])}')
