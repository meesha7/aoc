# -*- coding: utf-8 -*-
"""

"""

import re

REGEX = re.compile(r'(\w+ \w+) bags contain')

bags = {}

with open('input.txt', 'r') as fread:
    for line in fread:
        line = line.strip()
        m = REGEX.match(line)
        src = m.group(1)
        the_rest = line[m.span(1)[1] + 2 + len('bags contain'):].replace('.', '')
        holds = the_rest.split(', ')

        if holds[0] == 'no other bags':
            bags[src] = {}
            continue

        holds_parsed = {}

        for hold in holds:
            holds_parsed[str(hold[2:])] = int(hold[0])

        bags[src] = holds_parsed

print(bags)
