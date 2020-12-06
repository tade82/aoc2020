import string


def read_lines(file_name):
    with open(file_name) as fp:
        return fp.read()


if __name__ == '__main__':
    lines = read_lines("6.txt")
    asked_total = 0
    commonly_asked_total = 0
    groups = map(lambda x: x.splitlines(), lines.split("\n\n"))
    for group in groups:
        asked_questions = set()
        commonly_asked_questions = set(list(string.ascii_lowercase))
        for person in group:
            asked_questions = asked_questions.union(set(list(person)))
            commonly_asked_questions = commonly_asked_questions.intersection(set(list(person)))
        asked_total += len(asked_questions)
        commonly_asked_total += len(commonly_asked_questions)

    print(f'1st result: {asked_total}')
    print(f'2nd result: {commonly_asked_total}')
