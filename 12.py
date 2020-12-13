def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


if __name__ == '__main__':
    lines = read_lines('12.txt')
    instructions = []
    for line in lines:
        instructions.append((line[0], int(line[1:])))

    pos = (0, 0)
    wp = (10, 1)
    dir = 'E'
    dirs = ['E', 'S', 'W', 'N', 'E', 'S', 'W', 'N']
    idirs = ['E', 'N', 'W', 'S', 'E', 'N', 'W', 'S']
    for i in instructions:
        if i[0] == 'F':
            m = (wp[0] * i[1], wp[1] * i[1])
            pos = (pos[0] + m[0], pos[1] + m[1])
        if i[0] == 'E':
            wp = (wp[0] + i[1], wp[1])
        if i[0] == 'W':
            wp = (wp[0] - i[1], wp[1])
        if i[0] == 'N':
            wp = (wp[0], wp[1] + i[1])
        if i[0] == 'S':
            wp = (wp[0], wp[1] - i[1])
        if i[0] == 'L':
            if i[1] == 90:
                wp = (-wp[1], wp[0])
            if i[1] == 180:
                wp = (-wp[0], -wp[1])
            if i[1] == 270:
                wp = (wp[1], -wp[0])
        if i[0] == 'R':
            if i[1] == 90:
                wp = (wp[1], -wp[0])
            if i[1] == 180:
                wp = (-wp[0], -wp[1])
            if i[1] == 270:
                wp = (-wp[1], wp[0])
    print(pos)
    print(f'2nd result: {abs(pos[0]) + abs(pos[1])}')
