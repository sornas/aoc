#!/usr/bin/env python3
import aoc20
import sys


def pt1(_in):
    res = 0
    questions = {s for s in "abcdefghijklmnopqrstuvwxyz"}
    for line in _in:
        if line == "\n":
            res += 26 - len(questions)
            questions = {s for s in "abcdefghijklmnopqrstuvwxyz"}
            continue
        for ans in line:
            if ans in questions:
                questions.remove(ans)
    res += 26 - len(questions)
    return res


def pt2(_in):
    res = 0
    questions = {s for s in "abcdefghijklmnopqrstuvwxyz"}
    for line in _in:
        person = set()
        if line == "\n":
            res += len(questions)
            questions = {s for s in "abcdefghijklmnopqrstuvwxyz"}
            continue
        for ans in line:
            person.add(ans)
        for q in questions.copy():
            if q not in person:
                questions.remove(q)
    res += len(questions)
    return res


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 6)
    print(pt1(input))
    print(pt2(input))
