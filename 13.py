import math


def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


def lcm(x, y):
    return x * y // math.gcd(x, y)


if __name__ == '__main__':
    lines = read_lines("13.txt")
    timestamp = int(lines[0])
    buses = lines[1].split(',')
    minimum = 1000000000
    bus_num = -1
    offset = {}
    o = 0
    for bus in buses:
        if bus != 'x':
            offset[int(bus)] = o
            d = int(bus) - timestamp % int(bus)
            if d < minimum:
                minimum = d
                bus_num = int(bus)
        o += 1
    inc, t = list(offset.items())[0]
    while not all((t + v) % k == 0 for k, v in offset.items()):
        a = [(t + v) % k == 0 for k, v in offset.items()]
        if a[1]:
            print(a)
            fk, fv = list(offset.items())[1]
            sk, sv = list(offset.items())[2]
            print(f'{t} = {t / inc}*{inc} || {t + fv} = {(t + fv) / fk}*{fk} || {t + sv} = {(t + sv) / sk}*{sk}')
            inc = lcm(list(offset.keys())[0], list(offset.keys())[1])
            if a[2]:
                inc = lcm(inc, list(offset.keys())[2])
                if a[3]:
                    inc = lcm(inc, list(offset.keys())[3])
                    if a[4]:
                        inc = lcm(inc, list(offset.keys())[4])
                        if a[5]:
                            inc = lcm(inc, list(offset.keys())[5])
                            if a[6]:
                                inc = lcm(inc, list(offset.keys())[6])
                                if a[7]:
                                    inc = lcm(inc, list(offset.keys())[7])


        t += inc
    print(t)
