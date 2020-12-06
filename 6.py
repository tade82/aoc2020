import string


def read_groups(file_name):
    with open(file_name) as fp:
        for lines in fp.read().split("\n\n"):
            yield lines.splitlines()


if __name__ == '__main__':
    groups = read_groups("6.txt")
    anyone_count = 0
    everyone_count = 0
    for group in groups:
        anyone = set()
        everyone = set(list(string.ascii_lowercase))
        for person in group:
            anyone = anyone.union(set(list(person)))
            everyone = everyone.intersection(set(list(person)))
        anyone_count += len(anyone)
        everyone_count += len(everyone)

    print(f'1st result: {anyone_count}')
    print(f'2nd result: {everyone_count}')
