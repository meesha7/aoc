# -*- coding: utf-8 -*-
"""

"""

import re

REGEX = re.compile(r'(\d+)\-(\d+) ([a-z]): ([a-z]+)')


def valid_password(cnt, char, pwd):
    return int(pwd[cnt[0] - 1] == char) + int(pwd[cnt[1] - 1] == char) == 1

with open('input.txt', 'r') as fread:
    valid_passwords = 0

    for line in fread:
        m = REGEX.search(line)

        if m:
            range_low = int(m.group(1))
            range_high = int(m.group(2))
            char = m.group(3)
            pwd = m.group(4)

            if valid_password((range_low, range_high), char, pwd):
                valid_passwords += 1

print(valid_passwords)
