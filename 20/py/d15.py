#!/usr/bin/env python3
import aoc20
import sys


def say_nth(start, nth):
    amount = len(start)
    cur = start[-1]
    prev = {n: i for i, n in enumerate(start)}
    while amount < nth:
        if cur not in prev:
            new = 0
            prev[cur] = amount - 1
        else:
            new = amount - 1 - prev[cur]
            prev[cur] = amount - 1
        cur = new
        amount += 1
    return cur


def pt1(_in):
    return say_nth([int(n) for n in _in[0].split(",")], 2020)


def pt2(_in):
    return say_nth([int(n) for n in _in[0].split(",")], 30000000)


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 15)
    print(pt1(input))
    print(pt2(input))
