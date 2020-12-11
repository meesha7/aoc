# -*- coding: utf-8 -*-
"""

"""

import re

REGEX = re.compile(r'(\w+):([\w\d#]+)')
CLR_REGEX = re.compile(r'#[\da-fA-F]{6}')

with open('input.txt', 'r') as fread:
    lines = fread.readlines()

passports = []
passport_data = {}

for line in lines:
    if line == '\n':
        passports.append(passport_data)
        passport_data = {}
        continue

    m = re.findall(REGEX, line)

    for key, val in m:
        passport_data[key] = val


req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def validate(passport_data):
    fields = set(passport_data.keys())

    missing_fields = req_fields - fields

    if missing_fields:
        return False

    if len(passport_data['byr']) != 4:
        return False

    if len(passport_data['iyr']) != 4:
        return False

    if len(passport_data['eyr']) != 4:
        return False

    if int(passport_data['byr']) < 1920:
        return False

    if int(passport_data['byr']) > 2002:
        return False

    if int(passport_data['iyr']) < 2010:
        return False

    if int(passport_data['iyr']) > 2020:
        return False

    if int(passport_data['eyr']) < 2020:
        return False

    if int(passport_data['eyr']) > 2030:
        return False

    if 'cm' in passport_data['hgt']:
        if int(passport_data['hgt'].replace('cm', '')) < 150:
            return False

        if int(passport_data['hgt'].replace('cm', '')) > 193:
            return False
    elif 'in' in passport_data['hgt']:
        if int(passport_data['hgt'].replace('in', '')) < 59:
            return False

        if int(passport_data['hgt'].replace('in', '')) > 76:
            return False
    else:
        return False

    if not CLR_REGEX.match(passport_data['hcl']):
        return False

    if passport_data['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    if len(passport_data['pid']) != 9:
        return False

    return True

valid = 0

for passport_data in passports:
    if validate(passport_data):
        valid += 1

print(valid)
