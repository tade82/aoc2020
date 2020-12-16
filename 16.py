import itertools

import numpy


def read_nearby_tickets(file_name):
    with open(file_name) as fp:
        parts = fp.read().split('\n\n')
        ids_by_types = {i.split(': ')[0]: get_ids(i.split(': ')[1]) for i in parts[0].splitlines()}
        my_ticket = [int(i) for i in parts[1].splitlines()[1].split(',')]
        nearby_tickets = []
        for ticket_str in parts[2].splitlines()[1:]:
            nearby_tickets.append([int(ticket) for ticket in ticket_str.split(',')])
        return ids_by_types, my_ticket, nearby_tickets


def get_ids(ranges):
    nums = []
    v1, v2 = ranges.split(' or ')[0].split('-'), ranges.split(' or ')[1].split('-')
    nums += list(range(int(v1[0]), int(v1[1]) + 1))
    nums += list(range(int(v2[0]), int(v2[1]) + 1))
    return nums


def alma(args):
    return len(args)
    pass


def get_valid_tickets():
    errors = []
    valid_tickets = []
    for ticket_ids in nearby_tickets:
        ticket_is_valid = True
        for id in ticket_ids:
            valid = any([id in ids for ids in ids_by_types.values()])
            if not valid:
                errors.append(id)
                ticket_is_valid = False
        if ticket_is_valid:
            valid_tickets.append(ticket_ids)
    return valid_tickets, errors


def get_possible_positions(valid_tickets, ids_by_types):
    possible_positions = {}
    for type, ids in ids_by_types.items():
        possible_positions[type] = []
        for i in range(len(my_ticket)):
            if all(ticket[i] in ids for ticket in valid_tickets):
                possible_positions[type].append(i)
    return possible_positions


def get_types_by_positions(possible_positions_by_types):
    types_by_positions = {}
    while len(types_by_positions) < 20:
        for type, positions in possible_positions_by_types.items():
            l = list(set(positions) - set(types_by_positions.keys()))
            if len(l) == 1:
                types_by_positions[l[0]] = type
    return types_by_positions


if __name__ == '__main__':
    ids_by_types, my_ticket, nearby_tickets = read_nearby_tickets("16.txt")

    valid_tickets, errors = get_valid_tickets()
    print(f'1st result: {sum(errors)}')

    possible_positions_by_types = get_possible_positions(valid_tickets, ids_by_types)
    types_by_positions = get_types_by_positions(possible_positions_by_types)
    my_departures = [my_ticket[k] for k, v in types_by_positions.items() if v.startswith("departure")]
    print(f'2nd result: {numpy.prod(my_departures)}')