#!/usr/bin/env python3
import aoc20
import sys


def pt1(_in):
    me = int(_in[0])
    busses = [int(s) for s in _in[1].split(",") if s != "x"]
    time = me
    while True:
        for bus in busses:
            if time % bus == 0:
                return (time - me) * bus
        time += 1


def mul_inv(a, m):
    return pow(a, -1, mod=m)


def pt2(_in):
    busses = {}
    for i, s in enumerate(_in[1].strip().split(",")):
        if s != "x":
            busses[i] = int(s)
    N = 1
    for dep, bus in busses.items():
        N *= bus
    x = 0
    for dep, bus in busses.items():
        x += -dep * (N // bus) * mul_inv(N // bus, bus)
    return x % N


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 13)
    print(pt1(input))
    print(pt2(input))
