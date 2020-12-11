# -*- coding: utf-8 -*-
"""
Day 9
"""

import itertools

nums = []

with open('input.txt', 'r') as fread:
    for line in fread:
        num = int(line.strip())
        nums.append(num)


# Part 1

def is_sum(tested_num, tested_range):
    combs = itertools.combinations(tested_range, 2)

    for a, b in combs:
        if a + b == tested_num:
            return True

    return False


for i in range(25, len(nums) + 1):
    tested_num = nums[i]
    tested_range = nums[i - 25:i]

    if not is_sum(tested_num, tested_range):
        print(tested_num)
        break


# Part 2

found = False

for i in range(len(nums)):
    tested_range = []

    for j in range(i, len(nums)):
        tested_range.append(nums[j])
        s = sum(tested_range)

        if s == tested_num:
            print(min(tested_range) + max(tested_range))
            found = True
            break

    if found:
        break
