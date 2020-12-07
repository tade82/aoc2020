def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


def parse_rules(lines):
    rules = {}
    for line in lines:
        outer = line.split(" bags contain ")[0]
        rules[outer] = []
        inner_bags = line.split(" bags contain ")[1].split(', ')
        for ib in inner_bags:
            if ib != 'no other bags.':
                rules[outer].append((ib.split(' ')[0], ib.split(' ')[1] + " " + ib.split(' ')[2]))
    return rules


def bags_with_shiny_gold_in_it(rules):
    count = 0
    for k, v in rules.items():
        if k == 'shiny gold':
            pass
        tmp = v.copy()
        l = len(tmp)
        i = 0
        while i < l:
            bag = tmp[i][1]
            if bag == 'shiny gold':
                count += 1
                break
            for n in rules[bag]:
                tmp.append(n)
            l = len(tmp)
            i += 1
    return count


def bags_in_shiny_golden(rules):
    shiny_bag = rules['shiny gold']
    l = len(shiny_bag)
    i = 0
    while i < l:
        elem = shiny_bag[i]
        inner = elem[1]
        count = int(elem[0])
        for n in rules[inner]:
            shiny_bag.append((count * int(n[0]), n[1]))
        l = len(shiny_bag)
        i += 1

    count = 0
    for i in shiny_bag:
        count += int(i[0])
    return count


if __name__ == '__main__':
    lines = read_lines("7.txt")
    rules = parse_rules(lines)
    print(f'1st result: {bags_with_shiny_gold_in_it(rules)}')
    print(f'2ndt result: {bags_in_shiny_golden(rules)}')
