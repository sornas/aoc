#!/usr/bin/env python3
import aoc20
import sys


def pt1(_in):
    things = []
    for line in _in[:20]:
        thing = []
        line = line.strip().split(": ")
        for a in line[1].split(" or "):
            b = a.split("-")
            thing.append(range(int(b[0]), int(b[1])+1))
        things.append(thing)
    res = 0
    for line in _in[25:]:
        for n in line.strip().split(","):
            n = int(n)
            valid = False
            for thing in things:
                if any(n in r for r in thing):
                    valid = True
                    break
            if not valid:
                res += n
    return res


def pt2(_in):
    constraints = []
    for line in _in[:20]:
        thing = []
        line = line.strip().split(": ")
        for a in line[1].split(" or "):
            b = a.split("-")
            thing.append(range(int(b[0]), int(b[1])+1))
        constraints.append(thing)

    tickets = []
    for line in _in[25:]:
        valid_ticket = True
        for n in line.strip().split(","):
            n = int(n)
            valid_field = False
            for thing in constraints:
                if any(n in r for r in thing):
                    valid_field = True
                    break
            if not valid_field:
                valid_ticket = False
                break
        if valid_ticket:
            tickets.append(list(int(n) for n in line.strip().split(",")))

    # for each field
    #   assume it can be anything
    candidates = [set(range(20)) for _ in range(20)]  # one set per field

    for t, ticket in enumerate(tickets):
        for f, field in enumerate(ticket):
            for c, constraint in enumerate(constraints):
                if c in candidates[f] and not any(field in cons for cons in constraint):
                    candidates[f].remove(c)

    know = [-1 for _ in range(20)]
    while any(len(c) > 0 for c in candidates):
        for c, cand in enumerate(candidates):
            if len(cand) == 1:
                know[c] = cand.pop()
                to_remove = know[c]
                break
        for cand in candidates:
            if to_remove in cand:
                cand.remove(to_remove)

    my = list(int(n) for n in _in[22].strip().split(","))
    res = 1
    for f, field in enumerate(know):
        if field < 6:
            res *= my[f]
    return res


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 16)
    print(pt1(input))
    print(pt2(input))
