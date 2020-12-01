def read_lines(file_name):
    with open(file_name) as fp:
        return fp.readlines()


def expense(index):
    return int(lines[index])


if __name__ == '__main__':
    lines = read_lines("1.txt")
    result = 0
    for i in range(0,len(lines)):
        for j in range(i,len(lines)):
            for k in range(j, len(lines)):
                if expense(i) + expense(j) + expense(k) == 2020:
                    result = expense(i) * expense(j) * expense(k)
    print(result)
