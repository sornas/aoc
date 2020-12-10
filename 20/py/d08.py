#!/usr/bin/env python3
import aoc20
import sys
from copy import deepcopy


def parse(prog):
    return [((l := line.strip().split())[0], int(l[1])) for line in prog]


def run(prog):
    acc = 0
    loc = 0
    execed = set()
    while loc < len(prog):
        if loc in execed:
            return False, acc
        execed.add(loc)
        inst, offset = prog[loc]
        if inst == "acc":
            acc += offset
            loc += 1
        elif inst == "jmp":
            loc += offset
        else:
            loc += 1
    return True, acc


def pt1(_in):
    return run(parse(_in))[1]


def pt2(_in):
    prog = parse(_in)
    for i in range(len(prog)):
        orig = prog[i]
        inst, offset = orig
        if inst == "jmp":
            prog[i] = ("nop", offset)
        elif inst == "nop":
            prog[i] = ("jmp", offset)
        else:
            continue
        ret, acc = run(prog)
        if ret:
            return acc
        prog[i] = orig


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 8)
    print(pt1(input))
    print(pt2(input))
