import itertools


def read_lines(file_name):
    with open(file_name) as fp:
        snippet = []
        for blocks in fp.read().split('mask = '):
            if blocks:
                yield ''.join(blocks).splitlines()
            # for p in programs:
            # if programs != '':
            #     yield programs.split('\n')[:-1]


def masked_val(val, mask):
    result = []
    for i in range(len(val)):
        if mask[i] != 'X':
            result.append(mask[i])
        else:
            result.append(val[i])
    return ''.join(result)


def masked_addresses(addr, mask):
    result = []
    tmp = []
    for i in range(len(addr)):
        if mask[i] == '0':
            tmp.append(addr[i])
        else:
            tmp.append(mask[i])
    repeat_count = tmp.count('X')
    for x in itertools.product(range(2), repeat=repeat_count):
        copy_tmp = tmp.copy()
        c = 0
        for i in range(len(tmp)):
            if copy_tmp[i] == 'X':
                copy_tmp[i] = str(x[c])
                c += 1
        result.append(''.join(copy_tmp))
    return result


def version1(program_blocks):
    memory = {}
    for block in program_blocks:
        mask = block[0]
        program = block[1:]
        for p in program:
            addr = int(p.split('] = ')[0].replace('mem[', ''))
            val = f"{int(p.split('] = ')[1]):036b}"
            memory[addr] = int(masked_val(val, mask), 2)
    return memory


def version2(program_blocks):
    memory = {}
    for block in program_blocks:
        mask = block[0]
        program = block[1:]
        for p in program:
            addr = int(p.split('] = ')[0].replace('mem[', ''))
            bin_addr = f"{addr:036b}"
            val = int(p.split('] = ')[1])
            for masked_address in masked_addresses(bin_addr, mask):
                memory[int(masked_address, 2)] = val
    return memory


if __name__ == '__main__':
    program_blocks = list(read_lines('14.txt'))
    print(f'1st result: {sum(list(version1(program_blocks).values()))}')
    print(f'2nd result: {sum(list(version2(program_blocks).values()))}')