# -*- coding: utf-8 -*-
"""
Day 10
"""

from math import factorial as fact
import itertools
from tqdm import tqdm

adapters = []

with open('input.txt', 'r') as fread:
    for line in fread:
        adapters.append(int(line.strip()))


def part1(adapters):
    max_rating = max(adapters) + 3

    adapters.insert(0, 0)
    adapters.insert(len(adapters), max_rating)
    adapters.sort()

    diffs_1 = 0
    diffs_3 = 0

    for i in range(len(adapters)):
        try:
            d = adapters[i + 1] - adapters[i]
        except IndexError:
            break

        if d == 1:
            diffs_1 += 1
        elif d == 3:
            diffs_3 += 1

    return diffs_1*diffs_3


test_input_small = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
test_input = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
              38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

assert part1(test_input[:]) == 220
print(part1(adapters[:]))


def is_valid(adapters):
    for i in range(len(adapters)):
        try:
            d = adapters[i + 1] - adapters[i]

            if d > 3:
                return False
        except IndexError:
            return True

    return True


def part2(adapters):
    adapters.sort()
    print(adapters)

    shortest_path = [adapters[0]]

    i = 0

    while i < len(adapters):
        curr = adapters[i]

        if i < len(adapters) - 3:
            n = (adapters[i + 1], adapters[i + 2], adapters[i + 3])
            d = (n[0] - curr, n[1] - curr, n[2] - curr)
        elif i < len(adapters) - 2:
            n = (adapters[i + 1], adapters[i + 2])
            d = (n[0] - curr, n[1] - curr)
        elif i < len(adapters) - 1:
            n = (adapters[i + 1], )
            d = (n[0] - curr, )
        else:
            break

        print(n, d)

        if 3 in d:
            jmp = d.index(3)
        elif 2 in d:
            jmp = d.index(2)
        elif 1 in d:
            jmp = d.index(1)

        shortest_path.append(n[jmp])

        i += jmp + 1

    print(shortest_path)
    skipped = list(set(adapters) - set(shortest_path))
    print(skipped)

    # c = 0

    # for n in range(1, len(skipped)):
    #     c += len(list(itertools.combinations(skipped, n)))

    # print(c)

    # return 2 + fact(len(skipped) + 1)/(fact(2)*fact(len(skipped) + 1 - 2))

    cnt = 0

    for i in tqdm(range(len(adapters))):
        c = list(itertools.combinations(skipped, i))

        for cc in c:
            new = shortest_path.copy()
            new += list(cc)
            new.sort()

            print(new)

            if is_valid(new):
                cnt += 1

    print(cnt)
    return cnt


assert part2(test_input_small) == 8
print(part2(test_input))
assert part2(test_input) == 19208
