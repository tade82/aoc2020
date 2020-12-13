import math


def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


def get_leaves(tree, jolt, leaves_from):
    if not tree[jolt]:
        return 1
    else:
        cnt = 0
        for j in tree[jolt]:
            cnt += get_leaves(tree, j, leaves_from) if leaves_from.get(j) is None else leaves_from[j]
        return cnt


def get_jolts():
    jolts = []
    for line in lines:
        jolts.append(int(line))
    jolts.append(0)
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    return jolts


def jolt_distributions():
    diffs = {}
    for i in range(1, len(jolts)):
        d = jolts[i] - jolts[i - 1]
        diffs[d] = diffs[d] + 1 if diffs.get(d) is not None else 1
    return diffs


def build_tree(jolts):
    tree = {}
    for j in jolts:
        tree[j] = [j + i for i in range(1, 4) if j + i in jolts]
    return tree


if __name__ == '__main__':
    lines = read_lines("10.txt")
    jolts = get_jolts()
    print(f'1st result: {math.prod(jolt_distributions().values())}')

    tree = build_tree(jolts)
    leaves_from = {}
    for jolt in reversed(tree.keys()):
        leaves_from[jolt] = get_leaves(tree, jolt, leaves_from)
    print(f'2nd result: {leaves_from[0]}')


