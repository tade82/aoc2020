def calculate_nth(cache, stop):
    next, index = 0, len(cache)
    for i in range(stop):
        prev = next
        next = index - cache[next] if cache.get(next) is not None else 0
        cache[prev] = index
        index += 1
        if index == stop:
            return prev


if __name__ == '__main__':
    cache = {n: i for i, n in enumerate([7, 14, 0, 17, 11, 1, 2])}

    print(f'1st result: {calculate_nth(cache.copy(), 2020)}')
    print(f'2nd result: {calculate_nth(cache.copy(), 30000000)}')
