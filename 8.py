def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


def op(lines, i):
    return lines[i].split(' ')[0]


def arg(lines, i):
    return lines[i].split(' ')[1]


def swap(lines, i):
    if op(lines, i) == 'nop':
        lines[i] = f'jmp {arg(lines, i)}'
    elif op(lines, i) == 'jmp':
        lines[i] = f'nop {arg(lines, i)}'


def execute(lines):
    visited = []
    accumulator = 0
    i = 0
    while i not in visited and i < len(lines):
        visited.append(i)
        op_code = op(lines, i)
        argument = arg(lines, i)
        if op_code == 'nop':
            i += 1
        if op_code == 'jmp':
            i += int(argument)
        if op_code == 'acc':
            accumulator += int(argument)
            i += 1
    return i, accumulator


def execute_with_swap(input):
    for i in range(len(input)):
        lines = input.copy()
        if op(lines, i) != 'acc':
            swap(lines, i)
            ind, accumulator = execute(lines)
            if ind >= len(input):
                return ind, accumulator


if __name__ == '__main__':
    print(f'1st result: {execute(read_lines("8.txt"))}')
    print(f'2nd result: {execute_with_swap(read_lines("8.txt"))}')
