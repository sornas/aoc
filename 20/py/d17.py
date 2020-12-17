#!/usr/bin/env python3
import aoc20
import sys
import functools
from collections import defaultdict


@functools.cache
def neighbours3(p):
    res = set()
    for dx in range(-1, 1+1):
        for dy in range(-1, 1+1):
            for dz in range(-1, 1+1):
                if dx == dy == dz == 0:
                    continue
                res.add((p[0] + dx, p[1] + dy, p[2] + dz))
    return res


def pt1(_in):
    active = set()
    board = defaultdict(lambda: 0)
    for y in range(len(_in)):
        for x in range(len(_in[y])):
            if _in[y][x] == "#":
                active.add((x, y, 0))
                for n in neighbours3((x, y, 0)):
                    board[n] += 1

    for _ in range(6):
        new_board = defaultdict(lambda: 0)
        new_active = set()
        for p, deg in board.items():
            if p in active and 2 <= deg <= 3:
                new_active.add(p)
                for n in neighbours3(p):
                    new_board[n] += 1
            elif p not in active and deg == 3:
                new_active.add(p)
                for n in neighbours3(p):
                    new_board[n] += 1
        board = new_board
        active = new_active
    return(len(active))


@functools.cache
def neighbours4(p):
    res = set()
    for dx in range(-1, 1+1):
        for dy in range(-1, 1+1):
            for dz in range(-1, 1+1):
                for dw in range(-1, 1+1):
                    if dx == dy == dz == dw == 0:
                        continue
                    res.add((p[0] + dx, p[1] + dy, p[2] + dz, p[3] + dw))
    return res


def pt2(_in):
    active = set()
    board = defaultdict(lambda: 0)
    for y in range(len(_in)):
        for x in range(len(_in[y])):
            if _in[y][x] == "#":
                active.add((x, y, 0, 0))
                for n in neighbours4((x, y, 0, 0)):
                    board[n] += 1

    for _ in range(6):
        new_board = defaultdict(lambda: 0)
        new_active = set()
        for p, deg in board.items():
            if p in active and 2 <= deg <= 3:
                new_active.add(p)
                for n in neighbours4(p):
                    new_board[n] += 1
            elif p not in active and deg == 3:
                new_active.add(p)
                for n in neighbours4(p):
                    new_board[n] += 1
        board = new_board
        active = new_active
    return(len(active))


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 17)
    print(pt1(input))
    print(pt2(input))
