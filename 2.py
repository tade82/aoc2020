def read_lines(file_name):
    with open(file_name) as fp:
        return fp.readlines()


if __name__ == '__main__':
    lines = read_lines("2.txt")
    total = 0
    for line in lines:
        policy = line.split(':')[0]
        num = policy.split(" ")[0]
        p1 = int(num.split('-')[0])
        p2 = int(num.split('-')[1])
        letter = policy.split(" ")[1]
        pwd = line.split(':')[1]
        if (pwd[p1] == letter and pwd[p2] != letter) or (pwd[p1] != letter and pwd[p2] == letter):
            total += 1
    print(total)
