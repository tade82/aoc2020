import itertools


def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


def adj(waiting_area, i):
    ret = {}
    for x, y in itertools.product([1, 0, -1], [1, 0, -1]):
        if 0 <= i[0] + x <= width and 0 <= i[1] + y <= length and (i[0] + x, i[1] + y) != i:
            ret[(i[0] + x, i[1] + y)] = waiting_area[(i[0] + x, i[1] + y)]
    return ret


def visible(waiting_area, i):
    ret = {}
    for x, y in itertools.product([1, 0, -1], [1, 0, -1]):
        for a in range(1, 100):
            if 0 <= i[0] + x * a <= width and 0 <= i[1] + y * a <= length and (i[0] + x * a, i[1] + y * a) != i:
                ret[(i[0] + x * a, i[1] + y * a)] = waiting_area[(i[0] + x * a, i[1] + y * a)]
                if waiting_area[(i[0] + x * a, i[1] + y * a)] == '#' or waiting_area[
                    (i[0] + x * a, i[1] + y * a)] == 'L':
                    break
    return ret


def stable_waiting_area(waiting_area, fn, tolerate):
    while True:
        tmp = {}
        for i in waiting_area:
            if waiting_area[i] == 'L' and '#' not in fn(waiting_area, i).values():
                tmp[i] = '#'
            elif waiting_area[i] == '#' and list(fn(waiting_area, i).values()).count('#') >= tolerate:
                tmp[i] = 'L'
            else:
                tmp[i] = waiting_area[i]
        if waiting_area == tmp:
            break
        waiting_area = tmp
    return waiting_area


def get_waiting_area():
    global width, length
    waiting_area = {}
    for i in range(len(lines)):
        width = i
        for j in range(len(lines[i])):
            waiting_area[(i, j)] = lines[i][j]
            length = j
    return waiting_area


if __name__ == '__main__':
    lines = read_lines("11.txt")
    waiting_area = get_waiting_area()

    print(f'1st result: {list(stable_waiting_area(waiting_area, adj, 4).values()).count("#")}')
    print(f'2nd result: {list(stable_waiting_area(waiting_area, visible, 5).values()).count("#")}')
