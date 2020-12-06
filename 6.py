import string


def read_groups(file_name):
    with open(file_name) as fp:
        for lines in fp.read().split("\n\n"):
            yield lines.splitlines()


if __name__ == '__main__':
    groups = read_groups("6.txt")
    anyone_asked_count = 0
    everyone_asked_count = 0
    for group in groups:
        anyone_asked = set()
        everyone_asked = set(list(string.ascii_lowercase))
        for person in group:
            anyone_asked = anyone_asked.union(set(list(person)))
            everyone_asked = everyone_asked.intersection(set(list(person)))
        anyone_asked_count += len(anyone_asked)
        everyone_asked_count += len(everyone_asked)

    print(f'1st result: {anyone_asked_count}')
    print(f'2nd result: {everyone_asked_count}')
