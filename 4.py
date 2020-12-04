import re


def read_passports(file_name):
    with open(file_name) as fp:
        return fp.read().split('\n\n')


def validate(passports, with_value_check=False):
    rules = {
        'byr': (lambda x: 1920 <= int(x) <= 2002),
        'iyr': (lambda x: 2010 <= int(x) <= 2020),
        'eyr': (lambda x: 2020 <= int(x) <= 2030),
        'hgt': (lambda x: 150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' else 59 <= int(x[:-2]) <= 76 if x[-2:] == 'in' else False),
        'hcl': (lambda x: re.search('^#[0-9a-f]{6}$', x) is not None),
        'ecl': (lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
        'pid': (lambda x: re.search('^[0-9]{9}$', x) is not None),
        'cid': (lambda x: True)
    }
    result = 0
    for passport in passports:
        fields = {'cid': None}
        for field in passport.replace('\n', ' ').split(' '):
            fk = field.split(':')[0]
            fv = field.split(':')[1]
            if not with_value_check or rules[fk](fv):
                fields[fk] = fv

        if set(rules.keys()).issubset(fields.keys()):
            result += 1
    return result


if __name__ == '__main__':
    passports = read_passports('4.txt')
    print(f'1st result: {validate(passports)}')
    print(f'2nd result: {validate(passports, with_value_check=True)}')

