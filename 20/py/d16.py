#!/usr/bin/env python3
import aoc20
import sys
from functools import reduce


def pt1(_in):
    return sum(sum(int(field)
                   for field in line.strip().split(",")
                   if not any(any(int(field) in cons
                                  for cons in constraint)
                              for constraint in [[range(int(a.split("-")[0]),
                                                        int(a.split("-")[1])+1)
                                                  for a in line.split(": ")[1]
                                                               .split(" or ")]
                                                 for line in _in[:20]]))
               for line in _in[25:])


def pt2(_in):
    constraints = [[range(int((b := a.split("-"))[0]), int(b[1])+1)
                    for a in line.split(": ")[1].split(" or ")]
                   for line in _in[:20]]

    # all(any(any())) => ALL numbers on a ticket match ANY constraint in ANY constraint group
    tickets = [[int(n) for n in line.strip().split(",")]
               for line in _in[25:]
               if all(any(any(int(n) in cons
                              for cons in constraint)
                          for constraint in constraints)
                      for n in line.strip().split(","))]

    # for each field
    #   assume it can be anything
    candidates = [set(range(20)) for _ in range(20)]  # one set per field

    for ticket in tickets:
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
        for cand in candidates:
            if to_remove in cand:
                cand.remove(to_remove)

    return reduce(lambda x, y: x * y,
                  (int(_in[22].strip().split(",")[f])
                   for f, field in enumerate(know)
                   if field < 6),
                  1)


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 16)
    print(pt1(input))
    print(pt2(input))
