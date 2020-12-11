# -*- coding: utf-8 -*-
"""
Day 6
"""

groups = []

with open('input.txt', 'r') as fread:
    group = None

    for line in fread:
        if line != '\n':
            if group is None:
                group = set(line.strip())
            else:
                group &= set(line.strip())

        if line == '\n':
            groups.append(group)
            group = None
            continue
    else:
        groups.append(group)

print(sum([len(x) for x in groups]))
