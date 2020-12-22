def read_lines(file_name):
    with open(file_name) as fp:
        blocks = fp.read().split('\n\n')
        for block in blocks:
            yield [int(i) for i in block.splitlines()[1:]]


def first(p1, p2):
    combat(p1, p2, 1)
    points = sum([(i + 1) * j for i, j in enumerate(reversed(p1 + p2))])
    print(f'1st result: {points}')


def combat(p1, p2, i, second=False):
    LOG1 = {}
    LOG2 = {}
    while p1 and p2:
        if (LOG1.get(i) and p1 in LOG1[i]) or (LOG2.get(i) and p2 in LOG2[i]):
            return True
        LOG1[i] = LOG1[i] + [p1.copy()] if LOG1.get(i) else [p1.copy()]
        LOG2[i] = LOG2[i] + [p2.copy()] if LOG2.get(i) else [p2.copy()]
        if not p1:
            return False
        if not p2:
            return True
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if second and c1 <= len(p1) and c2 <= len(p2):
            i += 1
            if combat(p1.copy()[:c1], p2.copy()[:c2], i):
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
            LOG1[i] = []
            i -= 1
        elif c1 < c2:
            p2.append(c2)
            p2.append(c1)
        else:
            p1.append(c1)
            p1.append(c2)
    return bool(p1)


def second(p1, p2):
    combat(p1, p2, 1, second=True)
    points = sum([(i + 1) * j for i, j in enumerate(reversed(p1 + p2))])
    print(f'2nd result: {points}')


if __name__ == '__main__':
    p1, p2 = read_lines("22.txt")
    first(p1.copy(), p2.copy())
    second(p1.copy(), p2.copy())
