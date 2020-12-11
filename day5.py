# -*- coding: utf-8 -*-
"""
Day 5
"""

with open('input.txt', 'r') as fread:
    boarding_passes = [x.strip() for x in fread]


def parse(boarding_pass):
    row_part = boarding_pass[:7]
    col_part = boarding_pass[7:]

    size = 128
    low = 0
    high = 127

    c_size = 8
    c_low = 0
    c_high = 7

    for c in row_part:
        if c == 'F':
            size = size/2
            high -= size
        elif c == 'B':
            size = size/2
            low += size

    row = int(low)

    for c in col_part:
        if c == 'L':
            c_size = c_size/2
            c_high -= c_size
        elif c == 'R':
            c_size = c_size/2
            c_low += c_size

    col = int(c_low)

    sid = row*8 + col

    return sid


assert parse('BFFFBBFRRR') == 567
assert parse('FFFBBBFRRR') == 119
assert parse('BBFFBBFRLL') == 820

sids = []

for boarding_pass in boarding_passes:
    sid = parse(boarding_pass)
    sids.append(sid)

print(max(sids))

print(set(range(min(sids) - 1, max(sids) + 2)) - set(sids))
