#!/usr/bin/env python3
import sys


def pt1(_in):
    acc = 0
    loc = 0
    execed = set()
    while True:
        if loc in execed:
            return acc
        execed.add(loc)
        inst, offset = _in[loc][:-1].split() # \n
        offset = int(offset)
        if inst == "acc":
            acc += offset
            loc += 1
        elif inst == "jmp":
            loc += offset
        else:
            loc += 1


def pt2(_in):
    def run(prog):
        acc = 0
        loc = 0
        execed = set()
        while loc < len(prog):
            if loc in execed:
                return False, acc
            execed.add(loc)
            inst, offset = prog[loc].strip().split()
            offset = int(offset)
            if inst == "acc":
                acc += offset
                loc += 1
            elif inst == "jmp":
                loc += offset
            else:
                loc += 1
        return True, acc

    for i in range(len(_in)):
        prog = _in.copy()
        inst, offset = prog[i].strip().split()
        if inst == "jmp":
            prog[i] = "nop 0"
        elif inst == "nop":
            prog[i] = f"jmp {offset}"
        else:
            continue
        ret, acc = run(prog)
        if ret:
            return acc


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = open(sys.argv[1], "r").readlines()
    else:
        input = open("../input/08", "r").readlines()
    print(pt1(input))
    print(pt2(input))
