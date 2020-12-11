# -*- coding: utf-8 -*-
"""
Day 8
"""

from dataclasses import dataclass
import re

@dataclass
class Instruction:
    code: str
    arg: int
    has_run: bool = False


@dataclass
class State:
    acc: int = 0
    idx: int = 0
    ins: Instruction = None
    last_idx: int = 0
    last_ins: Instruction = None


REGEX = re.compile(r'(\w{3}) ((?:\+|-)\d+)')
instructions = []


with open('input.txt', 'r') as fread:
    for line in fread:
        if m := REGEX.match(line):
            ins = Instruction(m.group(1), int(m.group(2)))
            instructions.append(ins)

# Part 1

def run(instructions, state):
    while True:
        try:
            state.ins = instructions[state.idx]
        except IndexError:
            # Correct termination
            return True

        if state.ins.has_run:
            print(state.acc)
            return state

        state.ins.has_run = True
        state.last_idx = state.idx
        state.last_ins = state.ins

        if state.ins.code == 'jmp':
            state.idx += state.ins.arg
            continue

        if state.ins.code == 'acc':
            state.acc += state.ins.arg

        state.idx += 1

state = State()
last_state = run(instructions, state)

print(last_state)

# Part 2
last_state.last_ins.has_run = False
last_state.last_ins.code = 'nop'

instructions[last_state.last_idx] = last_state.last_ins

# Reset
for i in range(len(instructions)):
    instructions[i].has_run = False

ret = run(instructions, State())
print(ret)
assert ret == True
