#!/usr/bin/env python3
import aoc20
import sys


def read(lines):
    board = {}
    h = len(lines)
    w = len(lines[0])
    for y in range(h):
        for x in range(w):
            if lines[y][x] == "L":
                board[(x, y)] = 0
            elif lines[y][x] == ".":
                board[(x, y)] = -1
    return board, w, h


def amount_neighbours_occ(p, board):
    amount = 0
    for dy in range(-1, 1+1):
        for dx in range(-1, 1+1):
            if dy == dx == 0:
                continue
            new_p = (p[0] + dx, p[1] + dy)
            if new_p in board and board[new_p] == 1:
                amount += 1
    return amount


def pt1(_in):
    board, w, h = read(_in)
    while True:
        prev_board = board.copy()
        for p, state in prev_board.items():
            if state == 0:
                # empty
                if amount_neighbours_occ(p, prev_board) == 0:
                    board[p] = 1
            if state == 1:
                # occ
                if amount_neighbours_occ(p, prev_board) >= 4:
                    board[p] = 0
        if prev_board == board:
            break
        prev_board = board
    res = 0
    for _, state in board.items():
        if state == 1:
            res += 1
    return res


def amount_in_sight_occ(p, board, w, h):
    amount = 0
    dirs = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
    for dir in dirs:
        step = 0
        while True:
            step += 1
            new_p = p[0] + dir[0] * step, p[1] + dir[1] * step
            if new_p not in board:
                break
            if board[new_p] == -1:
                continue
            if board[new_p] == 1:
                amount += 1
            break
    return amount


def pt2(_in):
    board, w, h = read(_in)
    while True:
        prev_board = board.copy()
        for p, state in prev_board.items():
            if state == 0:
                # empty
                if amount_in_sight_occ(p, prev_board, w, h) == 0:
                    board[p] = 1
            if state == 1:
                # occ
                if amount_in_sight_occ(p, prev_board, w, h) >= 5:
                    board[p] = 0
        if prev_board == board:
            break
        prev_board = board
    res = 0
    for _, state in board.items():
        if state == 1:
            res += 1
    return res


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 11)
    print(pt1(input))
    print(pt2(input))
