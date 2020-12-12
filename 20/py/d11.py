#!/usr/bin/env python3
import aoc20
import sys
import functools


def vis(board):
    s = ""
    for r in board:
        for c in r:
            s += "T" if c[0] else "F"
            s += str(c[1]) if c[1] >= 0 else "-"
            s += str(c[2])
            s += " "
        s += "\n"
    return s


def read(lines):
    board = []
    h = len(lines)
    w = len(lines[0]) - 1
    for y in range(h):
        row = []
        for x in range(w):
            if lines[y][x] == "L":
                row.append([False, 0, 0, []])
            elif lines[y][x] == ".":
                row.append([False, -1, 0, []])
        board.append(row)

    def update_in_sight(x, y):
        for dy in range(-1, 1+1):
            for dx in range(-1, 1+1):
                if dy == dx == 0:
                    continue
                step = 0
                while True:
                    step += 1
                    px, py = x + (dx * step), y + (dy * step)
                    if px < 0 or px >= w or py < 0 or py >= h:
                        break
                    if board[py][px][1] != -1:
                        board[py][px][3].append((x, y))
                        break

    for y in range(h):
        for x in range(w):
            update_in_sight(x, y)
    return board, w, h


@functools.cache
def neighbours_occ(p, w, h):
    n = []
    for dy in range(-1, 1+1):
        py = p[1] + dy
        if 0 <= py < h:
            for dx in range(-1, 1+1):
                if dy == dx == 0:
                    continue
                px = p[0] + dx
                if 0 <= px < w:
                    n.append((px, py))
    return n


def pt1(_in):
    board, w, h = read(_in)
    while True:
        changed = False
        for y in range(h):
            for x in range(w):
                if not board[y][x][0] and board[y][x][1] == 0:
                    changed = True
                    board[y][x][0] = True
                    for nx, ny in neighbours_occ((x, y), w, h):
                        board[ny][nx][2] += 1
                if board[y][x][0] and board[y][x][1] >= 4:
                    changed = True
                    board[y][x][0] = False
                    for nx, ny in neighbours_occ((x, y), w, h):
                        board[ny][nx][2] -= 1
        for y in range(h):
            for x in range(w):
                if board[y][x][1] != -1:
                    board[y][x][1] = board[y][x][2]
        if not changed:
            break
    res = 0
    for y in range(h):
        for x in range(w):
            if board[y][x][0]:
                res += 1
    return res


def pt2(_in):
    board, w, h = read(_in)
    while True:
        changed = False
        for y in range(h):
            for x in range(w):
                if not board[y][x][0] and board[y][x][1] == 0:
                    changed = True
                    board[y][x][0] = True
                    for nx, ny in board[y][x][3]:
                        board[ny][nx][2] += 1
                if board[y][x][0] and board[y][x][1] >= 5:
                    changed = True
                    board[y][x][0] = False
                    for nx, ny in board[y][x][3]:
                        board[ny][nx][2] -= 1
        for y in range(h):
            for x in range(w):
                if board[y][x][1] != -1:
                    board[y][x][1] = board[y][x][2]
        if not changed:
            break
    res = 0
    for y in range(h):
        for x in range(w):
            if board[y][x][0]:
                res += 1
    return res


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 11)
    print(pt1(input))
    print(pt2(input))
