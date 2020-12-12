#!/usr/bin/env python3
import aoc20
import sys


def pt1(_in):
    x, y = 0, 0
    dirs = ((1, 0), (0, -1), (-1, 0), (0, 1))
    dir = 0
    for inst in _in:
        action, amount = inst[0], int(inst[1:])
        if action == "N":
            y -= amount
        elif action == "W":
            x -= amount
        elif action == "S":
            y += amount
        elif action == "E":
            x += amount
        elif action == "F":
            x += dirs[dir][0] * amount
            y += dirs[dir][1] * amount
        elif action == "L":
            dir = (dir + amount // 90) % 4
        elif action == "R":
            dir = (dir - amount // 90) % 4
    return abs(x) + abs(y)


def pt2(_in):
    ship_x, ship_y = 0, 0
    wp_x, wp_y = 10, -1
    for inst in _in:
        action, amount = inst[0], int(inst[1:])
        if action == "N":
            wp_y -= amount
        elif action == "W":
            wp_x -= amount
        elif action == "S":
            wp_y += amount
        elif action == "E":
            wp_x += amount
        elif action == "F":
            ship_x += wp_x * amount
            ship_y += wp_y * amount
        elif action == "L":
            for _ in range((amount//90) % 4):
                wp_x, wp_y = wp_y, -wp_x
        elif action == "R":
            for _ in range((amount//90) % 4):
                wp_x, wp_y = -wp_y, wp_x
    return abs(ship_x) + abs(ship_y)


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 12)
    print(pt1(input))
    print(pt2(input))
