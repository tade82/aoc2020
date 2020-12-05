def read_cards(file_name):
    with open(file_name) as fp:
        return fp.read().splitlines()


if __name__ == '__main__':
    cards = read_cards('5.txt')
    reserved_seats = []
    for card in cards:
        card = card.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        row = int(card[:7], 2)
        seat = int(card[-3:], 2)
        reserved_seats.append(row * 8 + seat)
    print(f'1st result: {max(reserved_seats)}')

    reserved_seats.sort()
    for i in range(1, len(reserved_seats)):
        if reserved_seats[i - 1] == reserved_seats[i] - 2:
            print(f'2nd result: {reserved_seats[i] - 1}')
