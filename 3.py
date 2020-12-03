def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


def move(pos, slope):
    return (pos[0] + slope[0], pos[1] + slope[1])


if __name__ == '__main__':
    lines = read_lines("3.txt")
    mod = len(lines[0])
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    pos = (0, 0)
    tree_per_slope = {}
    for slope in slopes:
        count = 0
        while pos[1] < len(lines):
            if lines[pos[1]][pos[0] % mod] == '#':
                count += 1
            pos = move(pos, slope)

        print(f'{slope} -> {count}')
        pos = (0, 0)
        tree_per_slope[slope] = count

    result = 1
    for slope, count in tree_per_slope.items():
        result *= count
    print(f'result: {result}')
