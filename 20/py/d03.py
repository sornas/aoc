#!/usr/bin/env python3
import aoc20
import sys


def pt1(_in):
    squares = set()
    trees = set()
    for y in range(len(_in)):
        for x in range(len(_in[y])):
            if _in[y][x] == ".":
                squares.add((x, y))
            else:
                trees.add((x, y))
    h = len(_in)
    w = len(_in[0]) - 1 # \n
    amount = 0
    x, y = 0, 0
    while y < h:
        x += 3
        y += 1
        if (x % w, y) in trees:
            amount += 1
    return amount


def pt2(_in):
    squares = set()
    trees = set()
    for y in range(len(_in)):
        for x in range(len(_in[y])):
            if _in[y][x] == ".":
                squares.add((x, y))
            else:
                trees.add((x, y))
    h = len(_in)
    w = len(_in[0]) - 1 # \n
    amounts = []
    for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        amount = 0
        x, y = 0, 0
        while y < h:
            x += slope[0]
            y += slope[1]
            if (x % w, y) in trees:
                amount += 1
        amounts.append(amount)
    s = 1
    for a in amounts:
        s *= a
    return s


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 3)
    print(pt1(input))
    print(pt2(input))
