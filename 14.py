import itertools


def read_lines(file_name):
    with open(file_name) as fp:
        for blocks in fp.read().split('mask = '):
            if blocks:
                yield ''.join(blocks).splitlines()


def mask_value(val, mask):
    return ''.join([mask[i] if mask[i] != 'X' else val[i] for i in range(len(val))])


def mask_address(addr, mask):
    result = []
    masked = [addr[i] if mask[i] == '0' else mask[i] for i in range(len(addr))]
    for x in itertools.product(['0', '1'], repeat=masked.count('X')):
        result.append(floating(masked.copy(), list(x)))
    return result


def floating(addr, values):
    return ''.join([values.pop(0) if bit == 'X' else bit for bit in addr])


def version1(program_blocks):
    memory = {}
    for block in program_blocks:
        mask = block[0]
        program = block[1:]
        for p in program:
            addr = int(p.split('] = ')[0].replace('mem[', ''))
            val = f"{int(p.split('] = ')[1]):036b}"
            memory[addr] = int(mask_value(val, mask), 2)
    return memory


def version2(program_blocks):
    memory = {}
    for block in program_blocks:
        mask = block[0]
        program = block[1:]
        for p in program:
            addr = int(p.split('] = ')[0].replace('mem[', ''))
            val = int(p.split('] = ')[1])
            for masked_address in mask_address(f"{addr:036b}", mask):
                memory[int(masked_address, 2)] = val
    return memory


if __name__ == '__main__':
    program_blocks = list(read_lines('14.txt'))
    print(f'1st result: {sum(list(version1(program_blocks).values()))}')
    print(f'2nd result: {sum(list(version2(program_blocks).values()))}')
