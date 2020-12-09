#!/usr/bin/env python3
import sys
import time


def parse(prog):
    return [[(l := line.strip().split())[0], int(l[1])] for line in prog]


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
    return run(_in)[1]


def pt2(_in):
    for i in range(len(_in)):
        prog = _in.copy()
        inst, offset = prog[i]
        if inst == "jmp":
            prog[i][0] = "nop"
        elif inst == "nop":
            prog[i][0] = "jmp"
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
    start = time.time()
    input = parse(input)
    print(pt1(input))
    print("pt1 {:.3}".format(time.time() - start))
    print(pt2(input))
    print("pt2 {:.3}".format(time.time() - start))
