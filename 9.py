def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


def the_number():
    for i in range(25, len(lines)):
        found = False
        num = int(lines[i])
        for j in range(i - 25, i - 1):
            for k in range(j + 1, i):
                if int(lines[j]) + int(lines[k]) == num:
                    found = True
        if not found:
            return num


def find_weakness(num):
    for i in range(0, lines.index(str(num)) - 1):
        sum = int(lines[i])
        acc = [int(lines[i])]
        for j in range(i + 1, lines.index(str(num))):
            sum += int(lines[j])
            acc.append(int(lines[j]))
            if sum < num:
                continue
            if sum == num:
                return min(acc) + max(acc)


if __name__ == '__main__':
    lines = read_lines("9.txt")
    num = the_number()
    print(f'1st result: {num}')
    print(f'2nd result: {find_weakness(num)}')




