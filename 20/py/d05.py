#!/usr/bin/env python3
import sys


def bin(lo, hi, x):
    mid = (hi+lo)//2
    if x in "BR":
        # upper
        return (mid + 1, hi)
    else:
        return (lo, mid)


def pt1(_in):
    highest = 0
    for board in _in:
        r_lo, r_hi = 0, 127
        for r in board[:7]:
            r_lo, r_hi = bin(r_lo, r_hi, r)
        c_lo, c_hi = 0, 7
        for c in board[7:]:
            c_lo, c_hi = bin(c_lo, c_hi, c)
        i = r_lo*8+c_lo
        if i > highest:
            highest = i
    return highest


def pt2(_in):
    seats = []
    for board in _in:
        r_lo, r_hi = 0, 127
        for r in board[:7]:
            r_lo, r_hi = bin(r_lo, r_hi, r)
        c_lo, c_hi = 0, 7
        for c in board[7:]:
            c_lo, c_hi = bin(c_lo, c_hi, c)
        seats.append(r_lo*8+c_lo)
    seats = sorted(seats)
    for i in range(len(seats) - 1):
        if seats[i+1] == seats[i] + 2:
            return seats[i] + 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = open(sys.argv[1], "r").readlines()
    else:
        input = open("../input/05", "r").readlines()
    print(pt1(input))
    print(pt2(input))
